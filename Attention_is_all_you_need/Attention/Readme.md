
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

attention score는 위의 내적 연산을 통해 얻어지며 결과는 모두 scalar <br>
이 경우 $ score(s_t, h_i) = s_t^Th_i $ <br>
$s_t$와 인코더 전체의 hidden state의 attention score의 모음을 $e_t$라고 정의하며 <br>
$ e^t = [s^T_th_1, ... , s_t^Th_N] $

<br>

<span style="font-size:14pt;"> Step2 </span>

![](https://wikidocs.net/images/page/22893/dotproductattention3_final.PNG)

$e^t$에 softmax를 적용하여 확률분포 계산 -> attention distribution <br>
디코더의 t시점에서 attnetion distribution: $\alpha^t = softmax(e^t)$ 

<br>

<span style="font-size:14pt;"> Step3 </span>

![](https://wikidocs.net/images/page/22893/dotproductattention4_final.PNG)

인코더의 각 hidden state와 attention 가중치를 곱한 후 더함 (가중합)

$ a_t = \Sigma^N_{i=1} \alpha_i^t h_i $

$a_t$: contect vector

<br>

<span style="font-size:14pt;"> Step4 </span>

![](https://wikidocs.net/images/page/22893/dotproductattention5_final_final.PNG)

디코더의 t 시점의 $s_t$와 attention value $a_t$ 벡터 결합 <br>

<br>

<span style="font-size:14pt;"> Step5 </span>

![](https://wikidocs.net/images/page/22893/st.PNG)

결합 벡터와 layer를 연산하여 새로운 벡터 $\tilde{s_t}$ 취득 <br>

$ \tilde{s_t} $ = tanh($ \textbf{W}_c[a_t;s_t] + b_c$)  

<br>

<span style="font-size:14pt;"> Step6 </span>

$\hat{y_t}$ = Softmax($\textbf{W}_y\tilde{s_t} + b_y$)

<br>
<br>


