d = {}
c = []
i = 1
while i <= 5:
    s = input("Enter Student : ")
    age = int(input("Enter age of student  : "))
    d[s] = age
    i = i + 1
print(d)
for ele in d:
    if d[ele] < 15:
        c.append(ele)
# print(c)
for ele1 in c:
    d.pop(ele1)
c.clear()
print("Updated Dictionary : ", d)
