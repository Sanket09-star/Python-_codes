import random
scores = [0, 1, 2, 3, 4, 6, 'W']
d = {}
n = int(input("Enter How many players will play cricket : "))
i = 1
while i <= n:
    p = input("Enter Player Name : ")
    d[p] = []
    i = i + 1
for ele in d:
    summ = 0
    print(ele, " on strike")
    while True:
        c = random.choice(scores)
        d[ele].append(c)
        if c == 'W':
            print("OUT")
            break
        else:
            print(c, "Run")
            summ = summ + c

    print("Total score is -", summ)
    d[ele].append(["Total score -", summ])

print(d)
