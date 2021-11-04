"""
Operations on single array: We can use overloaded arithmetic operators to do element-wise operation on array
to create a new array.
"""
import numpy as np

arr = np.array([5, 6, 7, 8])
print("Adding 1 to every element:", arr + 1)
print("Multiplying each element by 10:", arr * 10)
print("Remainder of each element by dividing with 2:", arr % 2)

print('\n')
"""
Unary operators: 
    Many unary operations are provided as a method of ndarray class. This includes sum, min, max, etc.
These functions can also be applied row-wise or column-wise by setting an axis parameter.
"""

arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

print("Largest element is:", arr1.max())

print("Row-wise maximum elements:", arr1.max(axis=1))

print("Column-wise minimum elements:", arr1.min(axis=0))

print("Sum of all array elements:", arr1.sum())

print("Cumulative sum along each row:\n", arr1.cumsum(axis=1))
print('\n')

"""
Binary operators: 
    These operations apply on array element-wise and a new array is created.
You can use all basic arithmetic operators like +, -, *, /,
"""

a = np.array([[1, 2],[3, 4]])
b = np.array([[4, 3, 2], [2, 1, 0]])
# print("Array sum:\n", a + b)
# print("Array multiplication:\n", a * b)
print("Matrix multiplication:\n", a.dot(b))
print('\n')

"""
Reshaping arrays:
    Reshaping means changing the shape of an array.
By reshaping we can add or remove dimensions or change number of elements in each dimension.
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print('\n')

"""
1D to 3D
"""

new_threeD_arr = arr.reshape(2, 3, 2)
print(new_threeD_arr)
print('\n')

"""
Unknown Dimension
    You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.
"""
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr2.reshape(2, 2, -1)
print(new_arr)
print('\n')

"""
Flattening the arrays
"""

flat1 = new_threeD_arr.flatten()
flat2 = new_threeD_arr.reshape(-1)
print("using flatten \n", flat1)
print("using reshape \n", flat2)
print('\n')

"""
array_split():
     Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
We also have the method split() available but it will not adjust the elements when elements
are less in source array for splitting
"""

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
print("split 1D array: ")
print(newarr[0])
print(newarr[1])
print(newarr[2])
print('\n')
"""
Splitting 2-D Arrays
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 4)
print("split 2D array along rows: ")
print(newarr[0], '\n')
print(newarr[1], '\n')
print(newarr[2], '\n')
print(newarr[3], '\n')
print(newarr[0].shape, '\n')

"""
using split will rise error error "Value Error: array split does not result in an equal division"
newarr1 = np.split(arr, 4)
print(newarr1[0], '\n')
print(newarr1[1], '\n')
print(newarr1[2], '\n')
print(newarr1[3], '\n')"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 4, axis=1)
print("split 2D array along columns: ")
print(newarr[0], '\n')
print(newarr[1], '\n')
print(newarr[2], '\n')
print(newarr[3], '\n')
print(newarr[0].shape, '\n')

"""
Searching Arrays:
    You can search an array for a certain value, and return the indexes that get a match.
To search an array, use the where() method.
"""
arr = np.array([1, 2, 3, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
x = np.where(arr % 2 == 0)
print(x)
print('\n')

"""
Sorting Arrays:
    The NumPy ndarray object has a function called sort(), that will sort a specified array.
"""

arr = np.array([6, 3, 7, 2, 0])
x = np.sort(arr)
print("sorted 1D array \n", x)
print()

"""
sorting 2D array 
"""

arr = np.array([[3, 2, 4], [5, 0, 1]])
x = np.sort(arr)
print("sorted 2D array along column\n", x)
print()

arr = np.array([[3, 2, 4], [5, 0, 1]])
x = np.sort(arr, axis=0)
print("sorted 2D array along rows \n", x)
print()

"""
Getting some elements out of an existing array and creating a new array out of them is called filtering.
In NumPy, you filter an array using a boolean index list.
There are two ways to filter 
1. Creating a filter array and passing it to our array
    If the value at an index is True that element is contained in the filtered array,
if the value at that index is False that element is excluded from the filtered array.
"""

arr = np.array([1, 2, 3, 4])
x = [True, False, True, False]
filtered_arr = arr[x]
print("original: ", arr, "\nfiltered", filtered_arr)
print()

"""
2.Creating Filter Directly From Array
    We can directly substitute the array instead of the iterable variable in our condition
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filtered_arr = arr[arr % 2 == 0]
print("original: ", arr, "\nfiltered", filtered_arr)
print()
