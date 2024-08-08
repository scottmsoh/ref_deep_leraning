

## Pre-fix Tuning

During the fine-tune,</br> 
The model should update the entire parameters. It is getting inefficient because LLMs are becoming huge like 36B parameters.</br>
It definitely will be time consuming so they encourage us to use only 0.1% parameters instead using Prefix Tuning.</br>
It will use only 0.1% of entire LLM's parameters.</br>


<img width="480" alt="image" src="https://github.com/user-attachments/assets/d8c811db-0ab5-40a4-8d29-592ff2580df7">


At GPT2, only utilize one prefix but at BERT who structured Encoder & decoder should use a prefix at each, entirely 2 prefixes.</br>

<img width="1209" alt="image" src="https://github.com/user-attachments/assets/770795cf-523c-4d7b-b1fe-97c9cc885bca">
