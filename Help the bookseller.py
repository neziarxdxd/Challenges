'''
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")

'''
result =[]
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B","C"]
for C in c:
    x= list(filter(lambda x: x.startswith(C), b))
    result.append("("+C+" : "+str(sum([ int(j.split()[1]) for j in x])) +")")
        
print(" - ".join(result))
        

        
        

