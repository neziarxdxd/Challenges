'''
[1,1,1,2,3,2,5,5,6,6,7,8]
'''
'''
x= [1,1,1,2,3,2,5,6,7,5,5,7,81,1,8,1]
y = []
for i in x:
    if i not in y:
        y.append(i)
for j in y:
    if x.count(j) >=2:
        print(j)
'''

x = [1,1,1,2,3,2,5,6,7,5,5,7,81,1,8,1]
print([i for i in list(set(x)) if x.count(i)>=2])

