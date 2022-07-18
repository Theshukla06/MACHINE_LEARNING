import numpy as np
n1=np.array([1,2,3])
n2=np.array([4,5,6])
print(np.vstack((n1,n2)))


n3=np.array([1,2,3])
n4=np.array([4,5,6])
print(np.hstack((n3,n4)))


n5=np.array([1,2,3])
n6=np.array([4,5,6])
print(np.column_stack((n5,n6)))