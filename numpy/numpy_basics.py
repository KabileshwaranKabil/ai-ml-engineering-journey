import numpy as np  

print(np.__version__) # version

arr = np.array([1,2,4,5,6,7])
print(arr)
print(type(arr))


print(arr[0]) # print first element of arr.

newArr = arr.reshape(3,2)
print(newArr)
print(type(newArr))


print(arr[1:3]) # excluding 3rd element

print(arr[1:len(arr):2])
