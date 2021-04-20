lst = [int(Element) for Element in input().split()]
x = int(input())
lst2= []
i=0
for n in lst:
    if n == x:
        lst2.append(lst.index(n,i))
    i+=1
if len(lst2) !=0:
    for OutNumber in sorted(lst2):
       print(OutNumber, end=' ')
else:
    print('Отсутствует')
