String = [int(Element) for Element in input().split()]
String.sort()
OutString=[]
for Count in String:
    if String[Count] not in String:
        del String[Count]
for Element in String:
    if Element == Element:
        print(Element,end=' ')