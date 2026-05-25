import numpy as np 

q=np.zeros((2,2))
w=np.ones((2,2))
e=np.eye(2)*2
r=np.diag((-3,-4))

block_matrix=np.block([[q,w],[e,r]])
print("\nBlock matrix: ")
print(block_matrix)