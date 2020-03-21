def question():
    ans = input("are you at home?")
    return ans

while(True):
    z=question()
    if (z=="yes"):
        print("Good stay at home")
        break
    else:        
        print("Go to home")
        question()
