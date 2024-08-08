
## Fine-tune methodologies
ref: https://www.labellerr.com/blog/comprehensive-guide-for-fine-tuning-of-llms/<br>

1. Question Answering
2. Language Generation
3. NER (Named Entity Recognition)
4. Sentiment Analysis
5. Summarization
6. Parapharase identification
7. others

![image](https://github.com/user-attachments/assets/828ec842-64e3-4394-ac4d-1bf744b950a4)


## Fine-tune Research

When Scaling Meets LLM Fine-Tuning: The Effect of Data, Model and Fine-Tuning Method:</br>
This paper explores various fine-tuning methods such as Full-Model Tuning (FMT), Prompt Tuning, and Low-Rank Adaptation (LoRA). It examines the impact of scaling different factors like model size and pre-training data size on the performance of LLMs. The study highlights that while small-scale fine-tuning can yield decent results, larger-scale fine-tuning data significantly enhances performance for well-defined downstream applications​ (ar5iv)​.</br>
https://ar5iv.labs.arxiv.org/html/2402.17193


LoftQ: Reimagining LLM Fine-Tuning with Smarter Initialization:</br>
Presented at ICLR 2024, LoftQ introduces a method combining quantization and adaptive initialization. Quantization reduces the precision of model parameters, lowering memory and computation needs. This approach is based on principles from LoRA and QLoRA and aims to preserve model capabilities while reducing resource usage. LoftQ's tests demonstrate strong performance, often surpassing QLoRA configurations on various tasks​ (Microsoft Cloud)​.</br>
https://www.microsoft.com/en-us/research/blog/loftq-reimagining-llm-fine-tuning-with-smarter-initialization/


Representation Fine-Tuning (ReFT):</br>
Developed by Stanford University researchers, ReFT focuses on fine-tuning by modifying less than 1% of a model's parameters. It targets specific parts of the model relevant to the task, achieving state-of-the-art performance in several benchmarks. ReFT methods like LoReFT (Low-rank Linear Subspace ReFT) operate on hidden representations rather than weights, offering a more efficient alternative to traditional parameter-efficient fine-tuning methods​ (TechTalks)​.</br>
https://bdtechtalks.com/2024/04/15/reft-llm-fine-tuning/


Random Masking Finds Winning Tickets for Parameter Efficient Fine-Tuning:</br>
This study investigates a simplified approach to PEFT using Random Masking. The method involves applying random masks to trainable parameters, which leads to effective fine-tuning with fewer parameters. Empirical results show that Random Masking can match the performance of standard PEFT methods such as LoRA, providing a cost-effective solution for fine-tuning LLMs​ (ar5iv)​.</br>
https://ar5iv.labs.arxiv.org/html/2405.02596


LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models:</br>
This paper discusses various adapter-based methods for parameter-efficient fine-tuning. It includes techniques like Series Adapters and Parallel Adapters, which add learnable modules within or alongside specific sublayers of the model. These methods aim to reduce computational complexity while maintaining performance. The paper presents extensive empirical studies on several benchmark datasets, demonstrating the effectiveness of these adapter-based approaches​ (ar5iv)​.</br>
https://ar5iv.labs.arxiv.org/html/2304.01933




