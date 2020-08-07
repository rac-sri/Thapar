import os
import numpy as np
from numpy import random

mat = random.randint(100,size=(10,10))

np.savetxt("matrix.txt",mat)