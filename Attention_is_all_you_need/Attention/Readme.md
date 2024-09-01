
# Attention Mechanism in Neural Networks

## Table of Contents
1. [Introduction](#introduction)
2. [Contribution](#contribution)
3. [Model](#model)
4. [Attention](#attention)
   - [Luong Attention](#luong-attention)
5. [Encoder](#encoder)
6. [Implementation](#implementation)

## Introduction
The original Seq2seq concept faced limitations in representing entire data using a single context vector at the encoding phase. This issue became particularly significant when dealing with long sequence lengths (corpus).

At here, we are only going to review Loung Attention mechanism, Bahnadau Attention will be reviewd.</br>
**Reference Paper**: [Effective Approaches to Attention-based Neural Machine Translation](https://courses.grainger.illinois.edu/cs546/sp2018/Slides/Mar15_Luong.pdf)

</br>

## Contribution
The key contribution is moving away from fixed-length vector encoding methods.

</br>

## Model
- Loung(post-attention): Utilizes a bidirectional or directional LSTM structure as an encoder, LSTM decoder.
- Bahdanau(pre-attention): Bidirectional RNN as an encoder, GRU as a decoder. 
- Calculates probability for each context vector Ci

The probability is given by:

p(**y**) = Π<sub>t=1</sub><sup>T</sup>p(y<sub>t</sub>|{y<sub>1</sub>, ..., y<sub>t-1</sub>}, c)

</br>

## Attention

## Luong Attention

![Overall structure of attention](https://wikidocs.net/images/page/22893/dotproductattention1_final.PNG)

</br>

#### Step 1: Calculating Attention Scores
![Step 1](https://wikidocs.net/images/page/22893/dotproductattention2_final.PNG)

Compute attention scores through dot product between decoder's hidden state at time t and all encoder hidden states.

![Attention Score Calculation](https://wikidocs.net/images/page/22893/i%EB%B2%88%EC%A7%B8%EC%96%B4%ED%85%90%EC%85%98%EC%8A%A4%EC%BD%94%EC%96%B4_final.PNG)

- Attention score: $ score(s_t, h_i) = s_t^Th_i $
- Attention score collection: $ e^t = [s^T_th_1, ... , s_t^Th_N] $

</br>

#### Step 2: Attention Distribution
![Step 2](https://wikidocs.net/images/page/22893/dotproductattention3_final.PNG)

Apply softmax to $e^t$ to get probability distribution (attention distribution):

$\alpha^t = softmax(e^t)$

</br>

#### Step 3: Context Vector Calculation
![Step 3](https://wikidocs.net/images/page/22893/dotproductattention4_final.PNG)

Compute weighted sum of encoder hidden states:

$ a_t = \Sigma^N_{i=1} \alpha_i^t h_i $

$a_t$ is the context vector.

</br>

#### Step 4: Concatenation
![Step 4](https://wikidocs.net/images/page/22893/dotproductattention5_final_final.PNG)

Concatenate decoder's hidden state $s_t$ with attention value $a_t$.

</br>

#### Step 5: New Vector Calculation
![Step 5](https://wikidocs.net/images/page/22893/st.PNG)

Compute new vector $\tilde{s_t}$:

$ \tilde{s_t} = tanh(\textbf{W}_c[a_t;s_t] + b_c)$

</br>

#### Step 6: Final Output
Compute final output:

$\hat{y_t} = Softmax(\textbf{W}_y\tilde{s_t} + b_y)$

</br>

## Encoder
Uses Bidirectional RNN structure:
- Forward RNN reads input sequence from $x_1$ to $x_{T_x}$
- Backward RNN reads input sequence from $x_{T_x}$ to $x_1$
- Annotation $h_j$ for each word $x_j$ combines forward and backward hidden states

## Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LuongAttention(nn.Module):
    def __init__(self, hidden_dim, vocab_size):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.vocab_size = vocab_size
        self.w_c = nn.Linear(2*hidden_dim, hidden_dim)
        self.w_y = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, query, key, value):
        query = query.unsqueeze(axis=1)
        attention_score = (query @ key)
        attention_distribution = F.softmax(attention_score, dim=-1)
        context_vector = (attention_distribution*value).sum(dim=1)
        concatenate = torch.cat([query.squeeze(), context_vector], axis=-1)
        tilde_s_t = F.tanh(self.w_c(concatenate))
        y_hat = F.softmax(self.w_y(tilde_s_t), dim=-1)

        return y_hat

x = torch.rand(32, 64, 64)
LoungAttention(64, 32078)(x, x, x).argmax(axis=-1)
