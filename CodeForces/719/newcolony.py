t = int(input())

for i in range(t):


    n, k = map(int, input().split())

    arr = list(map(int,input().split()))
    
    while(k!=0):
        count = 1
        for j in range(n-1):
            if arr[j] >= arr[j+1]:
                count += 1
            if arr[j] < arr[j+1] :
                arr[j] += 1
                k -= 1
                loc = j + 1
                break
        if k != 0 and count == n:
            break
    if k>0:
        print(-1)
    else:
        print(loc)
