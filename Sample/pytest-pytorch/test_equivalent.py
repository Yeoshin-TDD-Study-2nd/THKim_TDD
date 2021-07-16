import pytest
import torch

@pytest.mark.parametrize("device", ["cpu"])
class TestFoo:
    @pytest.mark.parametrize("dtype", [pytest.param(torch.float32, id="float32")])
    @pytest.mark.parametrize("op", ["add", "sub"])
    def test_bar(self, device, dtype, op):
        pass
    