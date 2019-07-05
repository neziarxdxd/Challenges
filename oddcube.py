num= [1,2,3,5,5,5]

    
try:
    print(sum([i**3 for i in num if i%2==1]))
except:
    print(None)