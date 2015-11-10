def longestCollatz(i):
    count=1
    x=i
    while(x>1):
        if(x%2==0):
            x=int(x/2)
        else:
            x=3*x+1
        count=count+1
        
    if(x==1):
        return count,i
max1=1
for i in range(1,10**6):
    count,x=longestCollatz(i)
    if(max1 < count):
        max1=count
        no=x
print no
    
    
