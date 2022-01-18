def fac(x) :
    result = 1
    for i in range(1, x+1) :
        result *= i
    return result

n, k = map(int, input().split())

result = fac(n) / (fac(n-k) * fac(k))
print(int(result))