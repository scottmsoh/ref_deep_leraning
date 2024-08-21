

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

Model



