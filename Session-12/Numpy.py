"""
Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional
array object, and tools for working with these arrays.
Numpy can also be used as an efficient multi-dimensional container of generic data.


Arrays in Numpy:

Array in Numpy is a table of elements (usually numbers), all of the same type,
indexed by a tuple of positive integers.
In Numpy, number of dimensions of the array is called rank of the array.
A tuple of integers giving the size of the array along each dimension is known as shape of the array.
An array class in Numpy is called as ndarray.

Elements in Numpy arrays are accessed by using square brackets.

"""
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 2, 5]])

print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
print('\n')

"""
Different ways of creating Numpy Arrays:

1.Intuitive approach: Using numpy.array():
    Numpy arrays can be created very easily by passing a list to the function numpy.array().
"""
li = [8, 5, 6, 9, 4, 2]
numpy_array = np.array(li)
print(numpy_array)

numpy_array2 = np.array([5, 7, 4, 1, 5, 6])
print(numpy_array2)

"""
dtype: This argument specifies the data-type of the array being created. Since, unlike lists, all the elements
in the Numpy array are of the same data-type.
"""

numpy_array = np.array([1, 8, 5, 59, 8, 98], dtype='float')
print(numpy_array)

Str = ['example', 'for', 'string', 'dtype', 'array']
arr = np.array(Str, dtype='str')
print(arr)
print('\n')

"""
Using arange() function to create a Numpy array:
 The first argument takes the starting point of the array you want to create, second is the stop point and
the third is the step. The last argument is again dtype, which is optional.
"""

arange_array = np.arange(0, 11, 2)
print("First array", arange_array)

arr1 = np.arange(15)
print("Second Array", arr1)

arr2 = np.arange(20, 0, -1)
print("Reverse Array", arr2)
print('\n')

"""
3. Creating Numpy array using linspace() function:
    Like arange() function, linspace() function can also be used to create Numpy array but
with more discipline.

linspace() function takes arguments: start index, end index and the number of elements to be outputted.
These number of elements would be linearly spaced in the range mentioned.
"""

arr = np.linspace(1, 10, 10)
print("First Array with linspace", arr)

arr1 = np.linspace(51, 99, 25)
print("Second Array with linspace", arr1)
print('\n')

"""
The empty() function is used to create arrays when we don't really have any values to create an array.
What it does is, it takes the shape of the array as desired and the array is then filled with random values.
The trick here is that without even using the random module we are able to build an array full of random values.

Syntax:
    empty(shape, dtype)
"""

arr = np.empty((5, 2), dtype=float)
print("Array with Float values using empty", arr)

arr1 = np.empty((4, 4), dtype=int)
print("Array with int values using empty", arr1)
print('\n')

"""
Special functions like np.zeros, np.ones, np.full
"""

zeros = np.zeros((3, 4))
print("array using np.zeroes", zeros)
ones = np.ones((3, 4))
print("array using np.ones", ones)
full = np.full((3, 4), 10)
print("array using np.full with value 10", full)
print('\n')

"""
we can also create 3D , 4D and n dimensional arrays
"""

threeD_array = np.full((2, 3, 4), 5)
print(threeD_array)
print('\n')
print(threeD_array[1, 2, 3])
fourD_array = np.full((2, 3, 5, 5), 5)
print(fourD_array)
print('\n')

"""
Indexing and Slicing in numpy arrays

We can achieve array indexing in three ways
1.Slicing: Just like lists in python, NumPy arrays can be sliced. As arrays can be multidimensional,
you need to specify a slice for each dimension of the array.
"""
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
temp = arr[1:3, 2:4]
print("array after slicing in their respective dimensions \n", temp, '\n')

print(arr[:, ::2])
print('\n')

"""
2.Integer array indexing:
    Integer array indexing: In this method, lists are passed for indexing for each dimension.
One to one mapping of corresponding elements is done to construct a new arbitrary array.
"""

temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp)
temp1 = arr[[0, 1, 2, 3], 2]
print("\nElements at indices (0, 2), (1, 2), (2, 2),(3, 2):\n", temp1)
print('\n')

"""
Boolean array indexing:    
    This method is used when we want to pick elements from array which satisfy some condition.
"""

temp = arr[arr >= 10]
print("\nElements greater than 2 : \n", temp)

"""

Iterating over an ndarray
1. using multiple loops

"""
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in arr:
    for y in x:
        print(y)

"""

2. using nditer()

"""
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
