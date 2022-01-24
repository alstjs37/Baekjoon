num_set = set(range(1, 10000))
generated_num = set()

for i in range(1, 10001) :
    for j in str(i) :
        i += int(j)
    generated_num.add(i)

self_num = sorted(num_set - generated_num)

for i in self_num :
    print(i)