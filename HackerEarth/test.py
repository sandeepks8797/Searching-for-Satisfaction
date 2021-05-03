n = int(input())
l = []
for i in range(n):
    s = str(input())
    if len(s) > 10:
        s = s[0] + str(len(s)-2) + s[-1]
        l.append(s)
    else:
        l.append(s)

for i in l:
    print(i)