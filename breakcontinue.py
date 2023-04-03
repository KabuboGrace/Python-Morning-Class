i = 1

while i<6:
    print(i)
    i+=1


while i<6:
    print(i)
    if i == 3:
        break

    i+=1


# continue statement

a = 2

while a<10:
    a += 1
    if a==6:
        continue

    print(a)



b = 79

while b<84:
    b += 1
    if b==83:
        continue
    print(b)