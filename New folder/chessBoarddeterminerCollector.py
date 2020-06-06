def cK(a):
   evOd= ((ord(a[0])-64) % 2 == 1) and ((ord(a[1])-64) % 2 == 1)
   same= (ord(a[0])-64) == int(a[1])
   if (evOd or same) :
      
      return ("black")
   else:
      return ("white")

print(cK("B2"))
      
