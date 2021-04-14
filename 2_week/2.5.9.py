String=input().split()
Summ=0
for Count in range(len(String)):
    String[Count] = int(String[Count])
    Summ += int(String[Count])
print(Summ)