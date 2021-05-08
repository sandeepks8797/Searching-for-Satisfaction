import numpy as np

t = int(input())     #testcases

for i in range(t):
    #size of matrix n*n
    n = int(input())
    
    #matrix input
    m = input()

    mat = np.array(m).reshape(n,n)

    #count the no. of star points
    count = 0
    
    l = []   #array for storing co-ordinates
    for x in range(n):
        for y in range(n):
            if mat[x][y] == "*":
                l.append([x,y])
                count += 1
        if count == 2:
            break
    
    mat[l[1][0]][l[0][1]] = "*"
    mat[l[0][0]][l[1][1]] = "*"

    print(mat)
    