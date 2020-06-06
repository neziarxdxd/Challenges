x = "1"
point= []
x = x.split('.')
if not(len(x) ==4):
   point.append('b')
for i in x:   
   if i.isdigit():
      if int(i) > 255:      
         point.append(1)
      elif not(len(i)==1):
         if i[0] == "0":
            point.append('x')    
         
   else:
      point.append(1)
print(len(point) ==0)
