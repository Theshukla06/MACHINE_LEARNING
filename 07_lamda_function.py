# l=lambda x : x*x*x
# print(l(5))

#LAMBDA WITH FILTER


# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=list(map(lambda x: x*2,l1))
# print(l2)

from audioop import mul
from functools import reduce


l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
sum=(reduce(lambda x,y: x+y,l1))
print(sum)

mul=(reduce(lambda x,y: x*y,l1))
print(mul)
