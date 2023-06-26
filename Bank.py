def checkaccnum():
    ac = int(input("Enter your account number -"))
    if ac == acnum:
        return 0
    else:
        print("Invalid Account number")
        return 1


def checkpin():
    p = int(input("Enter Your PIN - "))
    if p == pin:
        return 0
    else:
        print("Invalid PIN")
        return 1


def deposite():
    depo = int(input("Enter deposite amount -"))
    print("New balance is -", acbal + depo)
    return acbal + depo


def withdrawal():
    a1 = checkaccnum()
    if a1 == 0:
        b = checkpin()
        if b == 0:
            wit = int(input("Enter withdrawalabe Amount - "))
            print("New balance is - ", acbal - wit)
            return acbal - wit
        else:
            return acbal
    else:
        return acbal


def pin_change():
    a1 = checkpin()
    if a1 == 0:
        b = int(input("Enter Your new PIN"))
        c = int(input("Re-Enter your new PIN"))
        if b == c:
            print("PIN sucessfully changed")
            return c
        else:
            print("Previous PIN and New PIN doesn't Match")
    return pin


def show_bal():
    a1 = checkaccnum()
    if a1 == 0:
        b = checkpin()
        if b == 0:
            print("Bank Balance is - ", acbal)


def checkmini():
    if acbal < 2000:
        print("Account Balance is less than  MINIMUM required Balance")
        print("Fine is 20 Rs.")
        min1 = acbal - 20
        print("New Balance is - ", min1)
        return min1
    else:
        print("Account Balanced is maintained")
        return acbal


def addinter():
    intr = (acbal / 100) * 4
    intrr = acbal + intr
    print("Rs.", intr, "Credited as Interest.")
    print("New Balance is ", intrr)
    return intrr


def showdetails():
    print("Account Number : *****", (acnum % 1000))
    print("Account Balance : ", acbal)
    print("Account PIN :", pin)


acnum = int(input("Enter Account Number :  "))
acbal = int(input("Enter Initial Balance : "))
pin = int(input("Enter Initial PIN : "))
while True:
    print("Select an operation")
    print("1 - Deposite")
    print("2 - Withdrawal")
    print("3 - PIN change")
    print("4 - Show Balance")
    print("5 - Check for MINIMUM balance")
    print("6 - Add Interest")
    print("7 - Show Account Information")
    print("8 - EXIT")
    ch = int(input("Provide your choice -"))
    if ch == 1:
        bal = deposite()
        acbal = bal
    elif ch == 2:
        w4 = withdrawal()
        acbal = w4
    elif ch == 3:
        c2 = pin_change()
        pin = c2
    elif ch == 4:
        show_bal()
    elif ch == 5:
        c3 = checkmini()
        acbal = c3
    elif ch == 6:
        c1 = addinter()
        acbal = c1
    elif ch == 7:
        showdetails()
    elif ch == 8:
        exit(0)
