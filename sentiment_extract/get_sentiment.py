import pandas as pd
import numpy as np

def parse_sentiment():
    # df = pd.read_csv('soc-redditHyperlinks-title.tsv', sep='\t')

    # properties_df = df['PROPERTIES'].str.split(',', expand=True)

    # # These are already calculated sentiment values with VADER
    # vader_sentiments = properties_df.iloc[:, 18:21]
    # vader_sentiments.columns = ['Positive Sentiment', 'Negative Sentiment', 'Compound Sentiment']

    # # New table showing only sentiment data
    # result_df = df[['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', 'POST_ID', 'TIMESTAMP']].copy()

    # # Add the selected sentiment columns to the new DataFrame
    # result_df = pd.concat([result_df, vader_sentiments], axis=1)

    # # Display the resulting DataFrame
    # print(result_df.head())

    # print(result_df['SOURCE_SUBREDDIT'].nunique())

    print("Hello")
if __name__ == '__main__':
    parse_sentiment()