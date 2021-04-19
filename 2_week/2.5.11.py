String = [int(Element) for Element in input().split()]
String.sort()
String.append(' ')
Number=String[0] #первый элемент в повторящийся строки последовательности
for Count in String: #текущий элемент всегда Count
    if Number != Count:
        x = String.count(Number) #
        if x>1:
            print(Number,end=' ')
        Number=Count
        x = 0
