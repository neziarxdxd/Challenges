class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

f = open("demofile3.txt", "w")


for i in range(1,1001):
    
    
    f.write('''if(number=='''+str(i)+ '''){
    System.out.println("'''+str(py_solution().int_to_Roman(i))+ '''");
}\n'''
    )
f.close()

'''

SOURCE:
https://www.w3schools.com/python/python_file_write.asp

https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php


'''
