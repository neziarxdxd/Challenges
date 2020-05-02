x = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20,20]
be= [j for j in set(x)  if x.count(j)>= 2 ]  
print(be)
