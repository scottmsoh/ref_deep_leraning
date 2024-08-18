

## ULMFiT (Universal Language Model Fine-tuning)

Universal Language Model Fine-tuning for Text Classification</br>
https://arxiv.org/pdf/1801.06146﻿</br>


1) Gradual unfreezing</br>
2) Discriminative fine-tuning</br>

When creating the training dataset for fine-tuning,</br>
you can use 40% pre-training data and 60% new domain data (ratio adjustment is important).</br>
Cons:</br>
Data preparation can become complex.</br>
Training time may increase.</br>
The pre-training data format may differ from the fine-tuning data (e.g., QA).</br> 
In such cases, the QA dataset may need to be reformatted (e.g., "Question: {question} Answer: {answer}").</br>

### QA data conversion (example)
```python
qa_texts = [] 
for item in qa_data: 
    context = item['context'] 
    for qa_pair in item['qas']: 
        question = qa_pair['question'] 
        answer = qa_pair['answers'][0]['text']  # use first answer
        qa_text = f"context: {context}\nquestions: {question}\nanswers: {answer}" 
        qa_texts.append(qa_text)
```

3) Slanted triangular learning rates</br>
