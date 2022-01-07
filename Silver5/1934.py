import math

n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    result = int((a*b) / math.gcd(a,b))
    print(result)