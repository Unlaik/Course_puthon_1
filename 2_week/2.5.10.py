String = [int(Element) for Element in input().split()]
Counts=len(String)
i = 0
j = 2
if Counts>1:
    print(String[1]+String[-1],end=' ')
    for Element in range(1,Counts-1):
        Element = String[i] + String[j]
        print(Element,end=' ')
        i+=1
        j+=1
    print(String[-2]+String[0],end=' ')
else:
    for a in range(len(String)):
        print(String[a])