t = int(input())

for _ in range(t) :
    floor = int(input())
    num = int(input())
    f0 = [i for i in range(1, num+1)]

    for _ in range(floor) :
        for i in range(1, num) :
            f0[i] = f0[i] + f0[i-1]
    print(f0[-1])