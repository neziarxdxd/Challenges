def decompose(number):
   y=[]
   for i in range(len(number),0,-1):
      if int(number[len(number)-i]) !=0:
         y.append(str(int(number[len(number)-i])*(10**(i-1))))
   print("+".join(y))
x=[]
for i in range(4):
   x.append(input())

for i in x:
   decompose(i)

