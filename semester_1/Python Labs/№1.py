#Дана квадратная матрица.
#Пользователь задает 2 точки с координатами (i1,j1) (i2,j2).
#Определить среднее арифметическое чисел, лежащих ниже или
#на прямой, проходящей через указанные точки.
#Дополнительных списков не использовать.
#Элементы матрицы, меньшие среднего арифметического,
#переписать в одномерный список.
#В указанном списке определить количество монотонно
#возрастающих последовательностей подряд идущих элементов.
#n = int(input('Ввведите размер квадратной матрицы: '))
n = int(input('Введите размер матрицы: '))
matrix = []
print('Введите элементы матрицы: ')
for i in range(n):
    x = list(map(int, input().split()))
    matrix.append(x)
while True:
    print('Введите координаты точки A:')
    a_i = int(input('Введите i - '))
    a_j = int(input('Введите j - '))
    print('Введите координаты точки B:')
    b_i = int(input('Введите i - '))
    b_j = int(input('Введите j - '))
    if a_i < n and a_j < n and b_i < n and b_j < n:
        break
    else:
        print('Координаты выходят за предел матрицы.\n')

'''matrix = [[9,  7,   6, 4],
          [10, 21, 38, 3],
          [5,  78,  0, 90],
          [1,   5,  8, 91]]
'''
summ = 0
m = 0
print('Элемент = координаты.')
for i in range(n):
    for j in range(n):
        if (a_i < b_i and a_j < b_j) or (a_i > b_i and a_j > b_j):
            if (i >= a_i and j <= a_j) or (i >= b_i and j <= b_j):
                print('-- ',matrix[i][j],' = ', i,j, sep='')
                summ += matrix[i][j]
                m += 1
            elif (i > a_i   and i < b_i  and j < b_j - 1) or (i > b_i   and i < a_i  and j < a_j - 1):
                print('-- ',matrix[i][j],' = ', i,j, sep='')
                summ += matrix[i][j]
            elif i == abs(a_i - b_i) and (j < a_j or j < b_j):
                print('-- ',matrix[i][j],' = ', i,j, sep='')
                summ += matrix[i][j]
        elif (a_i > b_i and a_j < b_j) or (a_i < b_i and a_j > b_j):
            if (i >= a_i and j >= a_j) or (i >= b_i and j >= b_j):
                print('-- ',matrix[i][j],' = ', i,j, sep='')
                summ += matrix[i][j]
                m += 1
            elif (i > b_i  and j > a_j) or (j > b_j  and i > a_i):
                print('-- ',matrix[i][j],' == ', i,j, sep='')
                summ += matrix[i][j]
                m += 1
             
print('Cумма элементов =',summ)
print('Количество элементов = ',m)
a_arif = summ/m
print('Cреднее арифметическое чисел = ',a_arif)
b = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] < m:
            b.append(matrix[i][j])
print('Получили массив:', end=' ')
for i in b:
    print(i,end=', ')
print()
g = 0
d = 0
for i in range(1,len(b)):
    if b[i-1] < b[i]:
        d += 1
    else:
        if d == 1:
            d = 0
        else:
            g += 1
            d = 0
print('Количество монотонно возрастающих последовательностей =',g)
