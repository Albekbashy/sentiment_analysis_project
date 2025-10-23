from model import load_model
import torch

def test_model_forward_shape():
    model = load_model()
    # Create dummy input (batch_size=2, sequence_length=10)
    dummy = torch.randint(0, 1000, (2, 10))
    outputs = model(dummy)
    # Check output shape: batch_size x num_labels
    assert outputs.logits.shape == (2, 2)
