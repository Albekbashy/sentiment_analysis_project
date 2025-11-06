

import pandas as pd
import pytest
from pathlib import Path

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from data_extraction import load_data  # relative import

REAL_FILE_PATH = Path("data/dataset.csv")  # optional

def test_load_data_real_file():
    out = load_data(REAL_FILE_PATH)
    assert 'text' in out.columns
    assert 'label' in out.columns
    assert set(out['label']).issubset({0, 1})

def test_load_data_tmp_file(tmp_path):
    df = pd.DataFrame({
        'reviewId': ['r1','r2','r3'],
        'content': ['Good app', 'Bad crash', 'It is ok'],
        'score': [5, 1, 3]
    })
    file_path = tmp_path / "dataset.csv"
    df.to_csv(file_path, index=False)

    out = load_data(str(file_path))
    assert out.shape[0] == 2  # neutral dropped
    assert list(out.columns) == ['text', 'label']
    assert set(out['label']) <= {0, 1}

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("non_existing_file.csv")

def test_missing_columns(tmp_path):
    df = pd.DataFrame({'content': ['Good app', 'Bad app']})
    file_path = tmp_path / "bad.csv"
    df.to_csv(file_path, index=False)
    with pytest.raises(ValueError):
        load_data(str(file_path))
def test_load_data_handles_invalid_scores(tmp_path):
    """Test that invalid scores (non-numeric) are filtered out - covers exception handler"""
    csv_file = tmp_path / "invalid.csv"
    df = pd.DataFrame({
        "content": ["Good app", "Bad app", "Invalid score", "None score"],
        "score": [5, 1, "not_a_number", None]  # These trigger the exception
    })
    df.to_csv(csv_file, index=False)
    
    result = load_data(csv_file)
    # Only the first two rows with valid scores should remain
    assert len(result) == 2
    assert result["label"].tolist() == [1, 0]