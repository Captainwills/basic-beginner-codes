count = 5
passkey = 'Jason47'
while count > 0:
    password = input("please enter password: ")
    if password == passkey:
          print("successful\n vault unlock")
          continue
    elif count == 1:
          print("You have exceeded entry limit..\n You are barred!")
          break

    else:
        print("try again " + "you have" , count-1, " entry left")
        count -= 1


