import random
while True:
    p1 = int(random.randint(1, 6))
    print("Player-1 rolled : ", p1)
    if p1 == 6:
        print("Player-1 you have another chance, Game point")
        p1 = int(random.randint(1, 6))
        print(p1)
        if p1 == 6:
            print("Wew!!Player-1 got : ", p1)
            print("Player-1 win")
            break
        else:
            print("Better luck next time\n")
    else:
        p2 = int(random.randint(1, 6))
        print("Player-2 rolled : ", p2)
        if p2 == 6:
            print("Player-2 you have another chance, Game point")
            p2 = int(random.randint(1, 6))
            print(p2)
            if p2 == 6:
                print("Wew!!Player-2 got : ", p2)
                print("Player-2 win")
                break
            else:
                print("Better luck next time\n")
