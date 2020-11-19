#!/usr/bin/env python3

from complex import Complex
import unittest


class TestComplexClass(unittest.TestCase):
    def test_complex_plus(self):
        """
        Test add operation of Complex class
        :return: None
        """
        i = Complex(2, 3)
        j = Complex(4, 5)
        k = complex(4, 5)
        self.assertEqual(i + j, Complex(6, 8))
        self.assertEqual(i + k, Complex(6, 8))
        self.assertEqual(k + i, Complex(6, 8))
        self.assertEqual(j + 2, Complex(6, 5))
        self.assertEqual(2 + j, Complex(6, 5))

    def test_complex_minus(self):
        """
        Test subtraction of Complex class
        :return: None
        """
        i = Complex(2, 3)
        j = Complex(4, 5)
        k = complex(4, 5)
        self.assertEqual(i - j, Complex(-2, -2))
        self.assertEqual(j - i, Complex(2, 2))
        self.assertEqual(i - k, Complex(-2, -2))
        self.assertEqual(k - i, Complex(2, 2))
        self.assertEqual(j - 2, Complex(2, 5))
        self.assertEqual(2 - j, Complex(-2, -5))

    def test_complex_mult(self):
        """
        Test multiplication of Complex class
        :return: None
        """
        i = Complex(2, 3)
        j = Complex(4, 5)
        k = complex(4, 5)
        self.assertEqual(i * j, Complex(-7, 22))
        self.assertEqual(j * i, Complex(-7, 22))
        self.assertEqual(i * k, Complex(-7, 22))
        self.assertEqual(k * i, Complex(-7, 22))
        self.assertEqual(i * 2, Complex(4, 6))
        self.assertEqual(2 * i, Complex(4, 6))

    def test_conjugate(self):
        """
        Test conjugation of Complex class
        :return: None
        """
        i = Complex(2, -3)
        j = Complex(2, 3)
        self.assertEqual(i.conjugate(), Complex(2, 3))
        self.assertEqual(j.conjugate(), Complex(2, -3))

    def test_modulus(self):
        """
        Test modulus of Complex class
        :return: None
        """
        i = Complex(2, 3)
        self.assertEqual(i.modulus(), 3.605551275463989)

    def test_equals(self):
        """
        Test equality of Complex class
        :return:
        """
        i = Complex(2, 3)
        j = Complex(4, 5)
        k = Complex(2, 3)
        self.assertNotEqual(i, j)
        self.assertEqual(i, k)
        self.assertNotEqual(i, complex(4, 5))
        self.assertEqual(2, Complex(2, 0))


if __name__ == '__main__':
    unittest.main()

