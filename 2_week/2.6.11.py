InputNumber=int(input())
Matrix = [[0] * InputNumber for i in range(InputNumber)] #генерация матрицы n*n  и заполнение её нулями
Matrix[0] = [(col+1) for col in range(InputNumber)] #проход по самой верхней грани матрицы через генератор
y = 0; x = InputNumber-1; row=InputNumber; index = InputNumber # так как проход по верхней грани уже сделан,индекс равен верхней грани, y - столбец, х - строка
while index < InputNumber*InputNumber: #пока индекс не больше n*n
    row -=1 #уменьшения длины на 1
    for column in range(row):# вниз
        y += 1 #направление вниз
        index += 1
        Matrix[y][x] = index
    for column in range(row):     #влево
        x -= 1 #направление влево
        index += 1
        Matrix[y][x] = index
    if index >= InputNumber * InputNumber:
        break
    row -=1 #уменьшения длины на 1
    for column in range(row): # вверх
        y -= 1 #направление вверх
        index += 1
        Matrix[y][x] = index
    for column in range(row): # вправо
        x += 1 #направление вправо
        index += 1
        Matrix[y][x] = index

for line in Matrix:
    print("\t".join(map(str, line)))