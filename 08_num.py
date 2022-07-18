# NUMPY ---> TWO TYPES
# 1---> SINGLE DIMENSIONAL ARRAY
# 2 ---> MULTI - DIMENSIONAL ARRAY

# FIRST WE USE SINGLE DIMENSIONAL ARRAY
import numpy as np
from functools import reduce
n1=np.array([1,2,3,4,5,6,7,8,9])
#SINGLE DIMENSIONAL ARRAY
print(n1)

n2=np.array([[11,22,33,44],[99,88,77,66]])
# MULTI DIMENSIONAL ARRAY
print(n2)
sum=(reduce(lambda x,y: x*y,n2))
print(sum)