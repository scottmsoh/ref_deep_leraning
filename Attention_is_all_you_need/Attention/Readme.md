
## Attention 

Paper: https://courses.grainger.illinois.edu/cs546/sp2018/Slides/Mar15_Luong.pdf

## Introduction
- The limitation of Seq2seq: Original Seq2seq concepts was hard to represent the entire data using one context-vector at the encoding phase.
- Especially when long sequence length (Corpus) will occur the significant problems.

## Contribution: Not utilizing fixed-length vetor encoding method


## Model
- Bidirectional RNN structure
- Calculate each context vector Ci's probability

```
p(**y**) = Π<sub>t=1</sub><sup>T</sup>p(y<sub>t</sub>|{y<sub>1</sub>, ..., y<sub>t-1</sub>}, c)
```

<span style="font-size:18pt;"> Attention </span>

<span style="font-size:16pt;"> Loung Attention </span>

![](https://wikidocs.net/images/page/22893/dotproductattention1_final.PNG)

[Overall structure of attnetion]
