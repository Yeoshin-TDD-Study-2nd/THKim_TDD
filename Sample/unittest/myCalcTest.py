import unittest
import myCalc

class MyCalcTest(unittest.TestCase):
    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 9)

class MyExceptionTest(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            1/0
        with self.assertRaises(TypeError):
            1 + '2'

if __name__ == '__main__':
    unittest.main()