a=[1,2,3]
b=[]
for i in range(len(a)):
    b.append(a[i])
b[2]=0

print(a,b)