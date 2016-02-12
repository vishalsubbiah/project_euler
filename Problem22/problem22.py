data = open('p022_names.txt', 'r+')
names=data.read().replace('"','').split(',')
value={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
names.sort()
names_count=len(names)
total_value=0
for i in range(names_count):
    word_value=0
    for j in names[i]:
        word_value=word_value + value[j]
    total_value=total_value+((i+1)*word_value)
print total_value
