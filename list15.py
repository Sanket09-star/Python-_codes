ls = [10, 20, 30, 40]
ls2 = [100, 200, 300, 400]
ls2.reverse()
i = 1
for ele in ls2:
    ls.insert(i, ele)
    i = i + 2
print(ls)
