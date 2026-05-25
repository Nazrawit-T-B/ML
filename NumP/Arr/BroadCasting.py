# When assigning values to indexed arrays, NumPy uses broadcasting to make the shapes compatible.

#NumPy can automatically expand smaller arrays to match larger ones during assignment by : 
# 1.Single value to multiple elements 
# 2. Small array to larger selection

#Only works when shapes are compatible 

import numpy as np 
x=np.arange(10)

x[2:5]=99

y=np.arange(10)
y[y%2==0]= -1 