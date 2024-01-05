
Tensorflow
Pytorch 주로 사용

머리속으로 생각하고 돌려보는 스킬 중요

수학적 지식 중요:
선형대수학
통계

딥러닝
가장 중요요소:
  1) Data:
  2) Model: (KNN) AlexNet, Resnet, LSTM, 
  3) Loss function (분류: cross entropy): MSE(Regression), CE(Classification), 
                                         MLE(probabilistic task
                                         노이즈 (아웃라이어 클경우, 제곱X, 절대값으로)
  4) Algorithms : SGD, Adam optimization, R adam
     네트워크를 어떻게 줄일지 (SGD 잘 동작안함, 모멘텀 등)
     ex) Dropout, Early stopping, k-fold validation, Weight decay
         Batch normalization, MixUp, Ensemble, Baysian Optimization
     - 새로운 연구, 논문을 봤을때 contribution 알수 있음
    

### History
1) 2012 : AlexNet
2) 2013 : DQN (딥마인드: 알파고) 강화학습
3) 2014: Encoder/Decoder : NLP
4) 2014: Adam Optimizer : 그냥 사용*(성능이 좋음) - SGD, Momentum있지만
5) 2015: GAN & ResNET: 이미지 생성 **(굉장히 중요)
6) 2015: Residual Network: 중요** 딥러닝의 딥러닝 가능해짐. 20->100단 테스트 성능좋게됨
7) 2017: Transformer ***구글,
8) 2018: BERT (fine-tuned NLP): 굉장히 다양한 단어(위키피디아 등) 활용 pre-train, -> 내 network에 적용
9) 2019: LLM (OpenAI): 1750억개 파라메터,
10) 2020: Self-supervised learning (SimCLR): 이미지 분류, 한정된 학습 데이터 (Label 모르는 Unsupervised learning을 하겠다. 구글의 여러데이터를, 이미지->벡터화 할지)


### Neural Networks
Multi-layer Perceptron
Back propagation(역전파)는 사람의 뇌에 없음 (굳이 뇌를 모방했다라고 하긴 어려움)

Linear NN
y= Wx+b (W,b 어떻게 찾나? loss 최저가되는)
back propagation: 파라메터가 어느방향으로?? 미분하여 반대 방향으로 가게되면
Gradient decent

![Image 2024-01-04 at 5 24 PM](https://github.com/scottmsoh/ref_deep_leraning/assets/112598791/08cbf9bd-280c-45a1-a1ec-bac370ddad7d)

적절한 'stepsize'가 중요함: odaptive learning-rate가 자동으로 조정해줌

Stack more?
Non-linear -> linear -> Non 반복
![Image 2024-01-04 at 5 36 PM](https://github.com/scottmsoh/ref_deep_leraning/assets/112598791/3e9c89a0-dbfe-4c7a-ba91-593497ff93a7)

Activation functions:
ReLu, Sigmoid, Hyperbolic Tangent (Non-linear function이 들어가야 layer를 깊게 쌓았을떄
의미가 있게된다, 더 outperform하게됨)

![Image 2024-01-04 at 5 36 PM](https://github.com/scottmsoh/ref_deep_leraning/assets/112598791/c0f81cd8-994f-4e1e-ad21-ab40f43d5f82)

Universal approximate 
hidden layer가 하나있더라도 뉴럴네트워크가 다양한 표현력을 가지고 있다.

#### Multi-layer perceptron


#### Loss function
MSE - square : 도움이 안될수 있음
MAE - absolute value (outlier가 잇을때는 더 유리)
MARE - 
CE - 높기만 하면됨 (다른 값대비 그 값만):
MLE - ? 잘모르겠음
















    
  
