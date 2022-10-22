import argparse
import json
import os
import random
from pathlib import Path
from time import sleep

import openai
from langs_util import LANG_EXTS

MAX_TOKENS_PER_MIN = 150000
CODE_DELIM = '```'
DISALLOWED_DEFAULT = ['numpy', 'pandas', 'dataframe', *LANG_EXTS]


# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb
# define a retry decorator
def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
    errors: tuple = (openai.error.RateLimitError,),
):
    """Retry a function with exponential backoff."""

    def wrapper(*args, **kwargs):
        # Initialize variables
        num_retries = 0
        delay = initial_delay

        # Loop until a successful response or max_retries is hit or an exception is raised
        while True:
            try:
                return func(*args, **kwargs)

            # Retry on specified errors
            except errors:
                # Increment retries
                num_retries += 1

                # Check if max retries has been reached
                if num_retries > max_retries:
                    raise Exception(
                        f'Maximum number of retries ({max_retries}) exceeded.'
                    )

                # Increment the delay
                delay *= exponential_base * (1 + jitter * random.random())

                # Sleep for the delay
                sleep(delay)

            # Raise exceptions for any errors not specified
            except Exception as e:
                raise e

    return wrapper


@retry_with_exponential_backoff
def completion_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='+',
                        default=['./conala-corpus-v1.1/conala-test.json'],
                        help='JSON input file locations')
    parser.add_argument('-k', '--key',
                        default='intent',
                        help='key containing prompt')
    parser.add_argument('-l', '--langs', nargs='+',
                        default=['Java', 'Python'],
                        help='languages to translate into')
    parser.add_argument('-d', '--disallowed', nargs='+',
                        default=DISALLOWED_DEFAULT,
                        help='disallowed prompt terms')
    parser.add_argument('-t', '--tokens',
                        default=500,
                        help='max tokens per output')
    parser.add_argument('-m', '--model',
                        default='code-davinci-002',
                        help='OpenAI model to use')
    parser.add_argument('-o', '--output',
                        default='../data',
                        help='output directory')

    args = parser.parse_args()
    langs: list[str] = [lang for lang in args.langs if lang in LANG_EXTS]
    out_path = Path(args.output)

    openai.api_key = os.getenv('OPENAI_API_KEY')

    disallowed_terms: list[str] = [d.casefold() for d in args.disallowed]

    for inp in args.input:
        in_path = Path(inp)
        ds = json.loads(in_path.read_text(encoding='utf-8'))
        prompts: list[str] = list(set(e[args.key] for e in ds))
        prompts = [
            prompt for prompt in prompts
            if not any(x in prompt.casefold() for x in disallowed_terms)
        ]
        ds_path = out_path / f'{in_path.stem}_{args.model}'
        prompts_path = ds_path / 'prompts'
        prompts_path.mkdir(parents=True, exist_ok=True)

        for lang in langs:
            lang_path = ds_path / lang
            lang_path.mkdir(exist_ok=True)

        for i, prompt in enumerate(prompts):
            lang_to_res: dict[str, str] = {}

            for lang in langs:
                response = completion_with_backoff(
                    model=args.model,
                    prompt=f'### {prompt}\n### {lang}\n',
                    temperature=0,
                    max_tokens=args.tokens,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=['###']
                )
                stripped_text = response.choices[0].text.strip()
                lines: list[str] = stripped_text.splitlines()
                if len(lines) < 2:
                    break
                if CODE_DELIM in lines[0]:
                    del lines[0]
                if CODE_DELIM in lines[-1]:
                    del lines[-1]
                lines = [line.removeprefix('>>> ').rstrip() for line in lines]
                # lines.append('')
                lang_to_res[lang] = "\n".join(lines)

            if len(lang_to_res) != len(langs):
                continue
            prompt_path = prompts_path / f'{i}.txt'
            prompt_path.write_text(prompt, encoding='utf-8', newline='\n')

            for lang, res in lang_to_res.items():
                res_path = ds_path / lang / f'{i}.{LANG_EXTS[lang]}'
                res_path.write_text(res, encoding='utf-8', newline='\n')


if __name__ == "__main__":
    main()
