# Вычислить таблицу значений функций v1 и v2.
# Задаётся начальное, конечное значение аргумента и шаг.
# Указан оператор цикла, который нужно использовать (while).
# Должен быть заголовок: название функций и значение.
# Определить также суммы отрицательных значений v1 и v2.

# Нарисовать график функции v2.
# Ось у задаётся всегда, идёт вверху графика горизонтально, на ней сделать 
# от 4 до 8 засечек со значенями функии.
# Ось х идёт вниз, она задаётся, если функция имеет на отрезке  
# и положительные, и отрицательные значения.
# Слева от графика задаётся аргумент.

# v1 - значение первой функции
# v2 - значение второй функции
# minv1 - минимальное значение v1
# mina - минимальное значение a
# x0,xn,xh - начальное, конечное значение аргумента и шаг
# t - текущее значение аргумента
# miny,maxy - минимальное и максимальное значение функции на отрезке
# n - номер строки таблицы


# m - положение звёздочки
# width - ширина графика
# StepY - шаг для значений
# tekzas - текущее значение засечки
# zasStep - шаг значений для засечек
# k - вспомогательная переменная

while True:
    x0,xn = map(float,input("Введите начальное и конечное значение аргумента: "
                ).split())
    xh =  float(input("Введите шаг изменения аргумента: "))
    if xn - x0 > 0 and xh > 0 or xn - x0 < 0 and xh < 0 or xn == x0:
        break
    else:
        print("Ошибка ввода!")
        print("При данном шаге конечное значение аргумента недостижимо!")
        
import math
n = 1
minv1 = 100000
mina = 100000
a = x0
eps = 0.01
maxy, miny = "No","No"

# рисуем шапку таблицы
print("\nТаблица значений функций v1 и v2\n")
print('┌'+'─'*7+'┬'+'─'*20+'┬'+'─'*20+'┬'+'─'*20+'┐')
print("│{:^7}│{:^20}│{:^20}│{:^20}│".format("Номер","аргумент","v1","v2"))

# рисуем таблицу
if xh > 0:
    while a <= xn + eps:
        v1 = 4.07*(a**4) + 12.7*a**3 + 8.7*a**2 + 10.8*a +18.87
        v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
        if v1 < 0:
            minv1 == v1
            mina ==a
        if maxy == "No" or v2 > maxy:
            maxy = v2
        if miny == "No" or v2 < miny:
            miny = v2
        if n <=100:
            print("│{:>5}  │{:>18.3f}  │{:>18.3f}".format(n,a,v1),end = "  │")        
            if abs(v2) < 10000 and abs(v2) > 0.00001:
                print("{:>18.3f}  │".format(v2))
            else:
                print("{:>18.2e}  │".format(v2))
        a += xh
        n += 1
elif xh < 0:
    while a >= xn - eps:
        v1 = 4.07*(a**4) + 12.7*a**3 + 8.7*a**2 + 10.8*a +18.87
        v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
        if v1 < 0:
            minv1 == v1
            mina ==a
        if maxy == "No" or v2 > maxy:
            maxy = v2
        if miny == "No" or v2 < miny:
            miny = v2
        if n <=100:
            print("│{:>5}  │{:>18.3f}  │{:>18.3f}".format(n,a,v1),end = "  │")        
            if abs(v2) < 10000 and abs(v2) > 0.00001:
                print("{:>18.3f}  │".format(v2))
            else:
                print("{:>18.2e}  │".format(v2))
        a += xh
        n += 1
else:
    v1 = 4.07*(a**4) + 12.7*a**3 + 8.7*a**2 + 10.8*a +18.87
    v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
    if p1 < 0:
            minv1 == v1
            mina ==a
    if maxy == "No" or v2 > maxy:
        maxy = v2
    if miny == "No" or v2 < miny:
        miny = p2
    print("│{:>5}  │{:>18.3f}  │{:>18.3f}".format(n,a,v1),end = "  │")        
    if abs(v2) < 10000 and abs(v2) > 0.00001:
        print("{:>18.3f}  │".format(v2))
    else:
        print("{:>18.2e}  │".format(v2))
print('└'+'─'*7+'┴'+'─'*20+'┴'+'─'*20+'┴'+'─'*20+'┘')

print("Минимальное значение v1  "'{:.4f}'.format(minv1,2))
print("Соответствуещее минимальному v1 значение а  "'{:.4f}'.format(mina,2))

print("\n\nГрафик функции v2:\n")

import sys
if x0 == xn:
    print("Графиком функции v2 является одна точка")
    sys.exit()

kzas = 5
width = 65
StepY = (maxy - miny) / width
zasStep = (maxy-miny) / (kzas - 1)
spacebetweenzas = (width-1) // (kzas- 1)

# Расставляем значения засечек
print("     ", end='')
tekzas = miny
k = 1
while k < kzas:
    if abs(tekzas) < 10000 and abs(v2) > 0.00001:
        print("{:<9.1f}".format(tekzas)+" "*int(spacebetweenzas-9),end = "")
    else:
        print("{:<9.2e}".format(tekzas)+" "*int(spacebetweenzas-9),end = "")
    tekzas += zasStep
    k += 1
if abs(tekzas) < 10000 and abs(v2) > 0.00001:
    print("{:<9.1f}".format(tekzas),end = "")
else:
    print("{:<9.2e}".format(tekzas),end = "")

# Рисуем ось Оу
i = 0
print("\n ",end = "       ")
while i <= width:
    if i % (width//(kzas-1)) == 0:
        print("|",end = "") 
    else: 
        print("-",end = "") 
    i += 1
print(">Oy")

# рисуем график
a = x0
if xh > 0:
    if miny < 0 < maxy:
        j = int(abs(miny)//StepY)
        while a <= xn + eps:
            v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
            m = int(width*(v2 - miny)//(maxy - miny))    
            print("{:>7.2f}".format(a),end = "") 
            i = 0
            while i <= width:
                if i == m:
                    print("*",end = "")
                elif i == j:
                    print("|",end = "")
                else:
                    print(" ",end = "")
                i += 1
            a += xh
            print() 
        print(" "*(j+7)+"|")
        print(" "*(j+7)+"Ox")
    else:
        while a <= xn + eps:
            v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
            i = int(width*(v2 - miny)//(maxy - miny))    
            print("{:>7.2f}".format(a)," "*(i - 1)+"*",end = "")
            a += xh
            print()
elif xh < 0:
    if miny < 0 < maxy:
        j = int(abs(miny)//StepY)
        while a >= xn - eps:
            v2 =(4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
            m = int(width*(v2 - miny)//(maxy - miny))    
            print("{:>7.2f}".format(a),end = "") 
            i = 0
            while i <= width:
                if i == m:
                    print("*",end = "")
                elif i == j:
                    print("|",end = "")
                else:
                    print(" ",end = "")
                i += 1
            a += xh
            print() 
        print(" "*(j+7)+"|")
        print(" "*(j+7)+"Ox")
    else:
        while a <= xn + eps:
            v2 = (4 + a**2 )*((math.e)**a -(math.e)**(-a) ) - 18
            i = int(width*(v2 - miny)//(maxy - miny))    
            print("{:>7.2f}".format(a)," "*(i - 1)+"*",end = "")
            a += xh
            print()
