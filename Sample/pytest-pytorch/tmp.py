from torch.testing._internal.common_utils import TestCase
from torch.testing._internal.common_device_type import instantiate_device_type_tests
import pytest

@pytest.mark.parametrize("device", ("cpu", "cuda"))
class TestFoo(TestCase):
    def test_bar(self, device):
        pass
    
    def test_baz(self, device):
        pass

    
instantiate_device_type_tests(TestFoo, globals(), only_for=["cpu", "cuda"])
