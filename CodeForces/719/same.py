t = int(input())

for i in range(t):

    n = int(input())

    arr = list(map(int,input().split()))

    dic = {}
    count = 0


    for j in range(n):
        diff = arr[j] - j
        if diff in dic:
            dic[diff] += 1
        else:
            dic[diff] = 1
    
    
    for j in dic:
        if dic[j] >= 2:
            count += ((dic[j]) * (dic[j]-1)) // 2
    
    print(count)