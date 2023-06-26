ls1 = [10, 20, 30, 40]
ls2 = [100, 200, 300, 400]
# combine these two lists into third list in opposite order -> ls3=[10,400,20,300,30,200,40,100]
ls3 = []
ls2.reverse()
i = 0
while i <= 3:
    ls3.insert(i, ls1[i])
    j = 0
    while j <= 3:
        ls3.insert(j + 1, ls2[j])

        j = j + 1
    i = i + 1

print(ls3)