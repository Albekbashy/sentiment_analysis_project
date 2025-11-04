from transformers import AutoModelForSequenceClassification

def load_model():
    """
    Load pretrained BERT for binary sentiment classification.
    """
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )
    return model
