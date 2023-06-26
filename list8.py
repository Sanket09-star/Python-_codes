la = ["abc", "xyz", "aba", "1221", "xyzx", "92519", "MtM"]
ll = []
count = 0
for ele in la:
    b = len(ele)
    # print(ele)
    if 3 == b:
        ll.extend(ele)
        i = 0
        while i <= 2:
            if ll[0] == ll[2]:
                print(ll)
                count = count + 1
                break
            else:
                i = i + 1
        ll.clear()
print(count)
