import numpy as np
# Create an array with a range of elements
# np.arange(start, stop, step) - similar to Python's range()
# Use case: Creating sequences for loops, generating indices
arr_range=np.arange(0,10,2)
print("Array from arange: ")
print(arr_range)

arr_linspace=np.linspace(0,10,5)
print("\nArray from linspace: ")
print(arr_linspace)

arr_zeros=np.zeros((2,3))
print("\nArray of zeros: ")
print(arr_zeros)

arr_ones=np.ones((2,3))
print("\nArray of ones: ")
print(arr_ones)

arr_identity=np.eye(3)
print("\nIdentity matrix")
print(arr_identity)
