from multiprocessing import Process
import time
from numpy import random
import numpy as np

#  __init__ method you can initialize resource and by implementing Process.run() method you can write the code for the subprocess.

a=random.randint(100,size=(10,10))
b=random.randint(100,size=(10,10))

def subtract():
        print('subtract\n')
        print(np.subtract(a,b))
def multiply():
        print('multiply\n')
        print(np.multiply(a,b))

def add():
        print('add\n')
        print(np.add(a,b))

def divide():
        print('divide\n')
        print(np.divide(a,b))
    


  
if __name__ == '__main__': 

    p = Process(target=add) 
    p.start() 
    p.join() 
    p2 = Process(target=subtract) 
    p2.start() 
    p2.join() 
    p3 = Process(target=multiply) 
    p3.start() 
    p3.join() 
    p4 = Process(target=divide()) 
    p4.start() 
    p4.join() 
    
    