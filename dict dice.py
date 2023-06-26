import random
d = {}
i = 1
while i <= 4:
    name = input(print("Enter Your Name : "))
    d[name] = []
    i = i + 1
print(d)
f = 1
while f <= 1:
    for ele in d:
        print(ele, "Play Your Turn ")
        # input("Press Enter to roll the dice")
        player = int(random.randint(1, 6))
        print(player)
        d[ele].append(player)
        if player == 6:
            # input(print("Owo, You got 6 , Press enter to roll the dice"))
            player = int(random.randint(1, 6))
            d[ele].append(player)
            print(player)
            print("-------------------------------------------------------------")
            if player == 6:
                print(ele, "-you are the winner")
                print(ele, "your score is ", sum(d[ele]))
                f = 2
                break
            else:
                print(ele, "Ohhh,Better luch next time")
                print("-------------------------------------------------------------")
print()
print("-------------------------------------------------------------")
for ele in d:
    print("All Player total scores are .....")
    print(ele, "--", d[ele], "--", sum(d[ele]))
