# Stack Overflow Python Q&A Dataset for LLM Evaluation

This repository contains a cleaned subset of Stack Overflow questions and answers about the Python programming language, prepared for the study:

> A Semantic and Lexical Analysis of LLM-Generated Responses in Comparison with Stack Overflow Answers

## 1. Dataset Description

The file `data/stackoverflow_cleaned.csv` includes question–answer pairs collected via the Stack Exchange API. Each row corresponds to one Python question and its accepted human-written answer, together with the GPT-4o-mini response used in the experiments.

Main columns (simplify/adjust to your real schema):

- `question_id`: Stack Overflow question identifier  
- `title`: Question title (plain text)  
- `body`: Question body (cleaned HTML / text)  
- `answer_id`: Accepted answer identifier  
- `human_answer`: Human-written accepted answer text  
- `gpt_answer`: GPT-4o-mini answer generated for this question  
- additional metadata columns used in the paper (e.g., lengths, similarity scores), if present

The final dataset used in the paper contains 331 question–answer pairs after cleaning and filtering. [file:1][file:19]

## 2. Data Collection and Preprocessing

Data were collected via the Stack Exchange API (`https://api.stackexchange.com/`) using the `python` tag and restricted to questions with at least one accepted answer.

Key preprocessing steps:

- Removed records with missing or empty title, question body, or accepted answer.
- Applied length thresholds for title, body, and answer text to exclude extremely short entries.
- Deduplicated records based on `question_id`.
- Fixed or removed entries with invalid UTF-8 encoding.

The full preprocessing pipeline is implemented in `src/clean-data.py`.

## 3. License and Attribution

All original question and answer content is copyright its respective Stack Overflow contributors and is made available under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license, as specified in the Stack Overflow / Stack Exchange licensing terms.
When using this dataset, you **must**:

- Provide appropriate credit to Stack Overflow and the original contributors.  
- Include a link to the original content where feasible (e.g., via `question_id` and `answer_id`).  
- Share any derivative dataset under the same CC BY-SA 4.0 license.

A suggested attribution statement:

> This dataset includes content from Stack Overflow (https://stackoverflow.com), user contributions licensed under CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).

All code in this repository (e.g., data collection and cleaning scripts) is released under the MIT License (see `LICENSE`), and **does not** change the license of the Stack Overflow content itself.

## 4. How to Cite

If you use this dataset in academic work, please cite the accompanying paper:

> Çelepkolu, K. C., & Ortakçı, Y. (2026). *A Semantic and Lexical Analysis of LLM-Generated Responses in Comparison with Stack Overflow Answers*.

You may also optionally reference this repository:

> Dataset and code: https://github.com/keremclp/A-Semantic-and-Lexical-Analysis-of-LLM-Generated-Responses-in-Comparison-with-Stack-Overflow-Answers

## 5. Disclaimer

This repository is an independent research artifact and is **not** officially affiliated with or endorsed by Stack Overflow or Stack Exchange. Users are responsible for ensuring that their use of the data complies with the Stack Exchange Terms of Service and the CC BY-SA 4.0 license.
