# Заполнить квадратную матрицу n <= 17 следующим образом:
# - ниже главной диагонали все элементы равны нулю
# - выше главной диагонали включая диагональ начиная с левого
# верхнего угла матрицы по часовой стрелке размещаются по убывающей
# спирали последовательности натуральных числел начиная с числа
# n*(n+1)/2
# например n = 5

# 15 14 13 12 11
# 0   4  3  2 10
# 0   0  5  1  9
# 0   0  0  6  8
# 0   0  0  0  7

# Далее вычекнутьиз матрицы строку с минимальным элементом,
# расположенным над главной диагональю.Полученную матрицу напечатать.
def printMatrix(matrix):
    if matrix == []:
        print('Матрица пуста!')
    else:
        for i in matrix:
            print(''*4, end='')
            for j in i:
                print('{:5g}'.format(j), end='')
            print()
        print()
while True:
    n = int(input('Введите размер квадратной матрицы меньше 17: '))
    if n <= 17 and n > 0:
        break
    else:
        print('Размер матрицы больше 17! Превысен предел!')

matrix = [[0 for i in range(n)] for i in range(n)]
number = int(n*(n+1)/2)
b = 0
while b < int(n/2) and n > 1:
    for i in range(b,n-b):
            for j in range(b,n-b):
                if j < i+b:
                    continue
                if b == 0:
                    if i == 0:
                        matrix[i][j] = number
                        number -= 1
                    if j == n-1 and i != 0 :
                        matrix[i][j] = number
                        number -= 1
                else:
                    if i == b and j != b:
                        matrix[i][j] = number
                        number -= 1
                    if j == n-1-b and i != b and i != n-1-b:
                        matrix[i][j] = number
                        number -= 1
    for i in range(n-2-b,b,-1):
        for j in range(b,n-b):
            if number < 1:
                break
            if j < i+b:
                continue
            if i == j and b == 0:
                matrix[i][j] = number
                number -= 1
            if i < j and i+1+b> j and b > 0 and i != b and i!= n-1-b and j != n-1-b:
                matrix[i][j] = number
                number -= 1
    b += 1
    
if n == 1:
    matrix[0][0] = 1

print('Полученная матрица:')     
printMatrix(matrix)

minEl = matrix[0][0]
if n > 1:
    for i in range(n):
        for j in range(n):
            if matrix[i][j]!= 0 and minEl > matrix[i][j]:
                minEl = matrix[i][j]
                delete_i = i
    matrix.remove(matrix[delete_i])
    print('Минимальные элемент был найден в', delete_i+1, 'строке и равен', minEl,'\n')
else:
   matrix.remove(matrix[0])
   print('Минимальные элемент был найден в 1 строке и равен', minEl,'\n')
print('Преобразованная матрица:')
printMatrix(matrix)
