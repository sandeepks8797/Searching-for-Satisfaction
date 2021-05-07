import numpy as np

t = int(input())

for _ in range(t):
    n = int(input())
    mat = [[0]*n]*n
    temp = 0
    
    for i in range(n):
        for j in range((i%2), n):
            mat[i][j] = temp
            j += 1
            temp += 1
    
    for x in range(n):
        for y in range((x+1)%2 ,n):
            mat[x][y] = temp
            y += 1
            temp += 1
    print(mat)

