import unittest
import stringCalc

class StringCalcTest(unittest.TestCase):
    def test_add(self):
        res = stringCalc.string_add('10+30')
        self.assertEqual(res, 40)

    def test_substract(self):
        res = stringCalc.string_substract('30-10')
        self.assertEqual(res, 20)

    def test_multiply(self):
        res = stringCalc.string_multiply('30*10')
        self.assertEqual(res, 300)

    def test_division(self):
        res = stringCalc.string_division('30/0')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()