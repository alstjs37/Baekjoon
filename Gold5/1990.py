import math

def is_palindrom(x) :
    x = str(x)
    if x == x[::-1] :
        return True

def is_prime_number(x) :
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False
    return True

a, b = map(int, input().split())
if b > 10000000 :
    b = 10000000
array = []
for i in range(a, b+1) :
    if is_palindrom(i) == True :
        array.append(i)

for i in array :
    if is_prime_number(i) == True :
        print(i)
print(-1)
# array = [True for i in range(b+1)]

# for i in range(2, int(math.sqrt(b))+1) :
#     if array[i] == True :
#         j = 2
#         while i*j <= b :
#             array[i*j] = False
#             j += 1

# m = b+1

# for i in range(5,m) :
#     if is_palindrom(i) == True :
#         if array[i] :
#             print(i)
# print(-1)

