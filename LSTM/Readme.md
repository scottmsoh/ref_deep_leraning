

## LSTM (Long Short Term Memory)

https://deeplearning.cs.cmu.edu/F23/document/readings/LSTM.pdf</br>

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*tEN1Ziu4VvRAaH9zagN3EQ.png" width="600" height="300"/>

<br>
<br>

A cell introduced to address the limitations of RNNs. <br>
Utilizes gates such as input gate, forget gate, and output gate to update information. <br>

<br>
<br>

### Structure

#### Forget Gate
<img src="https://wikidocs.net/images/page/160053/10_LSTM3-focus-f.png" width="600" height="300"/>

Determines which information to discard from the cell state. <br>
Uses a Sigmoid function, where a value of 0 means removal, 1 means retention, and intermediate values mean partial retention by that proportion. <br>

<br>

#### Input Gate
<img src="https://wikidocs.net/images/page/160053/11_LSTM3-focus-i.png" width="600" height="300"/>

Updates the cell state from $C_{t-1}$ to the new cell state $C_t$. <br>
Adds information from $i_t*\tilde{C_t}$. <br>
&nbsp;&nbsp;&nbsp;&nbsp; $i_t$: Determines how much of $x_t$ to update. <br>
&nbsp;&nbsp;&nbsp;&nbsp; $\tilde{C_t}$: Scales the input value $x_t$ to the range -1 to 1. <br>

<br>

#### Output Gate
<img src="https://wikidocs.net/images/page/160053/13_LSTM3-focus-o.png" width="600" height="300"/>

Determines how much of the cell state $C_t$ to output. <br>
$o_t$: Determines how much of $C_t$ to output based on the input. <br>
$tanh(C_t)$: Scales $C_t$ to the range -1 to 1. <br>

<br>
<br>

### Advantages

1. Overcomes some of the learning instability issues in RNNs (vanishing and exploding gradients).
2. Captures long-term dependencies better than RNNs.

<br>

### Disadvantages

1. Does not completely solve the problem.

### Usage

```python
import torch.nn as nn

lstm = nn.LSTM(
   input_size,
   hidden_size,
   num_layers=,
   bidirectional=False,
   batch_first=True,
)
output, (h_n, c_n) = lstm(x)      # Without providing initial hidden state
output, (h_n, c_n) = lstm(x, h_0) # With providing initial hidden state

# x: input tensor (batch, seq_len, n_feature)
# output: output layer for each t
# h_n: final hidden state
# c_n: final cell state
```

<br>

#### Key Parameters
- `input_size` (int): The size of the input tensor (number of features).
- `hidden_size` (int): The number of neurons in the hidden state.
- `num_layers` (int): The number of stacked layers.
- `bidirectional` (bool): Whether to use a bidirectional LSTM.
- `batch_first` (bool): Whether to place the batch dimension first in the shape.
    - True: (batch, seq_len, n_feature)
    - False: (seq_len, batch, n_feature)

## Variants

There are various modifications of the LSTM structure. <br>
Although their performance is similar, certain variants are more suited to specific tasks.

### Peephole

<img src="https://wikidocs.net/images/page/160053/14_LSTM3-var-peepholes.png" width="600" height="300"/>

### Combined Forget and Input Gate

<img src="https://wikidocs.net/images/page/160053/15_LSTM3-var-tied.png" width="600" height="300"/>

