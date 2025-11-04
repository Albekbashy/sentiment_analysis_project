from transformers import AutoTokenizer
from model import load_model
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = load_model()

def predict_sentiment(text: str) -> str:
    """
    Return 'positive' or 'negative' sentiment prediction.
    """
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**tokens)
    pred = torch.argmax(outputs.logits, dim=1).item()
    return "positive" if pred == 1 else "negative"
