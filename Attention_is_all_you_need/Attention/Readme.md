
## Attention 

Paper: https://courses.grainger.illinois.edu/cs546/sp2018/Slides/Mar15_Luong.pdf

## Introduction
- The limitation of Seq2seq: Original Seq2seq concepts was hard to represent the entire data using one context-vector at the encoding phase.
- Especially when long sequence length (Corpus) will occur the significant problems.

## Contribution: Not utilizing fixed-length vetor encoding method


## Model
- Bidirectional RNN structure
- Calculate each context vector Ci's probability


p(**y**) = Π<sub>t=1</sub><sup>T</sup>p(y<sub>t</sub>|{y<sub>1</sub>, ..., y<sub>t-1</sub>}, c)


<span style="font-size:18pt;"> Attention </span>

<span style="font-size:16pt;"> Loung Attention </span>

![](https://wikidocs.net/images/page/22893/dotproductattention1_final.PNG)

[Overall structure of attnetion]

<br>

<span style="font-size:14pt;"> Step1 </span>

![](https://wikidocs.net/images/page/22893/dotproductattention2_final.PNG)

decoder의 t시점와 encoder의 전체 hidden state의 내적 연산을 통해 attention score 산출
- decoder의 t시점의 hidden state와 encoder의 각 hidden state가 얼마나 유사한지 판단

<br>

![](https://wikidocs.net/images/page/22893/i%EB%B2%88%EC%A7%B8%EC%96%B4%ED%85%90%EC%85%98%EC%8A%A4%EC%BD%94%EC%96%B4_final.PNG)
