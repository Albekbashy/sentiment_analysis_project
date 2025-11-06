from inference import predict_sentiment  # relative import

def test_predict_sentiment_output():
    assert predict_sentiment("I love Aivancity!") in ["positive", "negative"]
    assert predict_sentiment("This is terrible!") in ["positive", "negative"]
