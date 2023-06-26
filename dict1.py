d = {}
i = 1
while i <= 5:
    s = input("Enter Student : ")
    age = int(input("Enter age of student  : "))
    d[s] = age
    i = i + 1
print(d)
for ele in d:
    d[ele] = d[ele]+1
print("Updated Dictionary : ", d)
