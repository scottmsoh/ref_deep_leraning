

### GRU (Gated Recurrent Unit)

A variant of RNN that simplifies the three gates used in LSTM. <br>
It updates information using the update gate and reset gate. <br>
In GRU, the cell state and hidden state are combined into the hidden state. <br>

<br>

### Structure

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*-ldMy6GqBy8D25uNKQl2gA.png" width="600" height="300"/>

#### Reset Gate (a)

Determines how much information to forget.

<br>

#### Update Gate (b)

Decides how much information from the previous hidden state should be reflected in the current state. <br>
The closer the value is to 0, the more the information from the previous hidden state is forgotten; the closer it is to 1, the more the current hidden state is retained. <br>
In the diagram, the "-" indicates the amount of information being subtracted, representing the quantity removed.

<br>
<br>

### Advantages

1. Faster learning speed compared to LSTM due to fewer parameters.

<br>

### Disadvantages

1. In some tasks, GRU struggles to maintain long-term dependencies compared to LSTM when handling long sequence data.

### Usage

```python
import torch.nn as nn

gru = nn.GRU(
   input_size,
   hidden_size,
   num_layers=,
   bidirectional=False,
   batch_first=True,
)
output, h_n = gru(x)      # Without providing initial hidden state
output, h_n = gru(x, h_0) # With providing initial hidden state

# x: input tensor (batch, seq_len, n_feature)
# output: output layer for each t
# h_n: final hidden state
```

<br>

#### Key Parameters
- `input_size` (int): The size of the input tensor (number of features).
- `hidden_size` (int): The number of neurons in the hidden state.
- `num_layers` (int): The number of stacked layers.
- `bidirectional` (bool): Whether to use a bidirectional GRU.
- `batch_first` (bool): Whether to place the batch dimension first in the shape.
    - True: (batch, seq_len, n_feature)
    - False: (seq_len, batch, n_feature)

