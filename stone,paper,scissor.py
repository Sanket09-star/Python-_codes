import random
import time


def com_fun():
    i = 1
    tie = 0
    cwin = 0
    pwin = 0
    n = int(input("How many Rounds, you wants to play : "))
    while i <= n:
        print("\n--------------------- Round ", i, "---------------------")
        print("\n\t1-Stone\n\t2-Paper\n\t3-Scissor")
        ch = int(input("Player-1 enter your choice : "))
        pc = random.randint(1, 3)
        print("Computer Selected : ", pc)
        ch1 = pc
        if ch == 1 and ch1 == 1 or ch == 2 and ch1 == 2 or ch == 3 and ch1 == 3:
            print("\tTie")
            tie = tie + 1
        elif ch == 1 and ch1 == 2 or ch == 2 and ch1 == 3 or ch == 3 and ch1 == 1:
            print("\n\tComputer is a winner")
            cwin = cwin + 1
        elif ch == 2 and ch1 == 1 or ch == 3 and ch1 == 2 or ch == 1 and ch1 == 3:
            print("\n\tPlayer-1 is a winner")
            pwin = pwin + 1
        else:
            print("\tInvalid Choice")
        i = i + 1
    time.sleep(1)
    print("\n\n\t\t\tScorecard\t\t\t")
    print("\t\tPlayer-1 win ==", pwin, "\n\t\tComputer win ==", cwin)
    if pwin > cwin:
        print("Player-1 is a winner")
    elif cwin > pwin:
        print("Computer is a winner")
    else:
        print("Match is Tie")


def dual_fun():
    i = 1
    tie = 0
    p2win = 0
    pwin = 0
    n = int(input("How many Rounds, you wants to play : "))
    while i <= n:
        print("\n--------------------- Round ", i, "---------------------")
        print("\t1-Stone\n\t2-Paper\n\t3-Scissor")
        ch = int(input("Player-1 enter your choice : "))
        ch1 = int(input("Player-2 enter your choice : "))
        if ch == 1 and ch1 == 1 or ch == 2 and ch1 == 2 or ch == 3 and ch1 == 3:
            print("\tTie")
            tie = tie + 1
        elif ch == 1 and ch1 == 2 or ch == 2 and ch1 == 3 or ch == 3 and ch1 == 1:
            print("\tPlayer-2 is a winner")
            p2win = p2win + 1
        elif ch == 2 and ch1 == 1 or ch == 3 and ch1 == 2 or ch == 1 and ch1 == 3:
            print("\tPlayer-1 is a winner")
            pwin = pwin + 1
        else:
            print("\tInvalid Choice")
        i = i + 1
    time.sleep(1)
    print("\n\n\t\t\tScorecard\t\t\t")
    print("\t\tPlayer-1 win ==", pwin, "\n\t\tPlayer-2 win ==", p2win, "\n\t\t\t\tTie ==", tie)
    if pwin > p2win and pwin > tie:
        print("Player-1 is a winner")
    elif p2win > pwin and p2win > tie:
        print("Player-2 is a winner")
    else:
        print("Match is Tie")


def main_main():
    print("\n\n*******************************\n\t1-Single Player Mod\n\t2-Dualplayer Mod\n\t3-Exit")
    mch = int(input("Enter Your choice : "))
    if mch == 2:
        dual_fun()
    elif mch == 1:
        com_fun()
    elif mch == 3:
        exit(0)
    else:
        print("\tInvalid Choice")
    print("\n\n*******************************\n")


main_main()
