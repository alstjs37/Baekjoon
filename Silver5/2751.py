n = int(input())
l = []

for i in range(n) :
    l.append(int(input()))

new_l = sorted(l)

for i in range(len(new_l)):
    print(new_l[i])