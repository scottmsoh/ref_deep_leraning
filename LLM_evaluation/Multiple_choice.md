

## LLM Evaluation 1st methodology- Multiple-choice Evaluation of LLM Responses

This repository contains an evaluation of large language model (LLM) responses using multiple-choice questions. The evaluation focuses on comparing the accuracy and F1-score of the models' responses.</br>

### 3. Multiple-choice Evaluation

### Methodology

- **Objective Evaluation**:
  - The responses of the models are compared using metrics such as accuracy and F1-score.</br>
  - This method provides an objective measure of the models' performance.</br>

### Evaluation Content (Based on Korean Criteria):

- **Comprehensive Korean Benchmarks**: KMMLU, HAERAE-Bench</br>
- **Common Reasoning**: Hellaswag, Winogrande, PIQA, ARC, CommonsenseQA</br>
- **World Knowledge and Factuality**: Natural Questions, TriviaQA, CLiCk, Factscore</br>
- **Mathematics**: GSM8k, MATH</br>
- **Coding Capabilities**: HumanEval, MBPP</br>
- **Instruction-Following and Chatting Abilities**: MT-Bench</br>
- **Harmlessness**: TruthfulQA, BOLD</br>

### Handling Different Response Formats

- **Few-shot Prompting**:
  - Provide example questions and answer formats as prompts and compare the models' responses.</br>
- **Ground Truth (GT) Based Comparison**:</br>
  - Compare responses against ground truth answers for precise evaluation.</br>


