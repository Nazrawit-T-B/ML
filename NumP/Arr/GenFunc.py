import numpy as np 

data = np.genfromtxt('my_data.csv',
                     delimiter=",",
                     skip_header=1,
                     missing_values='NA',
                     filling_values=0,
                     usecols=(1,2),
                     dtype=float)

#the numpy.genfromtxt() function is used to read data from a text file, with the ability to handle missing values and different data types. It returns a numpy array containing the data from the file.

# the functions mist basic usage requires one argument: the path to the data source.

print (data)