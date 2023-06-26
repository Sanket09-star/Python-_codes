i = 0
num = 1
ls = []
while num<100:
  ls.append([])
  j = 0
  while True:
    ls[i].append([])
    ls[i][j] = num
    j = j + 1
    if num % 5 == 0:
      num = num +1
      break
    num = num + 1
  i = i + 1
print(ls)