
# import the necessary library 
import numpy as np 
  
# create a dummy array 
arr = np.arange(1,11) 
  
# display the array 
print(arr) 
  
# use the tofile() method  
# and use ',' as a separator 
# as we have to generate a csv file 
arr.tofile('data2.csv', sep = ',')