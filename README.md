# Group 3: Evaluating Java-Python code translation using scraped and generated datasets

This repository provides a way to fine-tune 2 models ([CodeBERT](https://github.com/microsoft/CodeBERT) and [PLBART](https://github.com/wasiahmad/PLBART)) on a scraped and generated dataset and evaluate these fine-tuned models on two metrics, namely Bleu-4 and xMatch.
The evaluation and fine-tuning of the models has been adapted from [CodeXGLUE](https://github.com/microsoft/CodeXGLUE) and the preprocessing of the data is done by [AVATAR](https://github.com/wasiahmad/AVATAR).


# Dataset

The dataset consists of data scraped from [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code), [Sample Programs](https://sampleprograms.io/languages/), [CodingBat](https://codingbat.com/), [A problem solved in 22 programming languages](https://andrewshitov.com/2020/12/07/a-problem-solved-in-22-programming-languages/) and [LeetCode](https://walkccc.me/LeetCode/).
Furthermore, it has been extended with data generated by the [OpenAI Codex](https://openai.com/blog/openai-codex/).

The datasets used for experimentation can be found in the folder `train_test_data`, the training set including generated data is found in the files `augmented_train.[py|java]`. Running the pre-processing might result in a slightly different resulting dataset as the pre-processing has been slightly adjusted.


# Installation

Aside from the standard local setup, which supports replicating all steps, a Docker setup for fine-tuning and testing on the final datasets is provided.

To ensure that the environment is set up correctly and models can generate predictions, `python3 train_and_test.py -b 1 -s 100 -e` can be executed from the `fine_tuning` directory in the case of local setup. Alternatively, `docker run --gpus all ghcr.io/ml4se2022/group3:latest -b 1 -s 100 -e` can be used for Docker. In both instances the `-e` flag replaces the complete datasets with a much smaller one (containing only 2 examples). Note that completing such a short run might still require some minutes. The output of the predictions should be available in `test_0.output`.


## Docker Setup

To pull and run the latest image without building it yourself use: `docker run --gpus all ghcr.io/ml4se2022/group3:latest`.

This starts training and testing right away. GPU acceleration should be enabled as long as the proper hardware and drivers are installed on the host machine. Arguments can be added to the end of the command to customize behaviour (e.g., `-h` shows help text).


## Local Setup

Python >=3.9 is recommended. After cloning, a `pip install -r requirements.txt` is required to install the appropriate packages for running the fine-tuning and evaluation (preferably within a [venv](https://docs.python.org/3/library/venv.html)).


### Code Scraping

From the `data_gathering` directory, any of the scrapers can be run through the command `scrapy crawl sitename`, where `sitename` is one of `rosettacode`, `sampleprograms`, or `walkccc`.

All scrapers can be configured with the following options:
- `langs` specifies which languages the scraper should look for
  - only problems implemented in all specified languages will be retrieved
  - currently supported languages: `Java`, `Python`, and `C++`
  - default value: `Java,Python` for all except `walkccc` where it is `C++, Java, Python`
  - example usage: `scrapy crawl sitename -a langs=Java,Python`
- `res_dir` specifies the output directory
  - by default, the `data` directory within the repository root is used
  - example usage: `scrapy crawl sitename -a res_dir="../data"`

Additionally, the `rosettacode` parser has the `rm_drafts` option, which, if set to value `y` (as by default), will not save [draft tasks](https://rosettacode.org/wiki/Category:Draft_Programming_Tasks). Any other value will retain drafts.

Under the aforementioned `data` directory, is a corresponding output for each of the scrapers (`rosettacode` was run with drafts retained, default values were used for all other parameters). Data under `codingbat` and `andrewshitov` was collected manually.


### Data Generation

Synthetic data can be generated with the help of the `code_generator.py` script in the `data_gathering` directory. As it uses the [OpenAI API](https://openai.com/api/), the `OPENAI_API_KEY` environment variable must exist and be valid for successful execution.

**Please keep in mind that usage of the OpenAI API generally incurs a cost that will be billed to the account/organization tied to the supplied key**.

Running `python3 code_generator.py -h` gives an overview of all available configuration options alongside their default values.

As before, the `data` directory holds an output instance of running the generator on the manually curated data from [CoNaLa](https://conala-corpus.github.io/) (both train and test). Prompts were taken from the `intent_field` (another option would be `rewritten_intent`). The input data is also present under `resources/conala-corpus-v1.1`.


### Misc

In the case of both the scrapers and the generator, the currently supported languages are: `C++`, `Java`, `Python`. Adding support for a new language requires updating the `LANG_EXTS` dictionary from `data_gathering/langs_util.py`, which specifies the file extension for each recognized language.

The class `CodeChecker` under `data_gathering/langs_util.py` is currently unused within the scraper or generator, but it can be used to check whether the program stored in a string is syntactically valid through the `is_invalid` instance method. It supports the same languages as the other two tools. In this instance, adding support for more languages would also require adding an appropriate [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) language [parser](https://tree-sitter.github.io/tree-sitter/#available-parsers).


### Pre-processing

The pre-processing is done by first setting `output_file` (indicating the location and name of the output file) and setting `from_directory` (indicating the directory containing the java-python files) in `./fine_tuning/process.py`.

The pre-processing can then be done by running the following commands:
```shell
cd ./fine_tuning
python3 process.py
```

### Fine-tuning

A script for running the evaluation is provided which can be run using:
```bash
cd ./fine_tuning
python3 train_and_test.py
```
This will run the training with the parameters provided in the script file (defaults to CodeBERT model, non-augmented dataset, Java to Python, 50000 training steps and batch size 4). The default command additionally runs testing after training completes. For information on changing any of the parameter values, refer to the output of `python3 train_and_test.py -h`.

# Model Artefacts

All models and outputs of evaluation can be found [here](https://drive.google.com/file/d/1hMEBrahXkBQ6mhLK4YXjwM0MIvajrXVb/view?usp=sharing). There are two folders corresponding with Java to Python Translation (JavaPython) and Python to Java Translation (PythonJava).
Each of the zips within this folder contains the output folder of the training and testing run by `./fine_tuning/train_and_test.py`.
The `test_0.output` file contains the translations of the provided test set. In the `checkpoint-best-ppl` folder within each zip is contained the final fine-tuned model. To evaluate these models, use the following commands:
```bash
cd ./fine_tuning
python3 train_and_test.py -l "./out/checkpoint-best-ppl/pytorch_model.bin"
```


# Results

Java to Python Translation:
| Name                 | Bleu-4 | xMatch |
|----------------------|--------|--------|
| CodeBERT             | 51.33  | 0.0    |
| PLBART               | 62.8   | **2.5126** |
| CodeBERT (Augmented) | 49.57  | 0.5025 |
| PLBART (Augmented)   | **63.44**  | **2.5126** |

Python to Java Translation:
| Name                 | Bleu-4 | xMatch |
|----------------------|--------|--------|
| CodeBERT             | 46.78  | 0.0    |
| PLBART               | **58.43**  | **3.0151** |
| CodeBERT (Augmented) | 45.42  | 0.0    |
| PLBART (Augmented)   | 49.86  | 1.5075 |
