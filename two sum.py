x = [12,10,8,2,6]
y = 20

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if ((x[i]+ x[j])==y):
            print(x[i], x[j])
    

