n = int(input())

array = []
for i in range(n) :
    array.append(int(input()))

for end in range(1, len(array)) :
    for i in range(end,0,-1) :
        if array[i-1] > array[i] :
            array[i-1], array[i] = array[i], array[i-1]

for i in range(len(array)) :
    print(array[i]) 