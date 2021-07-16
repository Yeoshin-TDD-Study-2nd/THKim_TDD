from unittest.mock import Mock

"""
>>> mock = Mock(return_value='Hello, Mock!')
>>> print(mock())

>>> mock = Mock(side_effect=Exception('Oops!'))
>>> print(mock())

>>> mock = Mock(side_effect=[1,2,3])
>>> for _ in range(3):
        mock()
"""