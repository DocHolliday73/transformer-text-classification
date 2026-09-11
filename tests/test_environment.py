import torch
import transformers
import datasets


def test_environment():
    assert torch.__version__
    assert transformers.__version__
    assert datasets.__version__