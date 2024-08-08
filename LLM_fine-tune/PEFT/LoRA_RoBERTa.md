
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



