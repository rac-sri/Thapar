import numpy as np
import random
import time

t=time.time()
x=[[random.randint(1,100) for i in range(2000)] for j in range(2000)]
y=[[random.randint(1,100) for i in range(2000)] for j in range(2000)]

print(np.add(x, y))
print(np.subtract(x, y))
print(np.divide(x, y))
print(np.linalg.inv(x))
print(np.linalg.inv(y))
print(np.dot(x,y))

print(time.time()-t)