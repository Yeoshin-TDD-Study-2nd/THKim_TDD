import torch

from torch.testing import _dispatch_dtypes
from torch.testing._internal.common_device_type import (
    instantiate_device_type_tests,
    ops,
)
from torch.testing._internal.common_methods_invocations import OpInfo
from torch.testing._internal.common_utils import TestCase

op_db = [
    OpInfo("add", dtypesIfCPU=_dispatch_dtypes([torch.int32])),
    OpInfo("sub", dtypesIfCPU=_dispatch_dtypes([torch.float32])),
]

class TestFoo(TestCase):
    @ops(op_db)
    def test_bar(self, device, dtype, op):
        pass

instantiate_device_type_tests(TestFoo, globals(), only_for="cpu")