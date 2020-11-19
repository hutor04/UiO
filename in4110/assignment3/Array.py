from functools import reduce


class Array:
    # Assignment 3.3

    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        if any(isinstance(_, bool) for _ in values) and not all(isinstance(_, bool) for _ in values):
            raise ValueError('Array values must be the same type: numerical or boolean.')

        if not all(isinstance(_, (int, float, complex)) for _ in values):
            raise ValueError('Array values must be the same type: numerical or boolean.')

        if len(shape) >= 1:
            if not reduce((lambda x, y: x * y), shape) == len(values):
                raise ValueError('Shape does not match number of elements')

        if len(shape) == 0:
            if not len(values) == 0:
                raise ValueError('Shape does not match number of elements')

        self.array = values
        self.shape = shape
        self.boolean = all(isinstance(_, bool) for _ in values)

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:int, float, complex
            str: A string representation of the array.
        """
        if len(self.shape) == 1:
            return f"[{' '.join(map(lambda x: str(x), self.array))}]"
        elif len(self.shape) == 0:
            return '[ ]'
        elif len(self.shape) == 2:
            result = '[\n'
            start = 0
            end = self.shape[1]
            for i in range(self.shape[0]):
                result += f"{' '.join(map(lambda x: str(x), self.array[start:end]))}\n"
                start = end
                end += self.shape[1]
            result += ']'
            return result
        else:
            raise NotImplemented('Only available for 1D and 2D arrays')

    def __getitem__(self, item):
        if len(self.shape) > 1:
            segment_size = reduce(lambda x, y: x*y, self.shape[1:])
            end = (item + 1) * segment_size
            start = end - segment_size
            return Array(self.shape[1:], *self.array[start:end])
        if len(self.shape) == 1:
            return self.array[item]

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return Array(self.shape, *tuple(x + y for x, y in zip(self.array, other.array)))
            else:
                raise NotImplemented('Only arrays of the same shape can be added.')
        elif isinstance(other, (int, float, complex)):
            return Array(self.shape, *tuple(x + other for x in self.array))
        else:
            raise NotImplemented('Something went wrong.')

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return Array(self.shape, *tuple(x - y for x, y in zip(self.array, other.array)))
            else:
                raise NotImplemented('Only arrays of the same shape can be added.')
        elif isinstance(other, (int, float, complex)):
            return Array(self.shape, *tuple(x - other for x in self.array))
        else:
            raise NotImplemented('Something went wrong.')

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return Array(self.shape, *tuple(y - x for x, y in zip(self.array, other.array)))
            else:
                raise NotImplemented('Only arrays of the same shape can be added.')
        elif isinstance(other, (int, float, complex)):
            return Array(self.shape, *tuple(other - x for x in self.array))
        else:
            raise NotImplemented('Something went wrong.')

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return Array(self.shape, *tuple(x * y for x, y in zip(self.array, other.array)))
            else:
                raise NotImplemented('Only arrays of the same shape can be added.')
        elif isinstance(other, (int, float, complex)):
            return Array(self.shape, *tuple(x * other for x in self.array))
        else:
            raise NotImplemented('Something went wrong.')

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return self.array == other.array
            else:
                return False
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if type(other) == type(self):
            if self.shape == other.shape:
                return Array(self.shape, *tuple(x == y for x, y in zip(self.array, other.array)))
            else:
                raise ValueError('Only arrays of the same shape can be compared.')
        elif isinstance(other, (int, float, complex)):
            return Array(self.shape, *tuple(x == other for x in self.array))
        else:
            raise NotImplemented('Something went wrong.')

    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        if not self.boolean:
            return sum(self.array) / len(self.array)
        else:
            pass

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        arr_mean = self.mean()
        return sum((x - arr_mean)**2 for x in self.array) / len(self.array)

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        if not self.boolean:
            return min(self.array)
        else:
            pass