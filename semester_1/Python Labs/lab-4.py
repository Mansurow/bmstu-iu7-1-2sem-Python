import math as m
import numpy as np

while True:
    xn,xk,xsh = map(float,input("Введите начальное и конечное значение аргумента и шаг: ").split())
    if xk - xn > 0 and xsh > 0  or xk - xn < 0 and xsh < 0 or xk == xn:
        break
    else:
        print("Ошибка!!!")
        print("При данном шаге невозможно!")
        
print("Вычисляем и строим график одной из функций: ")
print("q1 = h**4 - 3*h**3 + 8*h**2 - 5")
print("q2 = e**(-h) + (h - 1)**2 - 3")


minq1 = 100000
minh = 100000
eps = 0.011
maxy, miny ="No", "No"

q2_sum = 0
q2_multi = 1
y1 = []
y2 = []
x = []
print("\nТаблица значений функций q1 и q2\n")
print("----------------------------------------------------------------")
print("|{:^20}|{:^20}|{:^20}|".format("h","q1","q2"))
print("----------------------------------------------------------------")

for h in np.arange(xn,xk+xsh,xsh):  
    q1 = h**4 - 3*h**3 + 8*h**2 - 5
    q2 = (m.e)**(-h) + (h - 1)**2 - 3
    if q1 < 0:
        minq1 == q1
        minh = h
    if maxy == "No" or q1 > maxy:
        maxy = q1
    if miny == "No" or q1 < miny:
        miny = q1
    y1.append(q1)
    y2.append(q2)
    x.append(h)
    q2_sum += q2
    q2_multi *= q2
    print('|{:^20}|{:^20}|{:^20}|'.format(f'{h:.4g}', f'{q1:.4g}', f'{q2:.4g}'))
     
print("----------------------------------------------------------------")
print("Вычисляем суммы и произведение значений q2...")
print("Сумма значений q2 =", '{:.4g}'.format(q2_sum))
print("Произведение значений q2 =", '{:.4g}'.format(q2_multi))



import sys
'''or (xn + xk < xsh and xn + xk !=0)'''
if xn == xk :
    print("\nГрафиком функции q1 является одна точка")
    print("\nГрафиком функции q2 является одна точка")
    sys.exit()
while True:
    kzas = int(input("\nВвведите число засечек от 4 до 8: "))
    if kzas >= 4 and kzas <= 8:
        break
    else:
        print("Введите числа от 4 до 8!!!")
width = 70
StepY = (maxy - miny) / width
zasStep = (maxy-miny) / (kzas - 1)
r = (width-1) // (kzas- 1)
print("\nГрафик функции q1:\n")
# Расставляем значения засечек
print("     ", end='')
tekzas = miny
for k in range(1, kzas):
    if abs(tekzas) < 10000 and abs(q2) > 0.00001:
        print("{:<10.5g}".format(tekzas)+" "*int(r-10),end = "")
    else:
        print("{:<10.2e}".format(tekzas)+" "*int(r-10),end = "")
    tekzas += zasStep
if abs(tekzas) < 10000 and abs(q2) > 0.00001:
    print("{:<10.4g}".format(tekzas),end = "")
else:
    print("{:<10.2e}".format(tekzas),end = "")

# Рисуем ось Оу
print("\n ",end = "       ")
for i in range(0,width+1):
    if i % (width//(kzas-1)) == 0:
        print("|",end = "") 
    else: 
        print("-",end = "") 
print("--> Y")

# рисуем график q1
if xsh > 0:
    if miny < 0 < maxy:
        j = int(abs(miny)//StepY)
        for h in np.arange(xn,xk+eps,xsh):
            q1 = h**4 - 3*h**3 + 8*h**2 - 5
            m = int(width*(q1 - miny)//(maxy - miny))    
            print("{:>7.5g}".format(h),end = "") 
            for i in range(0,width+1):
                if i == m:
                    print("*",end = "")
                elif i == j:
                    print("|",end = "")
                else:
                    print(" ",end = "")

            print() 
        print(" "*(j+7)+"|")
        print(" "*(j+7)+"V")
        print(" "*(j+7)+"X")
    else:
        for h in np.arange(xn,xk+xsh,xsh):
            q1 = h**4 - 3*h**3 + 8*h**2 - 5
            i = int(width*(q1 - miny)//(maxy - miny))    
            print("{:>7.5g}".format(h)+"|"," "*(i - 1)+"*",end = "")
            print()
        print(" "*(7)+"|")
        print(" "*(7)+"V")
        print(" "*(7)+"X")
elif xsh < 0:
    if miny < 0 < maxy:
        j = int(abs(miny)//StepY)
        for h in np.arange(xk-eps,xn,xsh):
            q1 = h**4 - 3*h**3 + 8*h**2 - 5
            m = int(width*(q1 - miny)//(maxy - miny))    
            print("{:>7.5g}".format(h),end = "") 
            i = 0
            print(i , j)
            for i in range(0,width+1):
                if i == m:
                    print("*",end = "")
                elif i == j:
                    print("|",end = "")
                else:
                    print(" ",end = "")
            print() 
        print(" "*(j+7)+"|")
        print(" "*(j+7)+"V")
        print(" "*(j+7)+"X")
    else:
        for h in np.arange(xn,xk+eps,xsh):
            q1 = h**4 - 3*h**3 + 8*h**2 - 5
            i = int(width*(q1 - miny)//(maxy - miny))    
            print("{:>7.5g}".format(h)+"|"," "*(i - 1)+"*",end = "")
            print()
        print(" "*(7)+"|")
        print(" "*(7)+"V")
        print(" "*(7)+"X")
