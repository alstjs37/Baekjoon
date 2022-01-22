n = int(input())

if n < 100 :
    print(n)
else :
    cnt = 0
    for i in range(100, n+1) :
        num = str(i)
        if 2 * int(num[1]) == int(num[0]) + int(num[2]) :
            cnt += 1
    print(99 + cnt)