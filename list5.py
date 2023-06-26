ls=[]
i=0
l=1
while i<=3:
	j=0
	ls.append([])
	while j<=1:
		k=j+2
		ls[i].append([])
		while k:
			k-=1
			ls[i][j].append(l)
			l+=1
		j+=1
	i+=1
print(ls)