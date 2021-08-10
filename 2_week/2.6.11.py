InputNumber=int(input())
x=1
y=InputNumber
Matrix=[[0 for i in range(InputNumber)] for j in range(InputNumber)]
for i in range(1):
    for j in range(InputNumber):
        Matrix[i][j] +=x
        x+=1
while 0 not in Matrix:
    for j in range(1):
        for i in range(1):
            Matrix[i][j] +=x
            x+=1

       # for j in range(y,0,-1):
        #    for i in range(y,-1,-1):
         #       Matrix[i][j] += x
          #      x += 1