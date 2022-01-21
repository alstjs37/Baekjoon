import math

n = 123456 * 2
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1) :
    if array[i] == True :
        j = 2
        while i * j <= n :
            array[i*j] = False
            j += 1

while True : 
    x = int(input())
    cnt = 0

    if x == 0 :
        break
   
    for i in range(x+1, 2*x+1) :
        if array[i] == True :
            cnt += 1
    print(cnt)  