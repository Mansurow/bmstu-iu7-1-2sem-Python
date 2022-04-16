#3. Ввести матрицу найти столбец с наибольшим количеством нулей и переместить в конец.
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
print('Получаем матрицу')
for i in x:
    print(' ',end=' ')
    for j in i:
        print(j, end='  ')
    print()
c = []
vowels = ['a','e','o','u','y','i','A','I','E','O','U','Y']
d = 0         
b = 0
cmax = 0
for i in range(n):
    for j in range (m):
        if x[j][i] == 0:
            d += 1
    c.append(d)
    d = 0
cmax = max(c)
k = c.index(cmax)
if cmax != 0:
    for i in x:
        i.append(i[k])
    for i in x:
        i.remove(i[k])
 
print('\nПолучаем матрицу изменненную:')
for i in x:
    print(' ',end=' ')
    for j in i:
        print(j, end='  ')
    print()
