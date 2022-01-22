n = int(input())

wc = 0
for _ in range(n) :
    
    s = input()
    word = list(s)

    cnt = 0
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            word[i] = ""

    word = "".join(word)

    for i in word :
        
        w = word.count(i)
        
        if w > 1 :
            break
        cnt += 1

    if int(cnt / len(word)) == 1 :
        wc += 1
    
print(wc)