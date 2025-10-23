import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pandas as pd
from data_extraction import load_data
import pytest

def test_load_data(tmp_path):
    # Create a temporary CSV file
    df = pd.DataFrame({
        'reviewId': ['r1','r2','r3'],
        'content': ['Good app', 'Bad crash', 'It is ok'],
        'score': [5, 1, 3]  # score=3 will be dropped
    })
    file_path = tmp_path / "dataset.csv"
    df.to_csv(file_path, index=False)

    # Load data using our function
    out = load_data(str(file_path))

    # Check shape (neutral row removed)
    assert out.shape[0] == 2

    # Check columns
    assert list(out.columns) == ['text', 'label']

    # Check labels
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
