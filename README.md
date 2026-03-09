[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

# HSK 3.0 2026 Syllabus Dataset

Structured datasets for the Chinese HSK (Hànyǔ Shuǐpíng Kǎoshì) proficiency exam.

This repository contains machine-readable datasets of HSK vocabulary, characters, and grammar structures. The data has been extracted from the publicly available HSK syllabus and reorganized into formats that are easier to use for research, language learning tools, and data analysis.

## Dataset Contents

| File | Description |
|-----|-------------|
| data/hsk_hanzi.csv | HSK character list |
| data/hsk_hanzi_raw.json | HSK character list |
| data/hsk_hanzi_pretty.json | HSK character list |
| data/hsk_hanzi_compact.json | HSK character list |
| data/hsk_vocabulary.csv | HSK vocabulary list |
| data/hsk_vocabulary_raw.json | HSK vocabulary list |
| data/hsk_vocabulary_pretty.json | HSK vocabulary list |
| data/hsk_vocabulary_compact.json | HSK vocabulary list |
| data/hsk_grammar.csv | HSK grammar list |
| data/hsk_grammar_raw.json | HSK grammar list |
| data/hsk_grammar_pretty.json | HSK grammar list |
| data/hsk_grammar_compact.json | HSK grammar list |
| data/hsk_topic.csv | HSK topic list |
| data/hsk_topic_raw.json | HSK topic list |
| data/hsk_topic_pretty.json | HSK topic list |
| data/hsk_topic_compact.json | HSK topic list |
| data/hsk_task.csv | HSK task list |
| data/hsk_task_raw.json | HSK task list |
| data/hsk_task_pretty.json | HSK task list |
| data/hsk_task_compact.json | HSK task list |

All datasets are provided in **CSV and JSON formats** for compatibility with spreadsheets, databases, and programming environments.  

JSON files are available in three versions:  
- `_raw` — unprocessed raw JSON from the API  
- `_compact` — minified JSON for efficient storage  
- `_pretty` — human-readable JSON with indentation  

## Example

| examLevelId | word | type |
|-------------|------|------|
| HSK1 | 爱 | 1 |
| HSK1 | 八 | 1 |
| HSK1 | 爸 | 1 |

## Source

The original data comes from the official HSK syllabus published by Chinese Testing International.

Source website:
https://www.chinesetest.cn/

This repository does not claim ownership of the original content. The data has only been reorganized and converted into structured datasets for educational and research purposes.

All trademarks and original materials belong to their respective owners.

## Reproducibility

Scripts used to fetch and convert the data are included in the scripts directory.

Typical workflow:

1. Fetch raw JSON data from the HSK API
2. Save raw JSON files
3. Convert JSON files to CSV
4. Clean formatting and normalize text

Example:

python scripts/fetch_data.py
python scripts/json_to_csv.py

## Usage

You are free to use this dataset for:

- research
- educational tools
- language learning apps
- data analysis

Please provide attribution to the original source when possible.

## License

This repository is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).