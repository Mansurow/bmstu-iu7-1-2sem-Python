import math as m
A_x, A_y = float(input("Введите вершину A:\nx = ")), float(input("y = ")) 
B_x, B_y = float(input("Введите вершину B:\nx = ")), float(input("y = ")) 
C_x, C_y = float(input("Введите вершину C:\nx = ")), float(input("y = ")) 

# Находим длину стороны AB = a
a = m.sqrt((B_x - A_x)**2 + (B_y - A_y)**2)
# Находим длину стороны BC = b
b = m.sqrt((C_x - B_x)**2 + (C_y - B_y)**2)
# Находим длину стороны AC = c
c = m.sqrt((C_x - A_x)**2 + (C_y - A_y)**2)
print("Длина стороны AB =", '{:.4f}'.format(a),"\nДлина стороны BC =", '{:.4f}'.format(b),"\nДлина стороны AC =", '{:.4f}'.format(c))

if a + b > c and a + c > b and c + b > a:
    # Находим площадь тр.ABC через формулу Герона
    P_abc = (a + b + c)/2
    S_abc = m.sqrt(P_abc*(P_abc - a)*(P_abc - b)*(P_abc - c))
    #Находим наименьший угол и длину высоты проведенной из него
    cos_a = m.acos((a**2 + c**2 - b**2)/(2*a*c))
    cos_b = m.acos((a**2 + b**2 - c**2)/(2*a*b))
    cos_c = m.acos((c**2 + b**2 - a**2)/(2*c*b))

    if cos_a < cos_b and cos_a < cos_c:
        h = 2*S_abc/b
        print("Высота проведеная из наименьшего угла CAB к стороне BC => h = ", '{:.4f}'.format(h))
    elif cos_b < cos_a and cos_b < cos_c:
        h = 2*S_abc/c
        print("Высота проведеная из наименьшего угла CBA к стороне AC => h = ", '{:.4f}'.format(h))
    else:
        h = 2*S_abc/a
        print("Высота проведеная из наименьшего угла CAB к стороне AB => h = ", '{:.4f}'.format(h))

    M_x, M_y = float(input("Введите вершину M:\nx = ")), float(input("y = "))
    # Находим длину стороны MA 
    ma = m.sqrt((A_x - M_x)**2 + (A_y - M_y)**2)
    # Находим длину стороны MB
    mb = m.sqrt((B_x - M_x)**2 + (B_y - M_y)**2)
    # Находим длину стороны MC
    mc = m.sqrt((C_x - M_x)**2 + (C_y - M_y)**2)

    # Находим площадь тр.MAC через формулу Герона
    P_mac = (mc + ma + c)/2
    S_mac = m.sqrt(abs(P_mac*(P_mac - ma)*(P_mac - mc)*(P_mac - c)))
    # Находим площадь тр.MAB через формулу Герона
    P_mab = (mb + ma + a)/2
    S_mab = m.sqrt(abs(P_mab*(P_mab - mb)*(P_mab - ma)*(P_mab - a)))
    # Находим площадь тр.MBC через формулу Герона
    P_mbc = (mb + mc + b)/2
    S_mbc = m.sqrt(abs(P_mbc*(P_mbc - mb)*(P_mbc - mc)*(P_mbc - b)))
    print("S ABC =", '{:.4f}'.format(S_abc))
    print("S MAC =", '{:.4f}'.format(S_mac))
    print("S MAB =", '{:.4f}'.format(S_mab))
    print("S MBC =", '{:.4f}'.format(S_mbc))
    if (abs(S_mbc + S_mab + S_mac) - S_abc) <= 0.01:
        print ('Точка M(', M_x, ";", M_y, ") принадлежит треугольнику ABC", sep="")
        #ищем все расстояния от точки М до сторон и проверяем саммую удаленную
        h_mac = (2*S_mac)/a
        h_mab = (2*S_mab)/c
        h_mbc = (2*S_mbc)/b
        print("Расстояние до АC =", '{:.4f}'.format(h_mac))
        print("Расстояние до АB =", '{:.4f}'.format(h_mab))
        print("Расстояние до BC =", '{:.4f}'.format(h_mbc))
        
        if h_mac > h_mab and h_mac > h_mbc:
            print("Наиболее удаленное расстояние от точки М является расстояние до стороны AC, где она равняется", '{:.4f}'.format(h_mac))
        elif h_mab > h_mac and h_mab > h_mbc:
            print("Наиболее удаленное расстояние от точки М является расстояние до стороны AB, где она равняется", '{:.4f}'.format(h_mab))
        else:
            print("Наиболее удаленное расстояние от точки М является расстояние до стороны BC, где она равняется", '{:.4f}'.format(h_mbc))
    else:
        print ('Точка M(', M_x, ";", M_y, ") не принадлежит треугольнику ABC", sep="")

    #Проверяем остроугольность
    if m.pi/2 - cos_a  >= 0.01 and m.pi/2 - cos_b >= 0.01 and  m.pi/2 - cos_c >= 0.01 :
        print("Треугольник является остроугольным, т.е. все его углы меньше 90")
    else:
        print("Треугольник не является остроугольным")
else:
    print("Это не треугольник")
