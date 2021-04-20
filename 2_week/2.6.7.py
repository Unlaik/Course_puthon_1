String = []
NewNumber = int(input())
Summ = NewNumber
String.append((NewNumber))
while Summ != 0:
    NewNumber = int(input())
    String.append(NewNumber)
    Summ += NewNumber
Summ = 0
for NewNumber in String:
    Summ += NewNumber ** 2
print(Summ)