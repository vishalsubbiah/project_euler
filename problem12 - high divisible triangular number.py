from math import *
def trinumb(n):
    return n*(n+1)/2
    
def factors(N):
    fact=[]
    for i in xrange(1, int(sqrt(N+1))):    
        if(N%i==0):
            fact.append(i)
            fact.append(N/i) 
    return fact
n=16 

while(n>0):
    factlen1=len(factors(trinumb(n)))
    if(factlen1 > 500):
        print trinumb(n)
        n=-1
    else:
        n=n+1
        print factlen1
