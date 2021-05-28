t = int(input())

for i in range(t):

    n = int(input())
    temp = n

    while n != 0:
        n = temp & (temp - 1)
        temp -= 1

    print(temp)