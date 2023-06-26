la = [1, 2, 3, 4, 5]
i = 1
j = 1
while i <= 5 or j <= 5:
    la.insert(i, j * j)
    i = i + 2
    j = j + 1
print(la)
