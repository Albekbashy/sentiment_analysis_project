from transformers import AutoModelForSequenceClassification

def load_model():
    """
    Load a BERT model for binary sentiment classification (positive/negative).
    """
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased", num_labels=2
    )
    return model
