x=["abc", 
 "eeee", 
 "abcd", 
 "dcd"]
a =max([len(i)for i in x])
print([i for i in x if a == len(i)])
