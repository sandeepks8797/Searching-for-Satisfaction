t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    l = []
    l.append(s[0])
    count = 0

    for j in range(n-1):

        if s[j] == s[j+1]:
            continue

        if s[j] != s[j+1] and (s[j+1] not in l):
            l.append(s[j+1])
            continue

        if s[j] != s[j+1] and (s[j+1] in l):
            print("NO")
            count += 1
            break
    if count == 0:
        print("YES")