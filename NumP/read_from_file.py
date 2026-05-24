#NumPy excels at this because it efficiently reads large datasets and automatically converts them into appropriate numerical formats. 
import numpy as np 

try:
    data=np.loadtxt('NumP\data.csv',delimiter=",",skiprows=1)
    print("Data loaded from data.csv: ")
    print(data)
except IOError:
    print("Error: data.csv not found.")