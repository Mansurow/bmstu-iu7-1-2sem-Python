# В матрице отсортировать столбцы по среднему
# арифм положительных элементов,
# новые массивы использовать нельзя.
# И потом еще посчитать где больше чисел кратных 5-
# в нижнетреугольной или в верхнетреугольной

matrix = [[25,40,5,9,8],
          [10,6,7,8,0],
          [8,9,0,7,5],
          [4,90,50,2,1]]
n = len(matrix[0])
m = len(matrix)
#matrix1 = [[0 for j in range(n)] for i in range(m)]
def printMatrix(matrix):
    for i in range(m):
        print(' '*4 ,end='')
        for j in range(n):
            print('{:^5}'.format(matrix[i][j]), end='')
        print()
        
print('Матрица для работы:')
printMatrix(matrix)
dic = {}
for i in range(n):
    numberOfFigure = 0
    summ = 0
    for j in range(m):
        if matrix[j][i] >= 0:
            numberOfFigure += 1
            summ += matrix[j][i]
    ariv = summ / numberOfFigure
    dic[i] = ariv
    
b = 1
matrix = list(map(list, zip(*matrix)))
while b < len(matrix):
    for i in range(len(matrix) - b):
        if dic[i] > dic[i + 1]:
            dic[i], dic[i + 1] = dic[i + 1], dic[i]
            matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    b += 1

matrix = list(map(list, zip(*matrix)))
 
print('Матрица после операции над средним арифметическим:')
printMatrix(matrix)
numberOfLeft = 0
numberOfRight = 0
for i in range(m):
    for j in range(n):
        if j <= i and matrix[i][j] % 5 == 0:
            if matrix[i][j] == 0 :
                continue
            numberOfLeft += 1
for i in range(m):
    for j in range(n):
        if j >= i and matrix[i][j] % 5 == 0:
            if matrix[i][j] == 0 :
                continue
            numberOfRight += 1

if numberOfLeft > numberOfRight:
    print('В нижнем треугольнике матрице больше чисел кратным 5.')
    print('В нижнем треугольнике матрицы -', numberOfLeft)
    print('В верхнем треугольнике матрицы -', numberOfRight)
elif numberOfLeft < numberOfRight:
    print('В верхнем треугольнике матрицы больше чисел кратным 5.')
    print('В нижнем треугольнике матрицы -', numberOfLeft)
    print('В верхнем треугольнике матрицы -', numberOfRight)
elif numberOfLeft == 0 and numberOfRight == 0:
    print('В нижнем и верхнем треугольнике матрицы нет чисел кратным 5.')
else:
    print('В нижнем и верхнем треугольнике матрицы количестов чисел кратным 5 равны.')
