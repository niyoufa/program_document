import scipy as sp 
import time 

def create_id(): 
  return time.time() + sp.rand() 

if __name__ == "__main__": 
  id = create_id() 
  print id
