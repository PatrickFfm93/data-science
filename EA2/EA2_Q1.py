from time import time
import numpy as np

print(time())
## without numpy
a = [23, 104, 5, 190, 8, 7, -3]
b = []
random = list(range(1000000)) # or np.random.rand(1000000) with numpy

## Write a python function to get the indices of the sorted elements of given lists and compare the speed without using numpy and with numpy.
def indices_sorted_without_numpy(lst):
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numeric elements")
    
    start1 = time()
    indices = sorted(range(len(lst)), key=lambda i: lst[i])
    computetime = time() - start1
    print(f"Computation time without numpy: {computetime}")
    return indices

def indices_sorted_with_numpy(lst):
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numeric elements")
    
    start2 = time()
    indices_np = np.argsort(lst)
    computetime = time() - start2
    print(f"Computation time with numpy: {computetime}")
    return indices_np



print("List a, indices without numpy:", indices_sorted_without_numpy(a))
print("List a, indices with numpy:", indices_sorted_with_numpy(a))

print("List b, indices without numpy:", indices_sorted_without_numpy(b))
print("List b, indices with numpy:", indices_sorted_with_numpy(b))

print("List random, indices without numpy:", indices_sorted_without_numpy(random))
print("List random, indices with numpy:", indices_sorted_with_numpy(random))