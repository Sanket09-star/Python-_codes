import random
import time
all_times = []
p = int((input("Enter how many players : ")))
player = 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ops = ["+", "-", "*", "/"]
while player <= p:
    print("Player :-", player)
    q = 1
    start_time = time.perf_counter()
    while q <= 2:
        a = random.choice(nums)
        b = random.choice(nums)
        o = random.choice(ops)
        oans = eval(str(a) + o + str(b))
        print(a, o, b)
        print("Enter Your Answer -")
        uans = int(input())
        if oans == uans:
            print("Correct")
        else:
            print("Try Again")
        q = q + 1
    end_time = time.perf_counter()
    print("Player", player, "takes Time = ", end_time-start_time)
    all_times.append((end_time - start_time))
    player = player + 1
