import pytest
import torch

import penl


@pytest.fixture()
def resource():
    x = penl.eye(3, requires_grad=True)
    y = penl.tensor([[8.0, 0.5, -2.0]], requires_grad=True)
    torch_mm = torch.tensor([[8.0, 0.5, -2.0]], requires_grad=True).matmul(
        torch.eye(3, requires_grad=True)
    )

    def tear_down():
        ...

    return x, y, torch_mm


class TestTensorOps:
    def test_matmul(self, resource):
        x, y, torch_mm = resource
        z = penl.matmul(x, y)
        assert z.sum().item() == torch_mm.sum().item()
