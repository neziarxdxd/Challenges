import math

term = ['math.sqrt', 'math.pi', 'math.sin', 'math.cos', 'math.tan', 'math.log', 'math.log', 
'math.pow', 'math.cosh', 'math.sinh', 'math.tanh', 'math.sqrt', 'math.pi', 'math.radians', 
'math.e', 'math.radians']



replace_val = ['√', 'π', 'sin', 'cos', 'tan', 'log', 'ln', 'pow', 'cosh', 'sinh', 'tanh', 
'sqrt', 
'pi', 'radians',
       'e', 'rad']


re_write = []
equation = "x + √(4)"
for e in equation:
   if e in replace_val:
      re_write.append(e.replace(e,term[replace_val.index(e)]))
      
   else:
      re_write.append(e)
full_equation="".join(re_write)
print((full_equation))
