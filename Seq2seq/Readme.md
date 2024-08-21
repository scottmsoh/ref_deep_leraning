

## Sequence-to-Sequence (Seq2seq)

paper: https://arxiv.org/pdf/1409.3215</br>

** Introduction:</br> 
We have a problem with the difference between input length and the output length </br>
At the original model architecture, we can only apply for the case when the input and the output are fixed dimension.</br>

Voice recognition, machine translation, and questions answering are the sequence format, so we required the independent method for the sequence to sequence mapping.</br>

** Contribution</br>
With LSTM architecture, they propose the solution for the problem for sequence to sequence</br>

- After encoding the input sequence and transform to fixed dimension vector using LSTM (Encoder)</br>
- Using another LSTM (decoder) for the output sequence.</br>

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*0hNJAH3xgW_6smcsz0vaWw.png)

** Model

LSTM은 $(x_1, ..., x_T)$가 입력될 때 조건부 확률 $p(y_1, ..., y_{T'}|x_1, ..., x_T)$ 생성 <br>
$y_1, ..., y_{T'}$은 입력 길이 T와 다를 수 있는 길이 $T'$을 갖는 inpu sequence에 mapping되는 output sequence <br>
LSTM은 고정된 vector representation인 벡터 $v$를 input seuqnce $(x_1, ..., x_T)$의 마지막 hidden state를 계산하기 위해 사용 <br>
이러한 $v$를 decoder의 hidden state의 initial 값으로 설정하여 $y_1, ..., y_T$의 확률 계산



