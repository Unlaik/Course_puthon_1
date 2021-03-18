a = 0
while a<100 or a>10:
    a = int(input())
    if a<10:
        continue
    elif a>100:
        break
    else:
        print(a)
