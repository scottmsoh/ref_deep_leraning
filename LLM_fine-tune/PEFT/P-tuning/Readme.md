
P-tuning (GPT Understand, Too)
&nbsp;

Devised a Prompt Encoder (LSTM) to enable searching for more appropriate prompts in continuous space.</br>
Shows improvement in a major problem where there was a large difference in performance depending on how the sentence was structured.</br>
When P-Tuning was applied to NLU, which was the weak point of the one-way model GPT, it showed performance equivalent to the bi-directional model BERT.</br>

&nbsp;

<img width="1323" alt="image" src="https://github.com/user-attachments/assets/a14a5339-3882-40a2-9b59-b0c359db3f48">

&nbsp;

GPT shows huge gaps from minimal differences within prompt context
<img width="1183" alt="image" src="https://github.com/user-attachments/assets/4d356e03-2fd5-41d8-ad81-0080908fd856">

&nbsp;

There are many researches regarding prompt search, one is AutoPrompt but this method still have a limitation for discrete words, not continuous vetors. 
<img width="1086" alt="image" src="https://github.com/user-attachments/assets/1c4dcf31-70b8-4c71-a844-8822847db73e">

&nbsp;

LLMs such as GPT, BERT did not show proper improvement from fine-tuning but the p-tuning presents reasonable outcomes
<img width="1030" alt="image" src="https://github.com/user-attachments/assets/9042be0a-91b7-4d2d-8de7-ef7dc7e3082c">

&nbsp;

<img width="1320" alt="image" src="https://github.com/user-attachments/assets/2c267a48-5f72-47e1-ab97-2684cb2de8e0">
