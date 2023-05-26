attempst=3
for i in range(3):
    input_pass=input("please input your password: ")
    if input_pass == "hello" :
        print("wellcome!")
        break
    else:
        attempst -= 1
        print(f"you have {attempst} left !")
        if attempst == 0:
            print("you entered wrong password for three times. you are banned ")
            break


