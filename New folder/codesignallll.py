x = "www.xakep.ru"
x = x.split('.')
x.remove('www')
print(x)



'''nC= 16
nR = 11
c =5
r = 3

x = (nR-r)* (nC-(c-1))
print((nR-r),(nC*c-1))
print(x)
'''

'''
def centuryFromYear(year):
    if (year-(int(year/100)*100)>0):
        return (int(year/100))+1
    else:
        return (int(year/100))


print(centuryFromYear(2025))
'''
'''
inputArray = [3, 6, -2, -5, 7, 3]
print(max([(inputArray[i]*inputArray[i+1]) for i in range(len(inputArray)-1)]))
'''

'''
statues =  [6, 2, 3, 8]
statues.sort()

print((abs(sum([(statues[i]-statues[i+1]+1) for i in range(len(statues)-1)]))))
'''
'''
n= 25
print(sum([int(i) for i in str(n)]))
'''
