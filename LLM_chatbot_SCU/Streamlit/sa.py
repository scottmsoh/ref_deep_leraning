import streamlit as st
from collections import Counter
from urllib.parse import urlparse
from sa_core import extract_text_from_url, sentiment_analysis, nlp, sentiment_analyzer, label_mapping, get_stopwords, analyze_url
import json
import plotly.graph_objects as go
import requests

analysis_history = []

def generate_word_importance_chart(input_text, sentiment, nlp, sentiment_analyzer, label_mapping, get_stopwords):
    doc = nlp(input_text)
    stopwords = get_stopwords()
    words = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PRON'] and token.text.lower() not in stopwords]
    word_counts = Counter(words)

    word_scores = {}
    matching_words = []
    other_words = []

    # Separate words by sentiment
    for word, count in word_counts.items():
        word_sentiment = sentiment_analyzer(word)[0]
        sentiment_label = label_mapping[word_sentiment['label'].lower()]
        score = word_sentiment['score']

        if (sentiment == 'Positive' and sentiment_label == 'positive') or \
           (sentiment == 'Negative' and sentiment_label == 'negative') or \
           (sentiment == 'Neutral' and sentiment_label == 'neutral'):
            word_scores[word] = score * count
            matching_words.append((word, score, count))
        else:
            other_words.append((word, score, count))

    top_matching_words = sorted(matching_words, key=lambda x: abs(x[1]), reverse=True)[:10]

    if len(top_matching_words) < 10:
        needed_words = 10 - len(top_matching_words)
        top_other_words = sorted(other_words, key=lambda x: abs(x[1]), reverse=True)[:needed_words]
        top_matching_words.extend(top_other_words)

    top_words = top_matching_words
    words, scores, frequencies = zip(*top_words) if top_words else ([], [], [])
    bubble_sizes = [freq * 5 for freq in frequencies]
    colors = ['red' if sentiment == 'Positive' else 'blue' if sentiment == 'Negative' else 'yellow' for _ in scores]

    # Create a Plotly figure
    fig = go.Figure(data=[go.Scatter(
        x=words,
        y=frequencies,
        mode='markers',
        marker=dict(size=bubble_sizes, color=colors, opacity=0.6, line=dict(width=1.5, color='black')),
        showlegend=False
    )])
    fig.update_layout(
        title='Sentiment Chart of Top 10 Nouns and Pronouns Reflecting Sentiment',
        xaxis_title='Words (Nouns and Pronouns)',
        yaxis_title='Frequency',
        xaxis_tickangle=-45,
        showlegend=True,
        legend=dict(
            title='Sentiment Legend',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        legend_tracegroupgap=15
    )
    # Adding manual legend items for Positive, Negative, and Neutral
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Positive'
    ))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='Negative'
    ))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='yellow'),
        name='Neutral'
    ))
    st.plotly_chart(fig)

    return [{"x": words, "y": frequencies, "mode": "markers", "marker": {"size": bubble_sizes, "color": colors}}]

def add_to_history(input_type, user_input, sentiment, confidence, sentiment_label_score, sentiment_intensity, extracted_text, graph_data, summary=None):
    history_entry = {
        "Input Type": input_type,
        "Input": user_input,
        "Sentiment": sentiment,
        "Confidence Score": confidence,
        "Sentiment Label Score": sentiment_label_score,
        "Sentiment Intensity": sentiment_intensity,
        "Extracted Text": extracted_text,
        "Graph Data": graph_data
    }
    
    if input_type == 'URL' and summary is not None:
        history_entry["Summary"] = summary

    analysis_history.append(history_entry)
    
    with open('analysis_history.json', 'w') as history_file:
        json.dump(analysis_history, history_file)

def recreate_graph(graph_data):
    # Create a new Plotly figure using stored graph data
    fig = go.Figure()
    for trace in graph_data:
        fig.add_trace(go.Scatter(**trace, showlegend=False))
    fig.update_layout(
        title='Sentiment Chart of Top 10 Nouns and Pronouns Reflecting Sentiment',
        xaxis_title='Words (Nouns and Pronouns)',
        yaxis_title='Frequency',
        xaxis_tickangle=-45,
        legend=dict(
            title='Sentiment Legend',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        legend_tracegroupgap=15
    )
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Positive'
    ))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='Negative'
    ))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='yellow'),
        name='Neutral'
    ))
    return fig

