#Indexing is fundamental to data manipulation because it allows you to access and modify specific elements, rows, or columns in an array.
# Extract subsets of data for analysis 
# Modify specific values in large datasets
# filter data based on conditions 
# perform vectorized operations on selected elements

# Slicing lets you select a range of elements with the syntax start:stop:step

import numpy as np
x=np.arange(10)
print("Original array: ",x)

element=x[2]
print("Element at index 2: ",element)

a_slice=x[1:7:2]
print("Slice from 1 to 7 with step 2: ")

w=np.arange(12).reshape(3,4)
print("Original 2D array:\n", x)
element=w[1,2]
print("\nElement at (1,2): ",element)

first_row=x[0]
print("\nFirst row: ", first_row)