from itertools import combinations

length = []

for i in range(9) :
    length.append(int(input()))

sort_a = sorted(length)
a = list(combinations(sort_a, 7))

for i in a :
    if sum(i) == 100 :
        result = i

for i in range(len(result)) :
    print(result[i])