def sentiment_analysis_page():
    if st.button("⬅️ Back to Main", key="sentiment_back_to_main"):
        st.session_state.page = "main"
    
    # Load analysis history from file
    try:
        with open('analysis_history.json', 'r') as history_file:
            global analysis_history
            analysis_history = json.load(history_file)
    except FileNotFoundError:
        analysis_history = []

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<div id='sidebar'>", unsafe_allow_html=True)
        st.markdown("<div id='history-title'><h3>History</h3></div>", unsafe_allow_html=True)
        st.markdown("<div id='history-item-container'>", unsafe_allow_html=True)
        for idx, entry in enumerate(analysis_history):
            if st.button(f"Analysis {idx + 1}", key=f"history_{idx}"):
                st.session_state["current_analysis"] = entry
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("Return to Analysis Page"):
            st.session_state.pop("current_analysis", None)

    # Main Content: Analysis Interface
    with col2:
        st.title("Sentiment Analysis for Financial News")
        st.markdown("<div id='prompt-box'>Enter text or a URL for sentiment analysis. Examples: 'The market is bullish today' or 'https://example.com/news'</div>", unsafe_allow_html=True)

        if "current_analysis" in st.session_state:
            entry = st.session_state["current_analysis"]
            st.write(f"**Input Type**: {entry['Input Type']}")
            st.write(f"**Input**: {entry['Input']}")
            if entry['Input Type'] == 'URL' and 'Summary' in entry:
                st.write(f"**Summary for URL**: {entry['Summary']}")
            st.write(f"**Sentiment**: {entry['Sentiment']}")
            st.write(f"**Confidence Score**: {entry['Confidence Score']:.2f}")
            st.write(f"**Sentiment Label Score**: {entry['Sentiment Label Score']:.2f}")
            st.write(f"**Sentiment Intensity**: {entry['Sentiment Intensity']}")
            st.write("---")
            if "Graph Data" in entry:
                fig = recreate_graph(entry["Graph Data"])
                st.plotly_chart(fig)

        else:
            input_type = st.radio("Select input type:", ('Text', 'URL'))
            user_input = ""
            if input_type == 'Text':
                user_input = st.text_area("Enter your text here:")
            elif input_type == 'URL':
                user_input = st.text_input("Enter the URL here:")

            if st.button("Analyze Sentiment"):
                if user_input.strip():
                    extracted_text = ""
                    if input_type == 'URL':
                        parsed_url = urlparse(user_input.strip())
                        if parsed_url.scheme in ['http', 'https']:
                            extracted_text = extract_text_from_url(user_input.strip())
                            if extracted_text:
                                sentiment, confidence, sentiment_label_score = sentiment_analysis(extracted_text)
                                summary = analyze_url(user_input.strip())
                                sentiment_intensity = "Negative" if sentiment_label_score < -0.5 else "Positive" if sentiment_label_score > 0.5 else "Neutral"
                                st.write(f"**URL:** {user_input.strip()}")
                                st.write(f"**Summary for url:** {summary}")
                                st.write(f"**Sentiment:** {sentiment}")
                                st.write(f"**Confidence Score:** {confidence:.2f}")
                                st.write(f"**Sentiment Label Score:** {sentiment_label_score:.2f} ({sentiment_intensity})")
                                graph_data = generate_word_importance_chart(extracted_text, sentiment, nlp, sentiment_analyzer, label_mapping, get_stopwords)
                                add_to_history(input_type, user_input, sentiment, confidence, sentiment_label_score, sentiment_intensity, extracted_text, graph_data, summary)
                            else:
                                st.warning("Failed to extract content from the URL.")
                        else:
                            st.warning("Please enter a valid URL starting with http or https.")
                    else:
                        sentiment, confidence, sentiment_label_score = sentiment_analysis(user_input.strip())
                        sentiment_intensity = "Negative" if sentiment_label_score < -0.5 else "Positive" if sentiment_label_score > 0.5 else "Neutral"
                        st.write(f"**Input:** {user_input.strip()}")
                        st.write(f"**Sentiment:** {sentiment}")
                        st.write(f"**Confidence Score:** {confidence:.2f}")
                        st.write(f"**Sentiment Label Score:** {sentiment_label_score:.2f} ({sentiment_intensity})")
                        graph_data = generate_word_importance_chart(user_input.strip(), sentiment, nlp, sentiment_analyzer, label_mapping, get_stopwords)
                        add_to_history(input_type, user_input, sentiment, confidence, sentiment_label_score, sentiment_intensity, user_input.strip(), graph_data)
                else:
                    st.warning("Please enter some text or a URL.")

if __name__ == "__main__":
    sentiment_analysis_page()