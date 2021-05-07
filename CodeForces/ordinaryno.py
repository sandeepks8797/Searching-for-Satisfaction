t = int(input())

for i in range(t):

    n = int(input())
    count = 0

    for j in range(1,10):
        x = 0
        for k in range(1,11):
            x = x*10 + j
            if x <= n:
                count += 1
    print(count)

