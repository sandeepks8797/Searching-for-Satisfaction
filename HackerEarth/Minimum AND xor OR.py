import sys
T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    min_value = sys.maxsize
    for j in range(len(A) - 1):
        for k in range(j+1,len(A)):
            temp = ((A[j] and A[k]) ^ (A[j] or A[k]))
            if temp < min_value:
                min_value =  temp
    print(min_value)  