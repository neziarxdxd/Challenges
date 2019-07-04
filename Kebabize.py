word = "AbfdfdAcsddd"
new= [] 
old= []
for i in word:     
    if i.isupper():
        new.append(i)
    else: 
        old.append(i)
print(new)
print(old)
