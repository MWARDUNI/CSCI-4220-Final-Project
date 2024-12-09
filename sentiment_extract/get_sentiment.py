import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

import nltk
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import re

# Download VADER lexicon
nltk.download('vader_lexicon')

# reddit API key
reddit = praw.Reddit(
    client_id='BaVi2Bz4ZW3BPGc0M5gusw',         
    client_secret='OOcK08XZB7Mf-m16IWtnb7z8ZJlz9Q', 
    user_agent='sentiment-analysis'        
)

sia = SentimentIntensityAnalyzer()


def import_title_data():
    # Import the intitial data

    script_dir_title = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the absolute path to the TSV file
    file_path_title = os.path.join(script_dir_title, '..', 'soc-redditHyperlinks-title.tsv')
    
    # Normalize the path to handle any redundant separators
    file_path_title = os.path.normpath(file_path_title)

    df = pd.read_csv(file_path_title, sep='\t')

    properties_df = df['PROPERTIES'].str.split(',', expand=True)

    # These are already calculated sentiment values with VADER
    vader_sentiments = properties_df.iloc[:, 18:21]
    vader_sentiments.columns = ['Positive Sentiment', 'Negative Sentiment', 'Compound Sentiment']

    # New table showing only sentiment data
    result_df = df[['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', 'POST_ID', 'TIMESTAMP']].copy()

    # Add the selected sentiment columns to the new df
    result_df = pd.concat([result_df, vader_sentiments], axis=1)

    return result_df

def import_body_data():
    # Import the intitial data

    script_dir_body = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the absolute path to the TSV file
    file_path_body = os.path.join(script_dir_body, '..', 'soc-redditHyperlinks-title.tsv')
    
    # Normalize the path to handle any redundant separators
    file_path_body = os.path.normpath(file_path_body)

    df_body = pd.read_csv(file_path_body, sep='\t')

    properties_df_body = df_body['PROPERTIES'].str.split(',', expand=True)

    # These are already calculated sentiment values with VADER
    vader_sentiments_body = properties_df_body.iloc[:, 18:21]
    vader_sentiments_body.columns = ['Positive Sentiment', 'Negative Sentiment', 'Compound Sentiment']

    # New table showing only sentiment data
    result_df_body = df_body[['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', 'POST_ID', 'TIMESTAMP']].copy()

    # Add the selected sentiment columns to the new df
    result_df_body = pd.concat([result_df_body, vader_sentiments_body], axis=1)

    return result_df_body

