import pandas as pd
from typing import Union
from pathlib import Path

def load_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load Google Play reviews dataset and map scores to binary labels.

    Parameters:
        file_path (str or Path): Path to dataset.csv

    Returns:
        pd.DataFrame: Columns ['text', 'label'], label=1 for positive, 0 for negative
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    if 'content' not in df.columns or 'score' not in df.columns:
        raise ValueError("CSV must contain 'content' and 'score' columns")

    df = df.dropna(subset=['content', 'score'])

    def map_label(score):
        try:
            score = float(score)
        except (ValueError, TypeError):
            return None
        if score >= 4:
            return 1
        elif score <= 2:
            return 0
        return None

    df['label'] = df['score'].apply(map_label)
    df = df.dropna(subset=['label'])
    df = df[['content', 'label']].rename(columns={'content':'text'})
    df['label'] = df['label'].astype(int)
    return df.reset_index(drop=True)
