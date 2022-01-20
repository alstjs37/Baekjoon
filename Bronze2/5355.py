from tokenize import Double


n = int(input())

j = 0
while j < n :
    l = list(input().split())
    result = 0
    result += float(l[0])

    for i in l :
        if i == "@" :
            result *= 3
        elif i == "%" :
            result += 5
        elif i == "#" :
            result -= 7
    print(format(result, ".02f"))
    j += 1