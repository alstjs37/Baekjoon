import math

def is_prime_number(x) :
    if x == 1 :
        return True
    for i in range(2, int(math.sqrt(x))+1) :
        if x % i == 0 :
            return False
    return True

m = int(input())
n = int(input())
array = []

for i in range(m,n+1) :
    if is_prime_number(i) == True :
        array.append(i)

if len(array) == 0 :
    print(-1)
else :
    print(sum(array))
    print(min(array))