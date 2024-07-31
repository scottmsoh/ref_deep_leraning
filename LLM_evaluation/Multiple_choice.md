

# Multiple-choice Evaluation of LLM Responses

This repository contains an evaluation of large language model (LLM) responses using multiple-choice questions. The evaluation focuses on comparing the accuracy and F1-score of the models' responses.

## 3. Multiple-choice Evaluation

### Methodology

- **Objective Evaluation**:
  - The responses of the models are compared using metrics such as accuracy and F1-score.
  - This method provides an objective measure of the models' performance.

### Evaluation Content (Based on Korean Criteria):

- **Comprehensive Korean Benchmarks**: KMMLU, HAERAE-Bench
- **Common Reasoning**: Hellaswag, Winogrande, PIQA, ARC, CommonsenseQA
- **World Knowledge and Factuality**: Natural Questions, TriviaQA, CLiCk, Factscore
- **Mathematics**: GSM8k, MATH
- **Coding Capabilities**: HumanEval, MBPP
- **Instruction-Following and Chatting Abilities**: MT-Bench
- **Harmlessness**: TruthfulQA, BOLD

### Handling Different Response Formats

- **Few-shot Prompting**:
  - Provide example questions and answer formats as prompts and compare the models' responses.
- **Ground Truth (GT) Based Comparison**:
  - Compare responses against ground truth answers for precise evaluation.
