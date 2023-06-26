ls = [1, 3, 3, 7, 2, 1, 5, 8, 3, 1]
x = []
val = None
for i in ls:
    if i != val:
        x.append(i)
        val = i
print(x)
