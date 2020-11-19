#!/usr/bin/env python3
from Array import Array
import unittest


class TestMyArray(unittest.TestCase):
    def test_shape_01(self):
        """
        Make sure that the array raises error when shape and the number of elements mismatch.
        :return: None
        """
        with self.assertRaises(Exception) as context:
            a = Array((1,), 1, 2, 3)
        self.assertEqual('Shape does not match number of elements', context.exception.__str__())

    def test_shape_02(self):
        """
        Make sure that the array raises error when shape and the number of elements mismatch.
        :return: None
        """
        with self.assertRaises(Exception) as context:
            a = Array((2, 2), 1, 2, 3)
        self.assertEqual('Shape does not match number of elements', context.exception.__str__())

    def test_shape_03(self):
        """
        Make sure the array is created as per the given input, and the elements are accessible according to the
        shape of the array.
        :return: None
        """
        a = Array((1, ), 1)
        self.assertEqual(a.shape, (1,))
        self.assertEqual(a.array, (1,))
        self.assertEqual(a[0], 1)

    def test_shape_04(self):
        """
        Make sure the array is created as per the given input, and the elements are accessible according to the
        shape of the array.
        :return: None
        """
        a = Array((2, 2), 1, 2, 3, 4)
        self.assertEqual(a.shape, (2, 2))
        self.assertEqual(a.array, (1, 2, 3, 4))
        self.assertEqual(a[0], Array((2,), 1, 2))
        self.assertEqual(a[1][0], 3)

    def test_shape_05(self):
        """
        Make sure the array is created as per the given input, and the elements are accessible according to the
        shape of the array.
        :return: None
        """
        a = Array((), )
        self.assertEqual(a.shape, ())
        self.assertEqual(a.array, ())

    def test_shape_06(self):
        """
        Make sure the array is created as per the given input, and the elements are accessible according to the
        shape of the array.
        :return: None
        """
        a = Array((3, 2, 2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.assertEqual(a[1], Array((2, 2), 5, 6, 7, 8))
        self.assertEqual(a[1][0], Array((2,), 5, 6))
        self.assertEqual(a[1][0][1], 6)

    def test_types_01(self):
        """
        Make sure that the array accepts either only numeric types or booleans and does not allow to mix them.
        :return: None
        """
        a = Array((3,), 1, 2.4, 0)
        self.assertEqual(a.shape, (3, ))
        self.assertEqual(a.array, (1, 2.4, 0))

    def test_types_02(self):
        """
        Make sure that the array accepts either only numeric types or booleans and does not allow to mix them.
        :return: None
        """
        a = Array((3,), True, False, True)
        self.assertEqual(a.shape, (3, ))
        self.assertEqual(a.array, (True, False, True))

    def test_types_03(self):
        """
        Make sure that the array accepts either only numeric types or booleans and does not allow to mix them.
        :return: None
        """
        with self.assertRaises(Exception) as context:
            a = Array((1,), 1, False, 3)
        self.assertEqual('Array values must be the same type: numerical or boolean.', context.exception.__str__())

    def test_types_04(self):
        """
        Make sure that the array accepts either only numeric types or booleans and does not allow to mix them.
        :return: None
        """
        with self.assertRaises(Exception) as context:
            a = Array((1,), 1, 'hello', 3)
        self.assertEqual('Array values must be the same type: numerical or boolean.', context.exception.__str__())

    def test_printing_01(self):
        """
        Make sure the array is prinde to string.
        :return:
        """
        a = Array((3,), True, False, True)
        self.assertEqual(a.__str__(), '[True False True]')

    def test_printing_02(self):
        """
        Make sure the array is prinde to string.
        :return:
        """
        a = Array((3, 3), 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(a.__str__(), '[\n1 2 3\n4 5 6\n7 8 9\n]')

    def test_printing_03(self):
        """
        Make sure the array is prinde to string.
        :return:
        """
        a = Array((), )
        self.assertEqual(a.__str__(), '[ ]')

    def test_adding_01(self):
        """
        Test elementwise addition.
        :return:  None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3,), 8, 3, 4)
        self.assertEqual(a + 1, Array((3, 2), 9, 4, 5, 2, 7, 2))
        self.assertEqual(b + 1, Array((3, ), 9, 4, 5))

    def test_adding_02(self):
        """
        Test elementwise addition.
        :return:  None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3, 2), 8, 3, 4, 1, 6, 1)
        a1 = Array((3,), 8, 3, 4)
        b1 = Array((3,), 8, 3, 4)
        self.assertEqual(a + b, Array((3, 2), 16, 6, 8, 2, 12, 2))
        self.assertEqual(a1 + b1, Array((3,), 16, 6, 8))

    def test_substraction_01(self):
        """
        Test elementwise substraction.
        :return:  None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3,), 8, 3, 4)
        self.assertEqual(a - 1, Array((3, 2), 7, 2, 3, 0, 5, 0))
        self.assertEqual(b - 1, Array((3,), 7, 2, 3))

    def test_substraction_02(self):
        """
        Test elementwise substraction.
        :return:  None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3, 2), 8, 3, 4, 1, 6, 1)
        a1 = Array((3,), 8, 3, 4)
        b1 = Array((3,), 8, 3, 4)
        self.assertEqual(a - b, Array((3, 2), 0, 0, 0, 0, 0, 0))
        self.assertEqual(a1 - b1, Array((3,), 0, 0, 0))

    def test_multiplication_01(self):
        """
        Test elementwise multiplication.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3,), 8, 3, 4)
        self.assertEqual(a * 2, Array((3, 2), 16, 6, 8, 2, 12, 2))
        self.assertEqual(b * 2, Array((3,), 16, 6, 8))

    def test_multiplication_02(self):
        """
        Test elementwise multiplication.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3,), 8, 3, 4)
        self.assertEqual(a * a, Array((3, 2), 64, 9, 16, 1, 36, 1))
        self.assertEqual(b * b, Array((3,), 64, 9, 16))

    def test_equality_01(self):
        """
        Test equality between the two arrays.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 6, 1)
        b = Array((3, 2), 8, 3, 4, 1, 6, 1)
        a1 = Array((3,), 8, 3, 4)
        b1 = Array((3,), 8, 3, 4)
        self.assertTrue(a == b)
        self.assertTrue(a1 == b1)

    def test_equality_02(self):
        """
        Test equality between the two arrays.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 5, 1)
        b = Array((3, 2), 8, 3, 4, 1, 6, 1)
        a1 = Array((3,), 8, 3, 4)
        b1 = Array((3,), 8, 3, 5)
        self.assertFalse(a == b)
        self.assertFalse(a1 == b1)

    def test_equality_03(self):
        """
        Test equality between the two arrays.
        :return: None
        """
        a = Array((3, 2), True, False, True, True, False, True)
        b = Array((3, 2), True, False, True, True, False, True)
        a1 = Array((3, ), True, False, True)
        b1 = Array((3, ), True, False, True)
        self.assertTrue(a == b)
        self.assertTrue(a1 == b1)

    def test_equality04(self):
        """
        Test equality between the two arrays.
        :return: None
        """
        a = Array((3, 2), True, True, True, True, True, True)
        b = Array((3, 2), True, False, True, True, True, True)
        a1 = Array((3, ), True, True, True)
        b1 = Array((3, ), True, False, True)
        self.assertFalse(a == b)
        self.assertFalse(a1 == b1)

    def test_is_equal_01(self):
        """
        Test is_equal method of the array.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 5, 1)
        b = Array((3,), 8, 1, 4)
        self.assertEqual(a.is_equal(1), Array((3, 2), False, False, False, True, False, True))
        self.assertEqual(b.is_equal(1), Array((3,), False, True, False))

    def test_is_equal_02(self):
        """
        Test is_equal method of the array.
        :return: None
        """
        a = Array((3, 2), 8, 3, 4, 1, 5, 1)
        b = Array((3, 2), 7, 2, 3, 1, 4, 1)
        a1 = Array((3,), 8, 3, 4)
        b1 = Array((3,), 8, 3, 5)
        self.assertEqual(a.is_equal(b), Array((3, 2), False, False, False, True, False, True))
        self.assertEqual(a1.is_equal(b1), Array((3,), True, True, False))

    def test_mean_01(self):
        """
        Make sure the mean is calculated correctly.
        :return: None
        """
        a = Array((3, 2), 0, 0, 0, 0, 0, 0)
        b = Array((3,), 0, 0, 0)
        self.assertEqual(a.mean(), 0)
        self.assertEqual(b.mean(), 0)

    def test_mean_02(self):
        """
        Make sure the mean is calculated correctly.
        :return: None
        """
        a = Array((3, 2), 1, 2, 3, 4, 5, 6)
        b = Array((3,), 1, 2, 3)
        self.assertEqual(a.mean(), 3.5)
        self.assertEqual(b.mean(), 2.0)

    def test_variance_01(self):
        """
        Make sure the variance is calculated correctly.
        :return: None
        """
        truth = 2.9166666666666665
        truth1 = 0.6666666666666666
        a = Array((3, 2), 1, 2, 3, 4, 5, 6)
        b = Array((3,), 1, 2, 3)
        self.assertAlmostEqual(a.variance(), truth)
        self.assertAlmostEqual(b.variance(), truth1)

    def test_variance_02(self):
        """
        Make sure the variance is calculated correctly.
        :return: None
        """
        truth = 0
        a = Array((3, 2), 1, 1, 1, 1, 1, 1)
        b = Array((3,), 1, 1, 1)
        self.assertAlmostEqual(a.variance(), truth)
        self.assertAlmostEqual(b.variance(), truth)

    def test_min_01(self):
        """
        Make sure the minimum is calculated correctly.
        :return: None
        """
        a = Array((3, 2), 1, 2, 3, 4, 5, 6)
        b = Array((3,), 1, 2, 3)
        self.assertEqual(a.min_element(), 1)
        self.assertEqual(b.min_element(), 1)

    def test_min_02(self):
        """
        Make sure the minimum is calculated correctly.
        :return: None
        """
        a = Array((3, 2), 0, 0, 0, 0, 0, 0)
        b = Array((3,), 0, 0, 0)
        self.assertEqual(a.min_element(), 0)
        self.assertEqual(b.min_element(), 0)


if __name__ == '__main__':
    unittest.main()
