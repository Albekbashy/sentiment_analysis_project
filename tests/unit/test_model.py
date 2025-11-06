from model import load_model  # relative import
import torch

def test_model_output_shape():
    model = load_model()
    dummy_input = torch.randint(0, 1000, (2, 10))
    outputs = model(dummy_input)
    assert outputs.logits.shape == (2, 2)

def test_model_batch_size():
    model = load_model()
    dummy_input = torch.randint(0, 1000, (5, 10))
    outputs = model(dummy_input)
    assert outputs.logits.shape[0] == 5
