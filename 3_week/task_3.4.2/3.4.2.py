with open("text.txt", 'r') as Data:
    String = Data.readline()
    String += " "
    LongString = len(String) - 1
    Position = 0
    NextPosition = 1
    CurrentCount = 0
    CountList = []
    OutPutList = []
    while not (String[NextPosition] == " "):
            while String[NextPosition].isdigit():
                CurrentCount = String[NextPosition]
                CountList.append(CurrentCount)
                NextPosition += 1
                if NextPosition >= LongString:
                    FinalCount = int("".join(map(str, CountList)))
                    OutString = (String[Position] * FinalCount)
                    OutPutList.append(OutString)
                    StringForWrite = ("".join(map(str, OutPutList)))
                    break
                else:
                    CurrentCount = 0
                if NextPosition > LongString:
                    break
            if String[NextPosition].isalpha():
                FinalCount = int("".join(map(str, CountList)))
                OutString = (String[Position] * FinalCount)
                OutPutList.append(OutString)
                StringForWrite = ("".join(map(str, OutPutList)))
                Position = NextPosition
                NextPosition += 1
                CountList.clear()

with open("text.txt", 'w') as Data:
    Data.write(StringForWrite)
