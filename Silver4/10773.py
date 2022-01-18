import sys
input = sys.stdin.readline

k = int(input())

i = 0
array = []
while i != k :
    n = int(input())
    if n == 0 :
        array.pop()
    else : 
        array.append(n)
    i += 1

print(sum(array))