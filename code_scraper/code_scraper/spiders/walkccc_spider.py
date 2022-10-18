from dataclasses import dataclass, field
from pathlib import Path

import re
import time
import scrapy


@dataclass
class LangInfo:
    ext: str
    tasks: set[str] = field(default_factory=set)


class WalkcccSpider(scrapy.Spider):
    name = "walkccc"

    def __init__(self, langs: str = 'C++,Java,Python', exts: str = 'cpp,java,py', res_dir: str = '../data', *args, **kwargs):
        super(WalkcccSpider, self).__init__(*args, **kwargs)

        comma_regex: str = r'\s*,\s*'
        lang_list: list[str] = re.split(comma_regex, langs)
        ext_list: list[str] = re.split(comma_regex, exts)

        self.info_lang: dict[str, LangInfo] = {lang: LangInfo(ext) for (lang, ext) in zip(lang_list, ext_list)}
        self.res_dir: Path = Path(res_dir) / f'{self.name}-{int(time.time())}'

        for lang in self.info_lang:
            (self.res_dir / f'{lang}').mkdir(parents=True, exist_ok=True)

        self.download_delay = 0.25
        self.start_urls = ['https://walkccc.me/LeetCode/']

    def parse(self, response):
        problems = response.css('[aria-label="Problems"] a::attr(href)').getall()
        yield from response.follow_all(problems, callback=self.parse_problem)

    def parse_problem(self, response):
        problem = response.css('title::text').get()
        problem = problem.removesuffix(' - LeetCode Solutions').replace('.', '')
        problem = "".join(char if char not in '<>:"/\\|?*' else '_' for char in problem)
        try:
            container = response.css('.tabbed-set.tabbed-alternate')[0]
        except IndexError:
            return
        problem_langs = container.css('label::text').getall()
        problem_langs = [lang for lang in problem_langs if lang in self.info_lang]
        if len(problem_langs) != len(self.info_lang):
            return
        problem_impls = container.css('code')
        for i, lang in enumerate(problem_langs):
            impl_str = "".join(problem_impls[i].css('::text').getall()).rstrip()
            program_path: Path = self.res_dir / lang / f'{problem}.{self.info_lang[lang].ext}'
            program_path.write_text(impl_str, encoding='utf-8', newline='\n')
