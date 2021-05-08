t = int(input())

for i in range(t):

    a,b = map(int, input().split())
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(a, a*b, (a*b + a))