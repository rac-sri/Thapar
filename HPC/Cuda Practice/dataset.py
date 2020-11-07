import pandas as pd
import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

df = pd.DataFrame({"a" : a, "b" : b})
df.to_csv("dataset.csv", index=False)