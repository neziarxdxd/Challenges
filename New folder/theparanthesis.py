'''Given a a rectangular matrix of characters, add a border of asterisks(*) to it.
Example
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output
[time limit] 4000ms (py)
[input] array.string picture
A non-empty array of non-empty equal-length strings.
Constraints:
1 ≤ picture.length ≤ 5,
1 ≤ picture[i].length ≤ 5.
[output] array.string
The same matrix of characters, framed with a border of asterisks of width 1.'''

picture =["abc",
           "ded"]
for i in range(len(picture)):
   picture[i] = "*"+picture[i]+"*"
   
picture.append("*"*(len(picture[0])))
picture.insert(0,"*"*(len(picture[0])))

print(picture)
