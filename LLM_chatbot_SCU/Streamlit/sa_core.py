import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import requests
from bs4 import BeautifulSoup
import spacy
import gc

# GPU check
print(f"GPU available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")

# model load
model = AutoModelForSequenceClassification.from_pretrained(
    "Rabbit-123/fine_tuned_roberta_model",
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
tokenizer = AutoTokenizer.from_pretrained("Rabbit-123/fine_tuned_roberta_tokenizer")

label_mapping = {
    'LABEL_0': 'Negative',
    'LABEL_1': 'Neutral',
    'LABEL_2': 'Positive',
    'negative': 'Negative',
    'neutral': 'Neutral',
    'positive': 'Positive'
}

sentiment_analyzer = pipeline(
    'sentiment-analysis', 
    model=model, 
    tokenizer=tokenizer,
    device_map="auto"
)

nlp = spacy.load('en_core_web_sm')

summarizer = pipeline('summarization')

def get_stopwords():
    return set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "%", "that"])

def extract_text_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join([para.get_text() for para in paragraphs])
            return text.strip()
        else:
            return None
    except Exception as e:
        return None

def summarize_text(text):
    try:
        max_chunk_length = 400
        min_summary_length = 50
        max_summary_length = 150  

        if len(text.split()) < min_summary_length:
            return text

        chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

        summarized_chunks = []
        for chunk in chunks:
            if len(chunk.strip()) < min_summary_length:
                continue
                
            with torch.cuda.amp.autocast() if torch.cuda.is_available() else nullcontext():
                try:
                    summary = summarizer(
                        chunk,
                        max_length=max_summary_length,
                        min_length=min_summary_length,
                        do_sample=False,
                        truncation=True
                    )
                    summarized_chunks.append(summary[0]['summary_text'])
                except Exception as e:
                    print(f"Chunk summarization error: {str(e)}")
                    continue

        
        if not summarized_chunks:
            return text

        combined_summary = ' '.join(summarized_chunks)

        # if it is too long, return again
        if len(combined_summary.split()) > max_summary_length:
            try:
                with torch.cuda.amp.autocast() if torch.cuda.is_available() else nullcontext():
                    final_summary = summarizer(
                        combined_summary,
                        max_length=max_summary_length,
                        min_length=min_summary_length,
                        do_sample=False,
                        truncation=True
                    )[0]['summary_text']
                return final_summary
            except Exception as e:
                print(f"Final summarization error: {str(e)}")
                return combined_summary
        
        return combined_summary

    except Exception as e:
        print(f"Summarization error: {str(e)}")
        return text

def sentiment_analysis(input_text):
    try:
        max_length = 512
        tokens = tokenizer(
            input_text, 
            return_tensors='pt',
            truncation=False,
            padding=False
        )
        
        input_ids = tokens['input_ids'][0]
        num_chunks = (len(input_ids) + max_length - 1) // max_length
        chunks = [input_ids[i * max_length:(i + 1) * max_length] for i in range(num_chunks)]

        sentiments = []
        scores = []
        sentiment_scores = []
        
        for chunk in chunks:
            with torch.cuda.amp.autocast() if torch.cuda.is_available() else nullcontext():
                chunk_text = tokenizer.decode(chunk, skip_special_tokens=True)
                predictions = sentiment_analyzer(
                    chunk_text,
                    truncation=True,
                    padding=True,
                    max_length=512
                )
                sentiment_label = label_mapping[predictions[0]['label'].lower()]
                score = predictions[0]['score']
                sentiments.append(sentiment_label)
                scores.append(score)
                
                if sentiment_label == 'Positive':
                    sentiment_scores.append(score)
                elif sentiment_label == 'Negative':
                    sentiment_scores.append(-score)
                else:
                    sentiment_scores.append(0)
        
        overall_sentiment = max(set(sentiments), key=sentiments.count)
        average_score = sum(scores) / len(scores)
        sentiment_label_score = sum(sentiment_scores) / len(sentiment_scores)
        
        return overall_sentiment, average_score, sentiment_label_score

    except Exception as e:
        print(f"Sentiment analysis error: {str(e)}")
        return "Neutral", 0.0, 0.0

def analyze_url(url):
    text = extract_text_from_url(url)
    if text:
        summary = summarize_text(text)
        return summary
    else:
        return None

# GPU memory clear
def clear_gpu_memory():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        gc.collect()

# nullcontext add
from contextlib import nullcontext