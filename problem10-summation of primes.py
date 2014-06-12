def prim(x):
	for i in range(2, int(x/2)+1):
		if(x%i!=0):
			pass
		else:
			return False
	return x

i=2
sum1=0
while(i<2*(10**6)):
    if(prim(i)!=False):
        sum1=sum1+i
        print sum1
    i=i+1

print sum1
