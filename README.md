# Group 3: The evaluation of Java-Python code translation using scraped and generated datasets


# General
This repository provides a way to fine-tune 2 models ([CodeBERT](https://github.com/microsoft/CodeBERT) and [PLBART](https://github.com/wasiahmad/PLBART)) on a scraped and generated dataset and evaluate these fine-tuned models on two metrics, namely Bleu-4 and xMatch. 
The evaluation and fine-tuning of the models has been n/adapted from [CodeXGLUE](https://github.com/microsoft/CodeXGLUE) and the preprocessing of the data is done by [AVATAR](https://github.com/wasiahmad/AVATAR).


# Dataset
The dataset consists of data scraped from [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code), [Sample Programs](https://sampleprograms.io/languages/), [Coding Bat](https://codingbat.com/), [A problem solved in 22 programming languages](https://andrewshitov.com/2020/12/07/a-problem-solved-in-22-programming-languages/) and [LeetCode](https://walkccc.me/LeetCode/).
Furthermore, it has been extended with data generated by the [OpenAI Codex](https://openai.com/blog/openai-codex/).


# Installation

After cloning a `pip install -r requirements.txt` is required to install the appropriate packages for running the fine-tuning and evaluation.

### Scraping
TBA

### Data Generation
TBA

### Pre-processing
The pre-processing is done by first setting `output_file` (indicating the location and name of the output file) and setting `from_directory` (indicating the directory containing the java-python files).
**Note that the python and java files should be in the same directory and have the same name (with the `.java` and `.py` extension respectively)**

The pre-processing can then be done by running the following commands (requires conda):
```shell
cd ./fine_tuning
git clone https://github.com/wasiahmad/AVATAR.git
cd ./AVATAR
install_env.sh
pip install -r requirements.txt
cd ../../
python3 ./fine_tuning/process.py
```

### Fine-tuning

A script for running the evaluation is provided which can be run using:
```bash
./fine_tuning/train_and_test.java roberta #or plbart
```
This will run the training with the settings provided in the script file (default of 50000 training steps and a batch size of 4). To change from Java-Python translation to Python-Java translation, switch the order of the files given to `--train_filename` and `dev_filename`.


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