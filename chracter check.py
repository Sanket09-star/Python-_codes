i = 1
while i <= 4:
    inn = input("Enter a character : ")
    a = ord(inn)
    if (a >= 65) and (a <= 90):
        print("Character is in Uppercase : ", inn)
    elif (a >= 97) and (a <= 122):
        print("Character is in Lowercase : ", inn)
    elif (a >= 48) and (a <= 57):
        print("Character is in Digit : ", inn)
    else:
        print("Character is in Special Symbol : ", inn)
    i = i + 1
