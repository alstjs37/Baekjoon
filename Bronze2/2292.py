n = int(input())

x = 1
i = 1

while True :
    if n == 1 :
        print(1)
        break
    
    if x+1 <= n <= x + (6 * i) :
        print(i+1)
        break
    x = x + (6 * i)
    i +=1