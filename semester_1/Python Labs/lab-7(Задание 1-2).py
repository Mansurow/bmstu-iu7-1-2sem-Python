#1. Ввести квадратную числовую матрицу, повернуть её на 90 градусов по часовой стрелке.
#2. Ввести прямоугольную символьную матрицу, удалить из неё столбец, содержащий наибольшее количество гласных букв,
#вывести новую матрицу. Затем в одномерный массив B переписать все цифры из чётных строк матрицы и поменять местами
#максимальную нечётную цифру с последним нулём.
m, n = map(int,input('Введите размер матрицы m x n : ').split('x'))
x = [[0]*n for i in range(m)]
print('Вводим элементы матрицы:')
for i in range (m):
   print('----')
   for j in range(n):
       x1 = input()
       if type(x1) == str:
            if x1.isdigit():
                x1 = int(x1)
       x[i][j] = x1
   print('----')
if n == m:
    print('Получаем квадратную матрицу')
    for i in x:
        print(' ',end=' ')
        for j in i:
            print(j, end='  ')
        print()
    print('Повернуть её на 90 градусов по часовой стрелке.')
    x = [[x[i][j] for i in range(len(x)-1,-1,-1)]for j in range(n)]
    
else:
    print('Получаем прямоугольную матрицы')
    print('Удаляем столбец с наибольшем количеством гласных букв')
    vowels = ['a','e','o','u','y','i','A','I','E','O','U','Y'] # массив со всеми гласными
    c = []
    b = []
    d = 0
    print('\nДо удаление:')
    print('Размер матрицы', m, 'x', n)
    for i in x:
        print(' ',end=' ')
        for j in i:
            print(j, end='  ')
        print()
    print('\nПосле удаление:')
    #---------------------------------------------------
    #Удаление столбца с наибольшем количеством гласных букв
    for i in range(n):
        for j in range (m):
            if x[j][i] in vowels:
                d += 1
        c.append(d)
        d = 0
    cmax = max(c)
    k = c.index(cmax)
    if cmax != 0:
        for i in x:
            i.remove(i[k])
        n -=1
    #----------------------
    print('Размер матрицы', m, 'x', n)
    for i in x:
        print(' ',end=' ')
        for j in i:
            print(j, end='  ')
        print()
    #--------------------------------------------
    #Создаем массив B из чисел четных строк матрицы
    print('\nСоздаем массив B из чисел четных строк матрицы')
    for i in range(m):
        if (i+1) % 2 == 0:
            for j in range(n):
                if type(x[i][j]) == str:
                    continue
                b.append(x[i][j])
    print('Массив B =', b)
    #---------------------
    #--------------------------------------------
    #Меняем местами последний ноль и макс нечетное число
    d = -10000 # макс. нечетный элемент
    e = 1 # последнего нуля
    i_d = 0 # x[i][j] макс. нечетного элемента
    j_d = 0
    i_e = 0 # x[i][j] последнего нуля
    j_e = 0
    for i in range(m):
        for j in range(n):
            if type(x[i][j]) != str and x[i][j] % 2 !=0 and  x[i][j] > d:
                d = x[i][j]
                i_d = i
                j_d = j
        for j in range(n):
            if (x[i][j]) == 0:
                e = x[i][j]
                j_e = j
                i_e = i
    if e == 1:
        print('В матрице нет нулей')
    elif abs(d) % 2 == 0:
        print('В матрице все числа четные')
    else:
        x[i_d][j_d],x[i_e][j_e] = x[i_e][j_e],x[i_d][j_d]
        print('Макс. нечетный эелемент', d,'с индексом','x[',i_d,'][',j_d,']')
        print('Последний нуль расположен по индексу','x[',i_e,'][',j_e,']')
    #---------------------
# вывод       
for i in x:
    print(' ',end=' ')
    for j in i:
        print(j, end='  ')
    print()
