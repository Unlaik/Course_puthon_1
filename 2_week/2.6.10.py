String = []
while ['end'] not in String: #принимаем в массив числа, пока не встретим слово 'end'
 NewString = [Element for Element in input().split()] #через генератор формируем каждую строку в массив
 String.append(NewString) #присваеваем один массив к другому
String.remove(['end'])  #удаляем не нужную строку в массиве
for i in range(len(String)): #перебираем все вложенные списки
    for j in range(len(String[i])): #перебираем все элементы внутри вложенных списков
       FirtsNumber=String[i-1][j]
       SecondNumber=String[i+1-len(String)][j]#len(String)отнимает количество списков, т.к. мы асбтрактно не можем выйти за границы массива
       ThreeNumber=String[i][j-1]
       FourNumber=String[i][j+1-len(String[i])] #len(String[i])отнимает количество элементов вложенного списка, т.к. мы асбтрактно не можем выйти за границы массива
       j=int(FirtsNumber)+int(SecondNumber)+int(ThreeNumber)+int(FourNumber)
       print(j, end=' ')
    print()