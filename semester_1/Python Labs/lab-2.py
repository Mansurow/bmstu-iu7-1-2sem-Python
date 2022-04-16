import math as m
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
if a == 0 and b != 0 and c != 0:
    x = -(c/b)
    print("x =", '{:.4f}'.format(x))
elif a == 0 and b == 0 and c != 0:
    print("Нет корней")
elif a == 0 and b == 0 and c == 0:
    print("x - любое число")
elif a == 0 and b != 0 and c == 0:
    x = 0/b 
    print("x = ", '{:.4f}'.format(x))
else:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + m.sqrt(d)) / (2 * a)
        x2 = (-b - m.sqrt(d)) / (2 * a)
        print("x1 =", '{:.4f}'.format(x1), "и", "x2 =", '{:.4f}'.format(x2))
    elif d == 0:
        x = -b / (2 * a)
        print("x =", '{:.4f}'.format(x) )
    else:
        print("Нет корней")
