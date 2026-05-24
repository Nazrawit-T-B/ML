import numpy as np
# The most basic way to create a numpy array is by converting a Python sequence
# like a list or a tuple into an array. We can do this using the array() function.
#NumPy arrays have a fixed data type for all elements, which is specified by the dtype parameter
one_D = np.array([1, 2, 3, 4, 5])
two_D = np.array([[1, 2], [3, 4]])
three_D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1-D array:")
print(one_D)
print("\n2-D array:")
print(two_D)
print("\n3-D array:")
print(three_D)