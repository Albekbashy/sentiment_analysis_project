import pandas as pd
import re

def clean_text(text: str) -> str:
    """
    Clean review text:
    - Convert to lowercase
    - Remove URLs
    - Remove emojis, punctuation
    - Remove extra spaces
    """
    if not isinstance(text, str):
        text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.I)

    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Load Google Play reviews, clean text, and map scores to sentiment labels.

    Sentiment mapping:
    - Negative (score 1-2) -> 0
    - Neutral (score 3) -> 1
    - Positive (score 4-5) -> 2
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Check required columns
    required_cols = ['content', 'score']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' missing in CSV")

    # Clean the text column
    df['content'] = df['content'].apply(clean_text)

    # Map scores to sentiment labels
    def to_sentiment(score):
        score = int(score)
        if score <= 2:
            return 0  # negative
        elif score == 3:
            return 1  # neutral
        else:
            return 2  # positive

    df['sentiment'] = df['score'].apply(to_sentiment)

    return df
