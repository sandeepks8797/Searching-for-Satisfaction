t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int,input().split()))

    temp = min(arr)
    count = 0
    for j in arr:
        if temp < j:
            count += 1

    print(count)