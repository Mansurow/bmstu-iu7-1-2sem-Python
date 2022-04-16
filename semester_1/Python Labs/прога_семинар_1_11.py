# Квадратная матрица поменять минимальный элемент и дигональный элемент строки.
def getMatrix():
    size = int(input('Введите размер квадрвтной матрицы: '))

    matrix = [0] * size
    print('Построчно введите элементы матрицы:')
    for i in range(size):
        matrix[i] = list(map(float, input('> ').split()))

    return matrix, size

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
matrix, size = getMatrix()
    
for i in range(size):
    minElIndex = 0
    
    for j in range(size):
        if matrix[i][j] < matrix[i][minElIndex]:
            minElIndex = j

        matrix[i][minElIndex],matrix[i][i] = matrix[i][i], matrix[i][minElIndex]

print(printMatrix(matrix))

#------------------------------------------------------------------------------
#Из квадратной матрицы убрать главную диагональ и нижний треугольник подвинуть вверх

n = int(input('Введите размер квадрвтной матрицы: '))
mat = []

for i in range(n):
    x = list(map(int, input().split()))
    mat.append(x)
print(mat)
for i in range(n):
    for j in range(n-1):
        if i >= j:
            mat[i][j] = mat[i+1][j]
for i in range(n-1):
   print(mat[i])
#------------------------------------------------------------------------------
# Сформировать квадратную матрицу ввида
# 1 2 3 4 5
# 2 1 2 3 4
# 3 2 1 2 3
# 4 3 2 1 2 
# 5 4 3 2 1

n = int(input('Введите размер квадрвтной матрицы: '))

a=[n*[0] for i in range(n)]
for i in range(n):
    a[0][i] = i+1
    print(a[0][i], end=' ')
for i in range(1,n):
    print('\n')
    for j in range(i):
        a[i][j] = a[i-1][j]+1
        print(a[i][j], end=' ')
    for j in range(i,n):
        a[i][j] = a[i-1][j]-1
        print(a[i][j], end=' ')
# или

M = int(input('\nВведите размер строки'))
matrix = [[i*1 for i in range(M)] for i in range(M)]
for i in range(1,M):
    for j in range(M):
        matrix[i][j] = matrix[i-1][(j + M - 1)% M]
[print(*i) for i in matrix]

#Найти сумму элементов матрицы под главной и побочной диагоналей и вкл их
M = int(input('\nВведите размер строки'))
matrix = [0]*M
for i in range(M):
    matrix[i] = list(map(int,input().split()))

for i in range(M):
    print(matrix[i])
S = 0
for i in range(M):
    for j in range(M):
        if (i >= j and j <= M - i - 1) or (i <= j and j >= M - i - 1):
            S += matrix[i][j]
print(S)
