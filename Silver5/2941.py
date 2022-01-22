alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for i in alpa :
    word = word.replace(i, "*")
print(len(word))