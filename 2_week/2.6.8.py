CountList = []
n=int(input()) #макс. длинна списка
i = 1
CountTime=1
while len(CountList) < n: # запускаем цикл, пока длинна списка меньше максимальной длинны списка
    for AddInList in range(CountTime): # запускаем цикл определенное количетсво раз
        AddInList=CountList.append(i) #добавляем переменну i в список
        if len(CountList) == n: #проверяем длинну списка, чтобы не привышала максимальную длинну списка
            break
    i += 1 #Увеличиваем переменну i, которая принимает в себя [1,2,3...]
    CountTime+=1 #Увеличиваем количество пройденных раз на 1
for OutFromList in CountList: #Выводим ведь массив в длинну
    print(OutFromList,end=' ')