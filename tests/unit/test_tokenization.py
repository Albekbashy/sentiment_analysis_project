from data_processing import tokenize_data
import pandas as pd

def test_tokenize_data():
    df = pd.DataFrame({"text": ["I love this", "This is bad"]})
    result = tokenize_data(df)
    assert "input_ids" in result
    assert len(result["input_ids"]) == 2