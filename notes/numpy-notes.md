# Numpy

- NumPy is a Python library used for working with arrays.
- It also has functions for working in the domain of linear algebra, Fourier transform, and matrices.
- NumPy was created in 2005 by Travis Oliphant. 
- It is an open-source project and you can use it freely.
- NumPy stands for Numerical Python.
- https://github.com/numpy/numpy.

###  Why Use Numpy

- In Python, we have lists that serve the purpose of arrays, but they are slow to process.
- NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
- The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
- Arrays are very frequently used in data science, where speed and resources are very important.


### Why is NumPy Faster Than Lists?

- NumPy arrays are stored at one continuous place in memory, unlike lists.
	- So processes can access and manipulate them very efficiently.
	- This behaviour is called the locality of reference in computer science.
- This is the main reason why NumPy is faster than lists.
- Also, it is optimized to work with the latest CPU architectures.
- NumPy is a Python library and is written partially in Python.
	- Most of the parts that require fast computation are written in C or C++.

### Import Numpy

Install NumPy:      
```bash
conda install numpy
pip install numpy
```

```python
import numpy as np

arr=np.array([1,2,3,4,5,6,7])
print(arr)
print(type(arr))

```
`type()` - This built-in Python function tells us the type of the object passed to it.
Like in the above code it shows that arr is numpy.ndarray type.

- An ndarray is a (usually fixed-size) multidimensional container of items of the same type and size. 
- The number of dimensions and items in an array is defined by its shape, which is a tuple of N non-negative integers that specify the sizes of each dimension. 
- The type of items in the array is specified by a separate data-type object (dtype), one of which is associated with each ndarray.

```python 
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
```
![](arrays.png)

### Accessing Numpy Array

- The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

```py
arr = np.array([1, 2, 3, 4, 5])
```
*index → 0, 1, 2, 3, 4*

### Reshape ndarray

```py
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
```

![](reshape.png)

### Slicing

- Slicing in python means taking elements from one given index to another given index.
- We pass slice instead of index like this: [start:end].
- We can also define the step, like this: [start:end:step].
	- If we don't pass start its considered 0
	- If we don't pass end its considered length of array in that dimension
	- If we don't pass step its considered 1

```py
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
```
**The result includes the start index, but excludes the end index.**

![](slicing.png)

### Search, Sort, Filter
```py
import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("Original array:", arr1)

a = [True, False, False, True]
b = arr1[a]

print("Filtered array:", b)

#-----------------------------
print('-------------------------------')

arr2 = np.array([3, 2, 0, 1])

print("Original array:", arr2)
print("Sorted array:", np.sort(arr2))

#-----------------------------
print('-------------------------------')

arr3 = np.array([1, 1, 2, 3, 4, 1])
print("Original array:", arr3)

c = np.where(arr3==1)

print("Index of element 1:", c)
```
