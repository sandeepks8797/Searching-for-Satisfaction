import numpy as np

t = int(input())

for _ in range(t):
    n = int(input())
    mat = [[0 for i in range(n)] for j in range(n)]
    temp = 1
    
    for i in range(n):
        for j in range((i%2), n, 2):
            mat[i][j] = temp
            temp += 1
    
    for x in range(n):
        for y in range((x+1)%2 ,n, 2):
            mat[x][y] = temp
            temp += 1
    print(mat)

