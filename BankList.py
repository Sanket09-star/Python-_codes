def check_acc():
    d = int(input("Enter Account number : "))
    t = acc.count(d)
    if t != 0:
        ind = acc.index(d)
        if d == acc[ind]:
            return [0, ind]
        else:
            print("Invalid Account Number")
            return [1]

    else:
        print("Invalid Account Number , account number not found")
        return [1]


def check_pin():
    d = int(input("Enter Your PIN : "))
    t = apin.count(d)
    if t != 0:
        ind = apin.index(d)
        if d == apin[ind]:
            return 0
        else:
            print("Invalid PIN")
            return 1
    elif t > 1:
        print("Duplicate PIN, PIN is already taken,make new pin")
        return 1
    else:
        print("Invalid PIN")
        return 1


def add_account():
    global n, b, p
    print("Add new account :----")
    n = int(input("Enter Account Number : "))
    b = int(input("Enter Initial Balance : "))
    p = int(input("Enter Initial PIN : "))
    acc.append(n)
    aba.append(b)
    apin.append(p)
    print("Account  successfully created")


def withdraw():
    w = check_acc()
    if w[0] == 0:
        w1 = check_pin()
        if w1 == 0:
            ind = w[1]
            wi = int(input("Enter amount to withdraw : "))
            aba[ind] = aba[ind] - wi
            print("Withdraw successful")
            print("New Balance is", aba[ind])


def pin_change():
    w = check_acc()
    if w[0] == 0:
        w1 = check_pin()
        if w1 == 0:
            ind = w[1]
            b1 = int(input("Enter Your new PIN : "))
            c1 = int(input("Re-Enter your new PIN : "))
            if b1 == c1:
                print("PIN successfully changed")
                apin[ind] = c1
            else:
                print("Previous PIN and New PIN doesn't Match")


def deposite():
    w = check_acc()
    if w[0] == 0:
        ind = w[1]
        damt = int(input("Enter Amount to deposite : "))
        aba[ind] = aba[ind] + damt
        print("Deposite sucessfull")
        print("New Balance is", aba[ind])


def check_balance():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            print("Balance : ", aba[ind])


def check_mini():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            if aba[ind] > 2000:
                print("Account Balanced is maintained")
                print("Balance : ", aba[ind])
            else:
                aba[ind] = aba[ind] - 20
                print("Account Balance is less than  MINIMUM required Balance Fine Rs.20")
                print("Balance : ", aba[ind])


def addinter():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            inte = (aba[ind] / 100) * 4
            intee = aba[ind] + inte
            print("Rs.", inte, "Credited as Interest.")
            print("New Balance is ", (aba[ind] + intee))


def show_info():
    a = check_acc()
    if a[0] == 0:
        b2 = check_pin()
        if b2 == 0:
            ind = a[1]
            print("Account Number : ", acc[ind])
            print("Balance : ", aba[ind])
            print("PIN : ", apin[ind])


def transfer_fund():
    a = check_acc()
    if a[0] == 0:
        print("Transfer to ---")
        a1 = check_acc()
        if a1[0] == 0:
            am = int(input("Amount to Transfer : -"))
            if am >= 1000:
                b2 = check_pin()
                if b2 == 0:
                    ind1 = a1[1]
                    ind = a[1]
                    aba[ind] = aba[ind] - am
                    print("Rs.", am, "sucessfull transfer to Account", ind1)
                    aba[ind1] = aba[ind1] + am
                    print("New Balanace of Account no.", acc[ind], "Rs.", aba[ind])
                    print("New Balance of Account no.", acc[ind1], "Rs.", aba[ind1])

            else:
                print("Insufficicent Balance, Minimum Balance required for transfering funds is Rs.1000 ")


acc = []
aba = []
apin = []
i = 1
while i <= 2:
    print("Accepting details of Account : ", i)
    n = int(input("Enter Account Number : "))
    b = int(input("Enter Initial Balance : "))
    p = int(input("Enter Initial PIN : "))
    acc.append(n)
    aba.append(b)
    apin.append(p)
    i = i + 1

while True:
    print()
    print("--------------------------------------------------------------------")
    print("Select an operation")
    print("1 - Add new Account")
    print("2 - Withdrawal")
    print("3 - Deposite")
    print("4 - PIN change")
    print("5 - Check Balance")
    print("6 - Check for MINIMUM balance")
    print("7 - Add Interest")
    print("8 - Transfer Funds")
    print("9 - Show Account Information")
    print("0 - EXIT")
    ch = int(input("Provide your choice -"))
    print()
    print("----------------------------------------------------------------------")
    if ch == 1:
        add_account()
    elif ch == 2:
        withdraw()
    elif ch == 3:
        deposite()
    elif ch == 4:
        pin_change()
    elif ch == 5:
        check_balance()
    elif ch == 6:
        check_mini()
    elif ch == 7:
        addinter()
    elif ch == 8:
        transfer_fund()
    elif ch == 9:
        show_info()
    elif ch == 0:
        exit(0)
