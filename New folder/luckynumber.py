x = [-1,5,3,2,-1,1,5,2]
position=[]
for i in range(len(x)):
   if x[i] == -1:
      position.append(i)
y= []
for j in x:
   if j !=-1:
      y.append(j)
x = sorted(y)
for p in position:
   x.insert(p,-1)
print(position)
print(x)
