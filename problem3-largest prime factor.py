import sys
from math import sqrt

def prim(f):
    for i in range(2,int(f/2)+1):
        if(f % i ==0):
            return False
    return True

def fact(x):
    maxprime=0
    for i in xrange(2, int(sqrt(x)+1)):
        if(x%i==0):
            P=prim(i)
            if(i> maxprime and P):
                maxprime=i
            
    return maxprime

n=600851475143
print fact(n)



