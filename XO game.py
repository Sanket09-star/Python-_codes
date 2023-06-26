def display():
    global a, i, j
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            print(a[i][j], end=" ")
            j += 1
        print()
        i += 1


def check():
    global a
    if a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X':
        print("player 1 is winner")
        return True
    elif a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X':
        print("player 1 is winner")
        return True
    elif a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X':
        print("player 1 is winner")
        return True
    elif a[0][0] == 'O' and a[0][1] == 'O' and a[0][2] == 'O':
        print("player 2 is winner")
        return True
    elif a[1][0] == 'O' and a[1][1] == 'O' and a[1][2] == 'O':
        print("player 2 is winner")
        return True
    elif a[2][0] == 'O' and a[2][1] == 'O' and a[2][2] == 'O':
        print("player 2 is winner")
        return True
    elif a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
        print("Player 1 is winner")
        return True
    elif a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
        print("Player 2 is winner")
        return True
    elif a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X':
        print("Player 1 is winner")
        return True
    elif a[0][1] == 'O' and a[1][1] == 'O' and a[2][0] == 'O':
        print("Player 2 is winner")
        return True


a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
i = 0
while i <= 2:
    j = 0
    while j <= 2:
        print(a[i][j], end=" ")
        j += 1
    print()
    i += 1


f = 0
i = 0
p = 1
while i <= 9:
    if p == 1:
        print("Player", p, "Symbol(X)")
        p += 1
    else:
        print("Player", p, "Symbol(O)")
        p -= 1
    n = input("Enter Number : ")
    sy = input("Enter Your symbol : ")
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            if a[i][j] == n:
                a[i][j] = sy
                display()
            j += 1
        print()
        b = check()
        if b is True:
            f = 1
            break
        else:
            i += 1
    if f == 1:
        break
    else:
        i += 1
