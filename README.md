# Research Project 2024

This project is part of the [Research Project](https://github.com/TU-Delft-CSE/Research-Project) 2024 of [TU Delft](https://https//github.com/TU-Delft-CSE).

## Leveraging Large Language Models for Classifying Deliberative Arguments in Public Discourse.

This study investigates the effectiveness of Large Language Models (LLMs) in identifying and classifying subjective arguments within deliberative
discourse. Using data from a Participatory Value
Evaluation (PVE) conducted in the Netherlands,
this research introduces an annotation strategy that
involves considering whether a data item is an argument, and, if so, extracting the premise(s) of that
argument. Then, the Llama 2 model is used to test
three different prompting approaches: zero-shot,
one-shot and few-shot. The performance is evaluated using the cosine similarity metric and later
enhanced by introducing chain-of-thought prompting.

## Setup
1. Clone Repository
2. Setup Python Version: 3.11.0
3. Run "pip install requirements.txt"

## Data
The dataset used for this research is private and has been removed from the repository. To add your own data, follow these steps:

1. Navigate to the argument/data directory.
2. Create files named Personal_Annotation_{annotator_number}.csv, where annotator_number is an integer.
3. Each file should contain at least three columns:
   - 'question_id': The policy ID related to the question.
   - 'english': The data entry in English.
   - 'Argument': The annotation.

4. To extract the required data, run the extract_data.ipynb notebook.

## LLM responses
To apply zero-shot, one-shot or few-shot learning, run the respective notebooks:
- 'zero_shot.ipynb'
- 'one_shot.ipynb'
- 'few_shot.ipynb'

## Results
To analyze and obtain results, use the following notebooks:
- For results regarding personal annotator labels and majority labels, run 'cosine_similarity.ipynb'.
- For results regarding subjectivity, run 'subjectivity.ipynb'
