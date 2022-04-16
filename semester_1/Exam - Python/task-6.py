# Заполнить квадратную матрицу m <= 18 следующим образом:
# - ниже побочной диагонали все элементы равны нулю
# - выше побочной диагонали включая диагональ начиная с левого верхнего угла
# матрицы по часовой стрелке размещаются
# по возрастающей спирали последовательности натуральных чисел начиная
# с числа 1
# например n = 5

#  1  2  3 4 5
# 12 13 14 6 0
# 11 15  7 0 0
# 10  8  0 0 0
#  9  0  0 0 0

# Далее вычекнутьиз матрицы строку с максимальным элементом,
# расположенным над побочной диагональю.Полученную матрицу напечатать.

while True:
    m = int(input('Введите размер квадратной матрицы меньше 18: '))
    if m <= 18 and m > 0:
        break
    else:
        print('Размер больше 18! Превышен предел!')

def printMatrix(matrix):
    if matrix == []:
        print('Матрица пуста!')
    else:
        for i in matrix:
            print(' '*4, end='')
            for j in i:
                print('{:^5g}'.format(j), end='')
            print()
        print()

matrix = [[0 for j in range(m)] for i in range(m)]

number = 1
b = 0
t = 0

while b < int(m/2) and m > 1:
    c = m - 1 - b
    for i in range(m-b):
        for j in range (b,m-b):
            if j > c:
                continue
            else:
                if i == b:
                    matrix[i][j] = number
                    number += 1
                elif j == c and i > b:
                    matrix[i][j] = number
                    number += 1             
        c -= 1
        
    c = m - 1 - b
    for i in range(m-2-t,b,-1):
        for j in range (b,m-b):
            if j > c:
                continue
            else:
                if j == b :
                   matrix[i][j] = number
                   number += 1  
        c -= 1
        
    b += 1
    t += 2
else:
    matrix[0][0] = 1
print('Полученная матрица:')   
printMatrix(matrix)

maxEl = matrix[0][0]

if m > 1:
    for i in range(m):
        for j in range(m):
            if maxEl < matrix[i][j]:
                maxEl = matrix[i][j]
                delete_i = i
                
    matrix.remove(matrix[delete_i])
    print('Максимальный элемент матрицы в' , delete_i+1 ,'строке и равен', maxEl, '\n')
else:
    matrix.remove(matrix[maxEl-1])
    print('Максимальный элемент матрицы в 1 строке и равен 1\n')
print('Преобразованная матрица:')   
printMatrix(matrix)
