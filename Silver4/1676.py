n = int(input())

result = 1

for i in range(1, n+1) :
    result *= i

list_result = list(str(result))
list_result.reverse()
count = 0

for i in list_result :
    if i == "0" :
        count += 1
    else :
        break
print(count)
