import time
import numpy as np
from numpy import random

t0 = time.time()

mat1 = random.randint(100 , size=(2000,2000))
mat2 = random.randint(100, size=(2000,2000))

result = np.multiply(mat1,mat2)

print(result)

t1 = time.time()
print(t1-t0)