
## LLM Evaluation

1. SOTA LLM Evaluation Using GPT-4, HyperCLOVA X, and Gemini

This repository contains an evaluation of state-of-the-art large language models (LLMs) such as GPT-4, HyperCLOVA X, and Gemini. The evaluation assesses the appropriateness of the models' responses to given instructions.</br>

## Evaluation Methodology

1. **Evaluation Using SOTA LLMs**:
   - We utilize models like GPT-4, HyperCLOVA X, and Gemini to evaluate the appropriateness of responses to instructions.
   - This is one of the simplest evaluation methods and is widely used in various research papers and studies.

2. **Challenges**:
   - Although the same instructions and responses are used in each trial, the scores can vary significantly between trials, indicating inconsistency in measurement.

3. **Establishing Confidence Intervals**:
   - By increasing the number of trials and considering the variability of the scores, we establish confidence intervals to estimate the range within which the true score likely falls.

## Statistical Comparison of Models

The table below summarizes the statistical comparison between Model A and Model B based on their evaluation scores.

| Statistic | Model A                    | Model B                    |
|-----------|----------------------------|----------------------------|
| Score     | [20, 35, 55, 77, 88]       | [40, 45, 50, 60, 70]       |
| Mean      | 55                         | 53                         |
| Median    | 55                         | 50                         |
| STD       | ≈ 27.21                    | ≈ 11.40                    |
| C.I       | SE(A) = 12.17 \| CI = [30.14, 79.86] | SE(B) = 5.10 \| CI = [42.98, 63.02] |

### Detailed Explanation

- **Mean (평균)**: The average score. Model A has a mean of 55, and Model B has a mean of 53.
- **Median (중앙값)**: The middle value of the scores. Model A has a median of 55, and Model B has a median of 50.
- **STD (표준편차)**: The standard deviation, indicating how spread out the scores are from the mean. Model A has a standard deviation of approximately 27.21, while Model B has a standard deviation of approximately 11.40.
- **C.I (신뢰 구간)**: The confidence interval, providing an estimated range that is likely to contain the true mean score. Model A's confidence interval is [30.14, 79.86], and Model B's confidence interval is [42.98, 63.02].
