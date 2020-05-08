T = int(input())
for x in range(1, T + 1):
    N= map(int, input().split())
    H= list(map(int, input().split()))
    b = int(sum(H)/len(H))
    y= 0
    for i in H:
        print(i,b)
        if i>b:
            y+=1
        
    
    
    
    
    
    print("Case #{}: {}".format(x, y), flush = True)
