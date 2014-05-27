a=[1,2]
sum1=0
for i in range(0,10**6):
    
    if(a[0]<=4000000 and a[0]%2==0):
        sum1=sum1+a[0]
    temp=a[0]+a[1]
    a[0]=a[1]
    a[1]=temp
print sum1
