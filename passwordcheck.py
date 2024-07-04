pasw = input()

def passcheck(password):
    length = len(password)
    up = 0
    low = 0
    special = 0
    digits = 0

    if(length<6):
        print("password not strong")
        print("password must have at least 6 characters")
    else:
        for i in range(0,length):
            if password[i].isupper():
                up+=1
            elif password[i].islower():
                low+=1
            elif password[i].isdigit():
                digits+=1
            else:
                special+=1

        if (up != 0 and low != 0 and digits != 0 and special != 0):
            print("password is strong")
        else:
            print("password not strong")
            if (up == 0):
                print("Password must contain at least one uppercase character!\n")
            if (low== 0):
                print("Password must contain at least one lowercase character!\n")
            if (special== 0):
                print("Password must contain at least one special character!\n")
            if (digits == 0):
                print("Password must contain at least one digit!\n")



passcheck(pasw)