import random
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ls2 = []
i = 1
while i <= 3:
    b = random.choice(ls)
    ls2.append(b)
    i = i+1
print(ls)
print(ls2)
