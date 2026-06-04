import pandas as pd

data = [10,20,30,40,50]
s = pd.Series(data)

print ("\nData type: ",s.dtype)
print ("\nSize: ", s.size)

print ("The full series Array")
print ("\nThe First Element: ",s[0])
print ("Slicing ", s[1:3])