x = [[1,2,3],
     [4,5,6],
     [7,7,8]]
j=0
for i in range(len(x)):
    for j in range(i+1):
        if i > j:
            print(i,j)
        else:
            print(i,j)
    print("----------")
