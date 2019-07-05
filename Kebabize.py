x=['a', 'a', 'b', 'b', 'b']

words ={}
for i in x: 
    words[i] = words.get(i,0)+1
print(words)
