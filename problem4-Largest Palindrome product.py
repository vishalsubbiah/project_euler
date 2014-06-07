def palin_check(n):
	n_s=list(str(n))
#	print len(n_s)
	for i in range(0,int(len(n_s)/2)):
		if(n_s[i]==n_s[len(n_s)-i-1]):
			pass
		else:
			return False
	return n

for i in range(901,1000):
	for j in range(901,1000):
		t=palin_check(i*j)
		if(t!=False):
			x=t
print x
#print palin_check(101)		
