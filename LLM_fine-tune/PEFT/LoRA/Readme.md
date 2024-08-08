
## LoRA Fine-tune optimization - RoBERTa Token Classification

#### Hardware Spec CPU/GPU
CPU       : Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz 20 core(40thread) * 2 ea</br>
Memory : 512GB</br>
DISK      : /  ( 440 GB)</br>
             /raid (7 TB)</br>    
GPU : nvidia V100 16GB * 8 ea</br>

### RoBERTa
BERT(Bidirectional Encoder Representations from Transformers)의 개선된 버전입니다. RoBERTa는 더 큰 데이터셋에서 더 긴 시간 동안 학습하여 BERT의 성능을 향상시켰습니다.</br>
Huggingfacee: https://huggingface.co/docs/transformers/v4.44.0/en/model_doc/roberta#transformers.RobertaConfig</br>

-. Dataset: BioNLP2004 NER dataset formatted in a part of TNER project. BioNLP2004 dataset contains training and test only, so we randomly sample a half size of test instances from the training set to create validation set.</br>
Huggingfacee: https://huggingface.co/datasets/tner/bionlp2004</br>

T-NER: An All-Round Python Library for Transformer-based Named Entity Recognition</br>
Huggingface: https://github.com/asahi417/tner</br>
NER Data Structure:</br>
![image](https://github.com/user-attachments/assets/749f6459-6502-482c-919d-557b0b605471)

LoRA Fine-tune: </br> 
After using LoRA, trainable% is 56.19% as the image below. (trainable params: 700,427 || all params: 124,661,782)</br>

<img width="657" alt="image" src="https://github.com/user-attachments/assets/f41c845c-f6fb-44c9-8468-942c0dd7e2fa">

<Training result without LoRA></br>
<img width="560" alt="image" src="https://github.com/user-attachments/assets/a244dd21-f4a3-42a2-9ef5-3b389334b9df">

<Training result with LoRA></br>
<img width="555" alt="image" src="https://github.com/user-attachments/assets/c786e913-a27a-45ba-b578-78248e676543">


Explain: 
# Comparison of Model Performance Before and After Applying LoRA

| Metric             | Before LoRA    | After LoRA     | Difference    |
|--------------------|----------------|----------------|---------------|
| **Validation Loss**| 0.158031       | 0.151547       | -0.006484     |
| **Precision**      | 0.791423       | 0.784485       | -0.006938     |
| **Recall**         | 0.827481       | 0.827120       | -0.000361     |
| **F1 Score**       | 0.809050       | 0.805224       | -0.003826     |
| **Accuracy**       | 0.950083       | 0.949415       | -0.000668     |

## Analysis

- **Validation Loss**: The validation loss decreased after applying LoRA, indicating better generalization performance on the validation data.
- **Precision**: The precision slightly decreased after applying LoRA, but the difference is minimal, and it still maintains a high precision.
- **Recall**: The recall remains almost identical before and after applying LoRA.
- **F1 Score**: The F1 score slightly decreased after applying LoRA, but it still remains high.
- **Accuracy**: The accuracy slightly decreased after applying LoRA, but the difference is minimal, and it still maintains a very high accuracy.

## Conclusion
Although there was a slight decrease in some performance metrics after applying LoRA, the validation loss improved, indicating better generalization performance. This suggests that LoRA can enhance computational efficiency while maintaining high performance.



# Comparison of Power Consumption Before and After Applying LoRA

| Metric                     | Before LoRA          | After LoRA           | Difference        |
|----------------------------|----------------------|----------------------|-------------------|
| **Energy consumed for RAM (kWh)** | 0.597710               | 0.687351               | +0.089641         |
| **RAM Power (W)**          | 188.9085144996643    | 188.9085144996643    | 0                 |
| **Energy consumed for all GPUs (kWh)** | 1.585529               | 1.874576               | +0.289047         |
| **Total GPU Power (W)**    | 477.46172772572896   | 476.03178951650114   | -1.42993820922782  |
| **Energy consumed for all CPUs (kWh)** | 0.134576               | 0.154766               | +0.020190         |
| **Total CPU Power (W)**    | 42.5                 | 42.5                 | 0                 |
| **Total electricity used (kWh)** | 2.317815               | 2.716692               | +0.398877         |

## Analysis

- **Energy consumed for RAM**: The RAM power consumption increased slightly after applying LoRA, indicating that additional parameters might have been stored in RAM.
- **Energy consumed for all GPUs**: GPU power consumption increased after applying LoRA, suggesting that more computations were required.
- **Energy consumed for all CPUs**: CPU power consumption also increased slightly after applying LoRA, indicating an increase in CPU computations.
- **Total electricity used**: Total power consumption increased after applying LoRA, indicating that the overall system consumed more power.

## Conclusion

After comparing the power consumption before and after applying LoRA, it is observed that the model with LoRA consumed slightly more power. This increase in power consumption might be due to the additional computations required by LoRA. However, it is important to evaluate whether this increase in power consumption is acceptable in exchange for the potential performance improvements and efficiency gains offered by LoRA.



