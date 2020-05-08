s1= 'abcde'
s2= 'aaaae'
x=set.intersection(set([i for i in s1]),set([i for i in s2]))
print(len(x))
