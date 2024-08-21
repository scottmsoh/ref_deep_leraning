
## Sequence-to-Sequence (Seq2seq)

paper: https://arxiv.org/pdf/1409.3215</br>


## Introduction

Limitations of traditional models: they are only applicable to problems that can be encoded as fixed-dimensional vectors for both input and output. <br>
→ Sequence problems such as speech recognition, machine translation, and question answering require a domain-independent method that can map sequences to sequences. <br>

### Contribution:
This work proposes a method to solve sequence-to-sequence problems based on LSTM:
- Uses LSTM to encode the input sequence and convert it into a fixed-dimensional vector.
- Generates the output sequence through another LSTM (decoder).

## Model

LSTM generates the conditional probability $p(y_1, ..., y_{T'}|x_1, ..., x_T)$ when $(x_1, ..., x_T)$ is input. <br>
$y_1, ..., y_{T'}$ is the output sequence, which may have a length $T'$ different from the input length $T$. <br>
The LSTM uses a fixed vector representation $v$ as the final hidden state of the input sequence $(x_1, ..., x_T)$. <br>
This $v$ is set as the initial hidden state of the decoder to compute the probability of $y_1, ..., y_{T'}$.

$$
p(y_1, ..., y_{T'}|x_1, ..., x_T) = \Pi_{t=1}^{T'} p(y_t|v, y_1, ..., y_{t-1})
$$

In the equation above, each $p(y_t|v, y_1, ..., y_{t-1})$ distribution is represented as a softmax over the entire vocabulary. <br>
Each sequence ends with a special symbol \<EOS\>, which allows defining distributions over sentences of varying lengths. <br>
For example, in the figure above, the encoder input is 'A', 'B', 'C', '\<EOS\>', and the decoder input is 'W', 'X', 'W', 'Y', 'Z', '\<EOS\>'.

## Model Implementation

1. Two separate LSTMs are used:
    - One LSTM for the input sequence.
    - One LSTM for the output sequence. <br>
    → This slightly increases computational cost. <br>
    → Allows simultaneous training on different language pairs naturally.
2. Deep LSTMs perform significantly better than shallow LSTMs.
    - The paper uses 4 layers.
3. Reversing the input sequence leads to substantial performance improvements. <br>
    → Mapping c, b, a to $\alpha, \beta, \gamma$ is significantly more effective than mapping a, b, c to $\alpha, \beta, \gamma$ (where a-$\alpha$, b-$\beta$, c-$\gamma$ are translation pairs). <br>
    → This method helps to ensure that a aligns closely with $\alpha$, b with $\beta$, and c with $\gamma$. <br>
    → Stochastic Gradient Descent (SGD) makes it easier to establish communication between input and output.

## Experiments

### 1. Dataset Details

Used the 160k most frequent terms in the source language and the 80k most frequent terms in the target language. <br>
Out-of-vocabulary words were replaced with the "UNK" token.

### 2. Decoding and Rescoring

Given that we had to train very deep LSTMs on many sentence pairs, the model was trained to maximize the log probability of the correct translation for a given source sentence:

$$
1/|S| \Sigma_{(T,S) \in S} \log p(T|S)
$$

where $S$ is the training set.

After training, the model generates the most probable translation by maximizing:

$$
\hat{T} = \arg \max_{T} p(T|S)
$$

We use a simple left-to-right beam search decoder to find the most probable translation, maintaining a small number \(B\) of partial hypotheses, where a partial hypothesis is a prefix of some translation.

- **Partial hypothesis**: A portion of the translation generated so far.
- **Beam size (B)**: The number of partial hypotheses to retain. Larger values allow for more candidates.
- **Left-to-right decoder**: Generates the translation from left to right.

### Example:

- **Input sequence**: "I am happy"
- **Target language**: Korean
- **B**: 2

1. **Initial Status**: The decoder starts with an empty sentence.
2. **Step 1**: Generates possible first words (e.g., 나는, 저는).
3. **Step 2**: Expands each partial hypothesis to generate the next word.

The process continues, expanding the hypotheses and selecting the top candidates based on their probabilities. Beam search eventually selects the most likely translation.

### 3. Reversing the Source Sentences

The authors hypothesize that the performance improvements are due to the introduction of short-term dependencies in the dataset. <br>
When connecting the source and target sentences, each word in the source is far from its corresponding word in the target. This creates a "minimal time lag" problem.

By reversing the source sentence, the average distance between the source and target words remains unchanged, but the first few words in the source now correspond more closely to the first few words in the target, significantly reducing the minimal time lag. This allows for easier communication between source and target, resulting in a notable performance improvement.

> **Large Minimal Time Lag**: A large temporal gap between the input and output sequences.
