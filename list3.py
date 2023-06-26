ls = []
s = []
num = 1
i = 0
while i <=2:
  ls.append([])
  while True:
    ls[i].append(num)
    if num % 3 == 0:
       num = num +1
       break
    num = num + 1
  i = i + 1
print (ls)