## 🔑 Why NumPy Arrays?
Python lists are flexible, but they’re slow for numerical work because:
- They store elements in scattered memory locations.
- Operations like addition or multiplication need explicit loops.
- They don’t support vectorized math directly.

NumPy arrays, on the other hand:
- Store data in **contiguous memory blocks** (like C arrays).
- Allow **vectorized operations** (apply math to whole arrays at once).
- Are much faster and memory-efficient—critical for ML tasks where you deal with millions of numbers.

---

## 🧪 Quick Comparison

```python
import numpy as np
import time

# Python list addition
lst = list(range(1_000_000))
start = time.time()
lst_result = [x*2 for x in lst]
print("List time:", time.time() - start)

# NumPy array addition
arr = np.arange(1_000_000)
start = time.time()
arr_result = arr * 2
print("NumPy time:", time.time() - start)
```

👉 You’ll notice NumPy is **much faster** because it uses optimized C code under the hood.

---

## 🧩 First Steps with Arrays

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])   # from list
b = np.zeros((3, 3))             # 3x3 matrix of zeros
c = np.ones((2, 4))              # 2x4 matrix of ones
d = np.arange(0, 10, 2)          # numbers from 0 to 8 step 2
e = np.linspace(0, 1, 5)         # 5 evenly spaced numbers between 0 and 1

print(a)
print(b)
print(c)
print(d)
print(e)
```

---

## 🎯 Practice
1. Create a NumPy array of numbers from 10 to 50 with a step of 5.  
2. Create a 4×4 matrix filled with ones.  
3. Generate 7 evenly spaced values between 0 and 100.  
