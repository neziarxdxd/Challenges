hi = "abcd"
print(hi[0:2])


'''

s = "abcd"
print("-".join([(s[i]*(i+1)).capitalize() for i in range(len(s))]))




likes = ['Peter']

if len(likes) >=4:
    print("{}, {} and {} others like this".format(likes[0],likes[1],len(likes)-2))
elif len(likes) == 3:
    print("{}, {} and {} like this".format(likes[0],likes[1],likes[2]))
elif len(likes) == 2:
    print("{} and {} like this".format(likes[0],likes[1]))
elif len(likes) ==1:
    print("{} likes this".format(likes[0]))
else:
    print("no likes this")

    

num1 = '19 1 21 1 1 45 49 25 50 35 35 1 17 1 29 1 29 35 13'
num2 = "5 7 20 11 9"
num1=num1.split(" ")
print(num1)


x= [int(i)%2 for i in num1]
print(x)
if (x).count(1) == 1:
    print(x.index(1)+1)
else:
    print(x.index(0)+1)



def narcissistic( value ):
    return value==sum([int(i)**len(str(value)) for i in str(value)])


'''
