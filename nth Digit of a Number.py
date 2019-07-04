def find_digit(x,loc):

    if loc>0:
       
        if loc<=len(str(abs(x))):
            x=(str(abs(x))[::-1])
            return(int(x[loc-1]))
        else:
            return(0)
    else:
        return(-1)






print("The Digit is : ",find_digit(5673, 4))
print("The Digit is : ",find_digit(129, 2))
print("The Digit is : ",find_digit(-2825, 3))
print("The Digit is : ",find_digit(0, 20))
print("The Digit is : ",find_digit(65, 0))
print("The Digit is : ",find_digit(24, -8))
print("The Digit is : ",find_digit(-1234, 2))
print("The Digit is : ",find_digit(-5540, 1))
print("The Digit is : ",find_digit(678998, 0))
print("The Digit is : ",find_digit(-67854, -57))
print("The Digit is : ",find_digit(0, -3))  




'''
Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).

Note
If num is negative, ignore its sign and treat it as a positive value
If nth is not positive, return -1
Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
Examples
findDigit(5673, 4)     returns 5
findDigit(129, 2)      returns 2
findDigit(-2825, 3)    returns 8
findDigit(-456, 4)     returns 0
findDigit(0, 20)       returns 0
findDigit(65, 0)       returns -1
findDigit(24, -8)      returns -1


'''