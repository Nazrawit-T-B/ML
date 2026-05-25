# View is a different way of looking at the same data in memory . When you create a view you are not creating a new array, you're just creatinf a new reference to the existing data
# Copy creates a completely new array in memory with its own data.

#views are memory efficient , fast but they can cause unexpected side effects. Copies are safer

import numpy as np 
a=np.arange(1,5)
print("\nOriginal Array 'a': ",a)
b=a[:2]
b[0]=99
print("Modified view 'b': ",b)
print("Array 'a' after modifying the view", a)
c = a[:2].copy()
c[0] = 0 # Modify the copy
print("\nModified copy 'c':", c)
print("Array 'a' after modifying the copy:", a)