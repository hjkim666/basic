import numpy as np 

def getMatrix(a):
    if a > 0 & a%3 == 0:
        tmp = np.arange(a)
        tmp = tmp.reshape(int(a/3),3)
    else: 
        tmp  = 0 
    return tmp

if __name__ == '__main__':
    a = input('one number:')
    print(getMatrix(int(a)))   
    
      