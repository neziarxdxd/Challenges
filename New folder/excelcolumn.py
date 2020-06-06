def printString(n):
   
   x= []
   while (n > 0):
      
      
      x.append(n%26)
      n = n//26

   print(x)
printString(26) 
printString(51) 
printString(52) 
printString(80) 
printString(676) 
printString(702) 
printString(705) 
