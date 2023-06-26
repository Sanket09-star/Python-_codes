import random
a = int(input("How many players : "))
j = 1
while a >= j:
    print("Player-", j)
    j = j + 1
print("=============================================================================")
i = 1
while True:
    if a >= i:
        input("Press Enter for roll Dice")
        p1 = int(random.randint(1, 6))
        print("Player ", i, " rolled : ", p1)
        if p1 == 6:
            input("Press Enter for roll Dice")
            p1 = int(random.randint(1, 6))
            print("Player ", i, " rolled : ", p1)
            if p1 == 6:
                print("Player ", i, " win  ")
                break
            elif a >= 1:
                print("Player ", i, "Better luck next time\n")
                i = i + 1
            else:
                i = 1
        elif a >= i:
            i = i + 1
    else:
        i = 1
print("============================================================================")
