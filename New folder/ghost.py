num = [
   [1],
   [0],
   [5],
   [6],
   ]
x = len(num[0])
y = len(num)
for j in range(y):
   for i in range(x):
      if num[j][i] == 0:
         for b in range(j,y):                                    
            num[b][i]=0

return( sum(sum(i) for i in num))


       


