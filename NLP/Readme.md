
* Tokenization</br>

1) word tokenize: NLTK word_tokenize, WordPunctTokenizer,TreebankWordTokenizer(Standard) Keras text_to_word_sequence</br>
2) sentence tokenize: NLTK sent_tokenize</br>
3) Part-of-speech tagging: NLTK pos_tag</br>
4) Morpheme tokenize (For Korean): Konlpy Okt, Mecab, Komoran, Hannanum, Kkma</br>
 
* Cleaning </br>

1) Integration of words with different notation based on rules</br>
2) Integration of upper and lower case letters</br>
3) Removal of unnecessary words (words that appear less frequently,</br> 
   words of shorter length)</br>
4) Regular expression</br>

* Normalization (To reduce the size of corpors

1) Lemmatization: Lemma(표제어) 찾는 과정, ex) am,are,is = be, cats,cat = cat (cat어간+s접사)</br>
                  형태학적 파싱, 형태소(의미를 가진 가장 작은 단위) = Stem(핵심) + Affix(추가의미)</br>
                  ex) NLTK WordNetLemmatizer</br>
3) Stemming 어간 추출: Stem (어간), </br>
                    ex) Lancaster & Porter algorithms</br>
4) Korean stemming</br>
