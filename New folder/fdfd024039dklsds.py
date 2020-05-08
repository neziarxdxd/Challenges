import re
mystring="This is a sentence (once a day) [twice a day]"
regex = re.compile(".*?\([(.*?)]\)")
result = re.findall(regex, mystring)
print(result)