def build_model(df):
    # Split data into x,y (80/20 split)
    X_var = df[['SOURCE_SUBREDDIT_ENCODED', 'Positive Sentiment', 'Negative Sentiment']]
    y_var = df['Compound Sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size=0.2, random_state=42)

    # Create the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    return model, X_train, y_train, X_test, y_test

def make_title_model():
    # Copy the processed title data
    title_df = result_df.copy()

    # Top 50 SOURCE/TARGET_SUBREDDITs by count
    top_subreddits_title_source = title_df['SOURCE_SUBREDDIT'].value_counts().head(50)
    top_subreddits_title_target = title_df['TARGET_SUBREDDIT'].value_counts().head(50)

    # Encode data in order to put into model
    label_encoder_title = LabelEncoder()
    title_df['SOURCE_SUBREDDIT_ENCODED'] = label_encoder_title.fit_transform(title_df['SOURCE_SUBREDDIT'])

    # After model is returned, train the model.
    model_title, X_train_title, y_train_title, X_test_title, y_test_title = build_model(title_df)
    model_title.fit(X_train_title, y_train_title)   

    # Prediction and results for verification
    y_pred_title = model_title.predict(X_test_title)

    mse_title = mean_squared_error(y_test_title, y_pred_title)
    r2_title = r2_score(y_test_title, y_pred_title)

    return model_title, label_encoder_title, top_subreddits_title_source, top_subreddits_title_target

def make_body_model():
    # Copy the processed body data
    body_df = result_df_body.copy()

    # Top 50 SOURCE/TARGET_SUBREDDITs by count
    top_subreddits_body_source = body_df['SOURCE_SUBREDDIT'].value_counts().head(50)
    top_subreddits_body_target = body_df['TARGET_SUBREDDIT'].value_counts().head(50)

    # Encode data in order to put into model
    label_encoder_body = LabelEncoder()
    body_df['SOURCE_SUBREDDIT_ENCODED'] = label_encoder_body.fit_transform(body_df['SOURCE_SUBREDDIT'])

    # After model is returned, train the model.
    model_body, X_train_body, y_train_body, X_test_body, y_test_body = build_model(body_df)
    model_body.fit(X_train_body, y_train_body)  
    
    # Prediction and results for verification
    y_pred_body = model_body.predict(X_test_body)

    mse_body = mean_squared_error(y_test_body, y_pred_body)
    r2_body = r2_score(y_test_body, y_pred_body)

    return model_body, label_encoder_body, top_subreddits_body_source, top_subreddits_body_target

def choose_subreddit(subreddit_name):
    # Pass subreddit from input
    # subreddit_name_test = 'AITAH'  # only for testing
    subreddit = reddit.subreddit(subreddit_name)

    # Fetch the top 100 posts
    posts = []
    for post in subreddit.hot(limit=100):
        posts.append({
            'title': post.title,
            'body': post.selftext
        })

    # Create df of posts
    chosen_subreddit_df = pd.DataFrame(posts)

    # Apply preprocessing
    chosen_subreddit_df['clean_title'] = chosen_subreddit_df['title'].apply(preprocess_text)
    chosen_subreddit_df['clean_body'] = chosen_subreddit_df['body'].apply(preprocess_text)

    # Adding columns and appling VADERs sentiment anaylsis to those inputs

    chosen_subreddit_df['title_positive'] = chosen_subreddit_df['clean_title'].apply(lambda x: sia.polarity_scores(x)['pos'])
    chosen_subreddit_df['title_negative'] = chosen_subreddit_df['clean_title'].apply(lambda x: sia.polarity_scores(x)['neg'])
    chosen_subreddit_df['title_compound'] = chosen_subreddit_df['clean_title'].apply(lambda x: sia.polarity_scores(x)['compound'])
    
    chosen_subreddit_df['body_positive'] = chosen_subreddit_df['body'].apply(lambda x: sia.polarity_scores(x)['pos'])
    chosen_subreddit_df['body_negative'] = chosen_subreddit_df['body'].apply(lambda x: sia.polarity_scores(x)['neg'])
    chosen_subreddit_df['body_compound'] = chosen_subreddit_df['body'].apply(lambda x: sia.polarity_scores(x)['compound'])


    return chosen_subreddit_df

def subreddit_avg_sentiment(df):
    # Taking the averages sentiment
    average_title_positive = df['body_positive'].mean()
    average_title_negative = df['body_negative'].mean()
    average_title_compound = df['body_compound'].mean()

    average_body_positive = df['body_positive'].mean()
    average_body_negative = df['body_negative'].mean()
    average_body_compound = df['body_compound'].mean()

    # Compile all averages into a dictionary from most 100 recent posts in chosen subreddit 
    averages = (
       f"=== Average Sentiment Scores for the Past 100 Posts ===\n"
        f"--- Titles ---\n"
        f"Positive: {average_title_positive:.4f}\n"
        f"Negative: {average_title_negative:.4f}\n"
        f"Compound: {average_title_compound:.4f}\n\n"
        f"--- Bodies ---\n"
        f"Positive: {average_body_positive:.4f}\n"
        f"Negative: {average_body_negative:.4f}\n"
        f"Compound: {average_body_compound:.4f}\n\n"

        f"Key:\n"
        f"Positive (0.0-1.0, higher is more positive)\n"
        f"Negative (0.0-1.0, higher is more negative)\n"
        f"Compound (-1.0 to 1.0, -1 is most negative, 1 is most positive).\n\n"
    )

    return averages

def title_sentiment(scores, df):
    # Average sentiment from the title_df in order to see average throughout all subreddits for titles 
    title_positive = df['Positive Sentiment'].apply(pd.to_numeric, errors='coerce').mean()
    title_negative = df['Negative Sentiment'].apply(pd.to_numeric, errors='coerce').mean()
    title_compound = df['Compound Sentiment'].apply(pd.to_numeric, errors='coerce').mean()

    title_scores = (
        f"=== Average Sentiment Scores for titles in subreddits ===\n"
        f"Positive: {title_positive:.4f}\n"
        f"Negative: {title_negative:.4f}\n"
        f"Compound: {title_compound:.4f}\n\n"

        f"=== Sentiment Scores for input title ===\n"
        f"Positive: {scores['pos']}\n"
        f"Negative: {scores['neg']}\n"
        f"Compound: {scores['compound']}\n\n"

        f"Key:\n"
        f"Positive (0.0-1.0, higher is more positive)\n"
        f"Negative (0.0-1.0, higher is more negative)\n"
        f"Compound (-1.0 to 1.0, -1 is most negative, 1 is most positive).\n\n"
    )

    return title_scores

def body_sentiment(scores, df):
    # Average sentiment from the title_df in order to see average throughout all subreddits for body(posts) 
    body_positive = df['Positive Sentiment'].apply(pd.to_numeric, errors='coerce').mean()
    body_negative = df['Negative Sentiment'].apply(pd.to_numeric, errors='coerce').mean()
    body_compound = df['Compound Sentiment'].apply(pd.to_numeric, errors='coerce').mean()

    body_scores = (
        f"=== Average Sentiment Scores for body(message) in subreddits ===\n"
        f"Positive: {body_positive:.4f}\n"
        f"Negative: {body_negative:.4f}\n"
        f"Compound: {body_compound:.4f}\n\n"

        f"=== Sentiment Scores for input body(message) ===\n"
        f"Positive: {scores['pos']}\n"
        f"Negative: {scores['neg']}\n"
        f"Compound: {scores['compound']}\n\n"

        f"Key:\n"
        f"Positive (0.0-1.0, higher is more positive)\n"
        f"Negative (0.0-1.0, higher is more negative)\n"
        f"Compound (-1.0 to 1.0, -1 is most negative, 1 is most positive).\n\n"
    )

    return body_scores

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove URLs, mentions, special characters, numbers and extra white spaces
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def main(selection= None, value=None):
            value = preprocess_text(value)

            if selection == 4:
                return "Exit"

            match selection:
                case 1: 
                    subreddit_df = choose_subreddit(value)
                    averages = subreddit_avg_sentiment(subreddit_df)
                    return averages
                
                case 2: 
                    title_scores = sia.polarity_scores(value)
                    title_averages = title_sentiment(title_scores, result_df)
                    return title_averages

                case 3:
                    body_scores = sia.polarity_scores(value)
                    body_averages = body_sentiment(body_scores, result_df_body)
                    return body_averages

result_df = import_title_data()
result_df_body = import_body_data()
model_title, label_encoder_title, top_subreddits_title_source, top_subreddits_title_target = make_title_model()
model_body, label_encoder_body, top_subreddits_body_source, top_subreddits_body_target = make_body_model()

if __name__ == '__main__':
    main()