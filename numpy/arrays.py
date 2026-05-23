'''
In NumPy, 
the idea is generalized to an arbitrary number of dimensions
and so the fundamental array class is called  ndarray 
: it represents an “N-dimensional array”.

Most NumPy arrays have some restrictions
- All elements of the array must be of the same type of data.
- Once created, the total size of the array can’t change.
- The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must
have the same number of columns

When these conditions are met, NumPy exploits these characteristics to make the array faster, more
memory efficient, and more convenient to use than less restrictive data structures

'''

import numpy as np

a = np.array([1,2,3,4,5,6,7])
print(a)


# Elements of an array can be accessed in various ways. 
'''
we can access an individual element of this array as 
we would access an element in the original list: using the integer index of the
element within square brackets
'''

print(a[0])

a[0] = 100 # Like the original list, the array is mutable

print(a)

print(a[:3]) # also python slicing notation can be used for indexing

print(a[3:])


'''
One major difference is that slice indexing of a list copies the elements into a new list, but slicing an
array returns a view: an object that refers to the data in the original array. The original array can be
mutated using the view

'''

b = a[3:]
print(b)
b[0] = 50
print(a)


'''
Another difference between an array and a list of lists is that an element of the array can be accessed
by specifying the index along each axis within a single set of square brackets, separated by commas.
- For instance, the element 8 is in row 1 and column 3
'''
c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c[1,3]) # 8


print(c.ndim) # no of dimensions of an array is contained in this attribute.
print(c.shape) # is a tuple of non-negative integers that specify the no of elements along each dimesion


print(c.size) # fixed,total no of elements in array is contained in this attribute.

print(c.dtype) # arrays are typically "homogeneous". the data type is recorded in this attribute.

