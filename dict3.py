d = {}
num = 1
while num <= 10:
    d[num] = []
    i = 1
    while i <= 10:
        m = num * i
        d[num].append(m)
        i = i + 1
    num = num + 1
print(d)
