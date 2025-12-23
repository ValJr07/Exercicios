firstpha = input()
secondpha = input()
thirdpha = input()


v1=""
v2=""
v3=""
v4=""

l=[]
l.append(firstpha)
l.append(secondpha)
l.append(thirdpha)

for i in range(0,len(l)):
    v1+=l[i]
print(v1)

for i in range(0,len(l)):
    if i+1<len(l):
        l[i], l[i+1] = l[i+1], l[i]
        v2+=l[i]
    else:
        l[i], l[-1] = l[-1], l[i]
        v2+=l[i]
print(v2)

for i in range(0,len(l)):
    if i+1<len(l):
        l[i], l[i+1] = l[i+1], l[i]
        v3+=l[i]
    else:
        l[i], l[-1] = l[-1], l[i]
        v3+=l[i]
print(v3)

l.clear()
l.append(firstpha)
l.append(secondpha)
l.append(thirdpha)

for i in range(len(l)):
    for j in range(0,10):
        if j < len(l[i]):
            v4+=l[i][j]
        else:
            continue
print(v4)