import pandas as pd
import pytest
from pathlib import Path
from data_processing import clean_text, load_and_clean_data  # relative import

def test_clean_text():
    assert clean_text(" Hello!! http://test ") == "hello"
    assert clean_text("I LOVE AIvancity :)") == "i love aivancity"
    assert clean_text(None) == "none"
    assert clean_text("") == ""

def test_load_and_clean_data(tmp_path):
    df = pd.DataFrame({
        'reviewId': ['r1', 'r2', 'r3'],
        'content': ['Good app', 'Bad crash', 'It is ok'],
        'score': [5, 1, 3]
    })
    file_path = tmp_path / "dataset.csv"
    df.to_csv(file_path, index=False)

    out = load_and_clean_data(str(file_path))
    assert 'content' in out.columns
    assert 'sentiment' in out.columns
    assert set(out['sentiment']) <= {0, 1, 2}

def test_missing_columns(tmp_path):
    df = pd.DataFrame({'content': ['Good app', 'Bad app']})
    file_path = tmp_path / "bad.csv"
    df.to_csv(file_path, index=False)
    with pytest.raises(ValueError):
        load_and_clean_data(str(file_path))
