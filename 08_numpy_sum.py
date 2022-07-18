import numpy as np
n1=np.array([1,2,3])
n2=np.array([4,5,6])
print(np.sum((n1,n2)))
print(np.sum((n1,n2),axis=0))
print(np.sum((n1,n2),axis=1))