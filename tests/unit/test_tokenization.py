from data_processing import tokenize_data  # relative import
import pandas as pd

def test_tokenize_data():
    df = pd.DataFrame({"text": ["I love this", "This is bad"]})
    result = tokenize_data(df)
    assert "input_ids" in result
    assert len(result["input_ids"]) == 2
    assert all(isinstance(i, list) for i in result["input_ids"])

def test_tokenize_empty_text():
    df = pd.DataFrame({"text": ["", None]})
    result = tokenize_data(df)
    assert len(result["input_ids"]) == 2
