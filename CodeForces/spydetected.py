t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    a = arr[0]
    b = arr[1]
    if a == b:
        for j in range(1,len(arr)-1):
            if arr[j] != arr[j+1]:
                print(j+2)
                break
    else:
        if a == arr[2]:
            print(2)
        else:
            print(1)
            
