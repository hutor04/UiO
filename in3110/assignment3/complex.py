from math import sqrt


class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a}+{self.b}i'
        else:
            return f'{self.a}{self.b}i'

    @staticmethod
    def _to_complex(obj):
        """
        Check if the input object is of type Complex, if not, try to convert it to Complex type.
        Supported types are complex, float, and int.
        :param obj: Any object
        :return: Complex
        """
        if isinstance(obj, Complex):
            return obj
        elif isinstance(obj, complex):
            return Complex(obj.real, obj.imag)
        elif isinstance(obj, float):
            return Complex(obj, 0)
        elif isinstance(obj, int):
            return Complex(obj, 0)
        else:
            raise TypeError("Must be a complex number object")

    # Assignment 3.3
    def conjugate(self):
        """
        Conjugate self.
        :return: A new instance of Complex
        """
        return Complex(self.a, -self.b)

    def modulus(self):
        """
        Modulus of self.
        :return:  A new instance of Complex
        """
        return sqrt(self.a**2 + self.b**2)

    def __add__(self, other):
        """
        Addition of two complex numbers
        :param other: Complex compatible object
        :return: The result of Sum of self and object
        """
        obj = self._to_complex(other)
        return Complex(self.a + obj.a, self.b + obj.b)

    def __sub__(self, other):
        """
        Subtraction of two complex numbers. It is based on addition and negative
        :param other: Complex compatible object
        :return: Subtraction of self and object
        """
        obj = self._to_complex(other)
        return self.__add__(-obj)

    def __mul__(self, other):
        """
        Multiplication of two complex numbers.
        :param other: Complex compatible object
        :return: The result of multiplication of two complex numbers
        """
        obj = self._to_complex(other)
        return Complex(self.a * obj.a - self.b * obj.b,
                       self.a * obj.b + self.b * obj.a)

    def __eq__(self, other):
        """
        Comparison of two complex numbers
        :param other: Complex compatible object
        :return: True or False
        """
        obj = self._to_complex(other)
        return self.a == obj.a and self.b == obj.b

    # Assignment 3.4
    def __radd__(self, other):
        """
        Addition of two complex numbers
        :param other: Complex compatible object
        :return: The result of Sum of self and object
        """
        return self.__add__(other)

    def __rmul__(self, other):
        """
        Multiplication of two complex numbers
        :param other: Complex compatible object
        :return: The result of multiplication of two complex numbers
        """
        return self.__mul__(other)

    def __rsub__(self, other):
        """
        Subtraction of two complex numbers. It is based on addition and negative
        :param other: Complex compatible object
        :return: Subtraction of self and object
        """
        obj = self._to_complex(other)
        return obj - self

    def __neg__(self):
        """
        A negative complex number of self
        :return: a new instance of Complex
        """
        return Complex(-self.a, -self.b)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        """
        Turns self to an instance of Python's built-in complex number type
        :return: en instance of built-in complex number class
        """
        return complex(self.a, self.b)
