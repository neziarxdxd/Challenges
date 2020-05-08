def howMany(total, collected):
    x=((collected * -50)+total)/50
    y = collected -x
    return ("adult:",int(x),"students:",int(y))

T = int(input())
for i in range(1,T+1):
    
    print(howMany(*list(map(int, input().split()))))

             
