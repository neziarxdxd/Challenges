x ="qq-q"
y= []
if x[0].isdigit():
   y.append(1)
else:
   print("there is no digit in first")
   for i in x:     
      if (not(i.isdigit() or i.isalpha() or i=="_")):         
         y.append(1)
print(y)
         
