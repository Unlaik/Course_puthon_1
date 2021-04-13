String=input()
LongString=len(String)-1
Position=0
NextPosition=1
Count=1
if LongString>1:
    while Position<=LongString:
        if String[Position] in String.upper():
            while String[Position] == String[NextPosition]:
                Count += 1
                Position += 1
                NextPosition+=1
                if NextPosition > LongString:
                    break
            print(String[Position]+str(Count),end='')
            if NextPosition > LongString:
                break
            Position+=1
            NextPosition += 1
            Count=1
            if NextPosition>LongString:
                print(String[Position] + str(Count), end='')
                break
        else:
            while String[Position] == String[NextPosition]:
                Count += 1
                Position += 1
                NextPosition += 1
                if NextPosition>LongString:
                    break
            print(String[Position]+str(Count),end='')
            if NextPosition>LongString:
                break
            Position += 1
            NextPosition += 1
            Count = 1
            if NextPosition>LongString:
                print(String[Position] + str(Count), end='')
                break
else:
    print(str(String)+str(1))