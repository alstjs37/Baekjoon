import math

def is_prime(x) :
    if x == 1 :
        return False
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False
    return True

n = int(input())
l = list(map(int, input().split()))
array = []
for i in l :
    if is_prime(i) == True :
        array.append(i)

array = set(array)

result = 1
if len(array) == 0 :
    result -= 2
for i in array :
    result *= i
print(result)
