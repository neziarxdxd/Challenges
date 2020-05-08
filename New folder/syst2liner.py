z = '3 -6 7'
w = '2 3 1'
x1,y1,c1 = list(map(int,z.split(' ')))
x2,y2,c2 = list(map(int,w.split(' ')))
print(x1,y1,c1)
print(x2,y2,c2)
if (-x1/y1,c1/y1) == (-x2/y2,c2/y2):
    print('Consistent and Dependent ')
elif (-x1/y1) == (-x2/y2):
    print('Inconsistent no_solution')
else:
    a1,a2 = (-x1/y1) , (c1/y1)
        
        
    root1=(-(y2 * a2) + c2)/(x2 + (a1*y2))
    root2= (-x1*root1/y1)+(c1/y1)
    print(a1,a2)
    print('Consistent and independent','x:',root1,'y:',root2)
