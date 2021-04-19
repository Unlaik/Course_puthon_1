Numbers = [int(string) for string in input().split()]
Minimum = Numbers[0]
for CurrentNumber in Numbers:
    if Minimum>CurrentNumber:
        Minimum=CurrentNumber
print(Minimum)