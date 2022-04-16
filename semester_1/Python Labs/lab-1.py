import math as m
r = float(input("Введите радиус основания цилиндра: "))
h = float(input("Введите высоту: "))
s = (3 * m.sqrt(3)) / 4 * (r**2)

sb = m.sqrt(3) * 3 * r * h
ps = 2 * s + sb
v = s * h

print("Объем призмы: ",'{:8.4f}'.format(v) )
print("Площадь боковой поверхности: ", '{:.4f}'.format(sb))
print("Площадь полной поверхности: ", '{:.4f}'.format(ps))
