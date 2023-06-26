s = "aurangabad"
ls = []
ls.extend(s)
print(ls)
i = 0
j = 1
while i <= 10 or j <= 10:
    ls.insert(i, j)
    j = j+1
    i = i+2
print(ls)
