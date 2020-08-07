import numpy as np
from numpy import random
import time

t=time.time()
x=random.randint(100,size=(10,10))
y= random.randint(100,size=(10,10))


print(np.add(x, y))
print(np.subtract(x, y))
print(np.divide(x, y))
print(np.linalg.inv(x))
print(np.linalg.inv(y))
print(np.dot(x,y))

print(time.time()-t)