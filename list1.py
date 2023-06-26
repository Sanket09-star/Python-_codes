ls = []
i = 1
while i <= 9:
    ls.append([i, i + 1, i + 2])
    ls.append([i + i + 1 + i + 2])
    i = i + 3
print(ls)
