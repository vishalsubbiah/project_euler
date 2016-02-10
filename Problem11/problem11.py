import numpy as np

D= np.zeros((20,20))

data=open('input.txt','r+')
i=0
for d in data.readlines():
    j=0
    for dint in d.split():
        D[i,j]=int(dint)
        j=j+1
    i=i+1

maxvalue=0
for i in range(20):
    for j in range(20):
        if(i+3<=19):
            temp1=D[i,j]*D[i+1,j]*D[i+2,j]*D[i+3,j]
        else:
            temp1=0
            
        if(j+3<=19):
            temp2=D[i,j]*D[i,j+1]*D[i,j+2]*D[i,j+3]
        else:
            temp2=0
        
        if(i+3<=19 and j+3<=19):
            temp3=D[i,j]*D[i+1,j+1]*D[i+2,j+2]*D[i+3,j+3]
        else:
            temp3=0
       
        if(i-3>=0 and j+3<=19):
            temp4=D[i,j]*D[i-1,j+1]*D[i-2,j+2]*D[i-3,j+3]
        else:
            temp4=0
        temp=max(temp1,temp2,temp3,temp4)
        if(temp>maxvalue):
            maxvalue=temp
print maxvalue
