
## Attention 

Paper: https://courses.grainger.illinois.edu/cs546/sp2018/Slides/Mar15_Luong.pdf

## Introduction
- The limitation of Seq2seq: Original Seq2seq concepts was hard to represent the entire data using one context-vector at the encoding phase.
- Especially when long sequence length (Corpus) will occur the significant problems.

## Contribution: Not utilizing fixed-length vetor encoding method


## Model
- Bidirectional RNN structure
- Calculate each context vector Ci's probability


Original decoder: C(context vector is fixed)
$$ p(\textbf{y}) = \Pi_{t=1}^Tp(y_t|\{y_1, ..., y_{t-1}\}, c) \tag{1} $$
where $ \textbf{y} = (y_1, ..., y_{T_y}) $ 


<span style="font-size:18pt;"> Attention </span>

<span style="font-size:16pt;"> Loung Attention </span>

![](https://wikidocs.net/images/page/22893/dotproductattention1_final.PNG)

[Overall structure of attnetion]
