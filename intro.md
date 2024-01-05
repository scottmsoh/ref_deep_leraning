
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
    

## History
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







    
  
