from inference import predict_sentiment

def test_predict_sentiment_output():
    result = predict_sentiment("I love Aivancity!")
    assert result in ["positive", "negative"]
