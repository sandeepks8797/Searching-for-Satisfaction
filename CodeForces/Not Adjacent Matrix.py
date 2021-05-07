n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i==2:
        print(-1)
        continue
    arr1= [[0 for i in range(i)] for j in range(i)]
    count=1
    for j in range(i):
        for k in range(j%2,i,2):
            arr1[j][k]=count
            count+=1
    for j in range(i):
        for k in range((j+1)%2,i,2):
            arr1[j][k]=count
            count+=1
    for j in range(i):
        print(arr1[j])