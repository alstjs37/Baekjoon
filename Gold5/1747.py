import math

def is_prime_number(x) :
    if x == 1 :
        return False
    for i in range(2, int(math.sqrt(x))+1) :
        if x % i == 0 :
            return False
    return True

def is_palindrom(num) :
    list_num = list(str(num))
    reverse_num = list(str(num))
    reverse_num.reverse()

    if list_num == reverse_num :
        return True

m = int(input())

while True :
    if is_prime_number(m) == True :
        if is_palindrom(m) == True :
            print(m)
            break
    m += 1