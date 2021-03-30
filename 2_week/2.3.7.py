a=int(input())
b=int(input())
summa=0
numbers=0
for i in range(a,b+1):
    if i % 3 == 0:
        summa+=1
        numbers += i
print(numbers/summa)

