	

def prim(x):
	for i in range(2, int(x/2)+1):
		if(x%i!=0):
			pass
		else:
			return False
	return x
i=5
count=2
while(count<10001):
	t=prim(i)
	if(t!=False):
		count=count+1
	i=i+1

print t
