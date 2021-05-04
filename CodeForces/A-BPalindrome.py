t = int(input())
for i in range(t):

    a,b = map(int,input().split())
    s = input()
    a1 = a
    b1 = b
    n = a + b
    count = 0
    k = 0
    bin_no = 1
    count_ones = 0
    count_zeros = 0
    for j in range(n):
        if s[j] == "?":
            count+=1
        elif s[j] == "0":
            count_zeros += 1
        elif s[j] == "1":
            count_ones += 1
    if count%2 != 0 and count == (a + b):
        print(-1)
        break

    while a!=0 or b!=0:
        if s[k] != s[n-1-k]:
            print(-1)
            break

        elif s[k] == s[n-1-k] and s[k] != "?":
            a -= 1
            b -= 1
            k += 1
            continue

        elif s[k] == "?" and s[n-1-k] == "?":
            if count_ones <= count_zeros:
                bin_no = 1
                count_ones += 2
            else:
                bin_no = 0
                count_zeros += 2
            s[k] = str(bin_no)
            s[a+b-1+k] = str(bin_no)
            a -= 1
            b -= 1
            k += 1
        else:
            if s[k] == 0:
                s[n-1-k] = s[k]
                count_zeros += 1
                
            elif s[k] == 1:
                s[n-1-k] = s[k]
                count_ones += 1
    
            elif s[n-1-k] == 0:
                s[k] = s[n-1-k]
                count_zeros += 1 
                
            elif s[n-1-k] == 1:
                a[k] = s[n-1-k]
                count_ones += 1
            a -= 1
            b -= 1
            k += 1

    if a1 != count_zeros or a1 != count_ones:
        print(-1)
    elif  a1 == count_zeros and b1 == count_ones:
        print(s)