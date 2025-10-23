import sys
import os
from pathlib import Path
import pandas as pd
import pytest

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from data_extraction import load_data

# Example: replace this with your real CSV path
REAL_FILE_PATH = Path(r"C:\Users\abdul\Downloads\dataset.csv")

def test_load_data_real_file():
    # Load data using the real CSV file
    out = load_data(REAL_FILE_PATH)

    # Basic sanity checks
    assert 'text' in out.columns
    assert 'label' in out.columns
    assert set(out['label']).issubset({0, 1})
    print("Loaded rows:", len(out))
    print(out.head())

def test_load_data_tmp_file(tmp_path):
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
