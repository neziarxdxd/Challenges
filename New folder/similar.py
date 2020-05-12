a= [2, 3, 9]
b= [10, 3, 2]
a_table = []
b_table =[]
for i in b:
   if i in a:
      b_table.append(True)
   else:
      b_table.append(False)
for i in a:
   if i in b:
      a_table.append(True)
   else:
      a_table.append(False)
      
print(a_table,b_table)
print(not((False in a_table) or (False in b_table)))
