count = 5
passkey = 'Jason47'
while count > 0:
    password = input("please enter password: ")
    if password == passkey:
        print("sucessful\n vault unlock")
        break
    else:
        print("try again " + "you have" , count-1, " entry left")
        count -= 1

