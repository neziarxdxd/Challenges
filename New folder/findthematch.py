s1= "aabcc"
s2= "adcaa"
s1 = list(s1)
s2 = list(s2)
c=0
for i in range(len(s1)):
   if s1[i] in s2:
      
      s2.remove(s1[i]) 
      
      c +=1
print("Count",c)
print(s1)
print(s2)
      

   
      
