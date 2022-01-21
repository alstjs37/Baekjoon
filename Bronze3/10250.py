x = int(input())

i = 0
while i < x :
    h, w, n = map(int, input().split())

    if n % h == 0 :
        room = n // h
        floor = h
    else :
        room = (n // h) + 1
        floor = n % h

    if room < 10 :
        room = "0" + str(room)
    print(str(floor) + str(room))
    i += 1