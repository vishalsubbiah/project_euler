for a in range(0,1000):
	for b in range(0,1000):
		csqr=(a**2)+(b**2)
		c=(pow(csqr,0.5))
		if(a+b+c==1000):
			print (a*b*c)	
