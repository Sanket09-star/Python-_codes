import random
ls = [1, 2, 2, 4, 5, 5, 2, 7, 7, 9, 4, 11, 7, 1, 3, 6]
ls2 = []
i = 1
while i <= 3:
    b = random.choice(ls)
    if ls2.count(b) == 0:
        ls2.append(b)
        i = i+1
print(ls)
print(ls2)
