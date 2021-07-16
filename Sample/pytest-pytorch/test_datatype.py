import torch

from torch.testing._internal.common_utils import TestCase
from torch.testing._internal.common_device_type import (
    instantiate_device_type_tests,
    dtypes,
)

class TestFoo(TestCase):
    @dtypes(torch.int32, torch.float32)
    def test_bar(self, device, dtype):
        pass

instantiate_device_type_tests(TestFoo, globals(), only_for="cpu")