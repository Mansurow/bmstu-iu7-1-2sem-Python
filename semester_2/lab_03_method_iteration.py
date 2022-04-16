from tkinter import *
from tkinter import messagebox
from math import *
import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np

# ошибки при рассчетах 
def errors(number_error):
    if (number_error == 0):
        return number_error, "Успех"
    if (number_error == 1):
        return number_error, "Превышен"
    if (number_error == 2):
        return number_error, "Расход."
    if (number_error == 3):
        return number_error, "Другие"


# нахождения lambda для использование в рассчетах g(x) = x - l * f(x)
def arbitrary_lambda(a,b):
    return 1 / max(fsh(a),fsh(b))

# функция f(x) - !!!!!!!! 
def f(x):
    return sin(x)
# производная от f(x) !!!!!!
def fsh(x):
    return cos(x)
def f2():
    return lambda x: -sin(x)
# итерационные функции g(x)
def g_2(x, t):
    return x - t * f(x)
def g_1(x):
    return x + f(x)
# произволная от функции g(x)
def gsh_2(x, t):
    return 1 - t * fsh(x)
def gsh_1(x):
    return 1 + fsh(x)

# определдение границ сходимости корня
def set_borders(f, a, b):
    if f(a) * f(b) <= 0:
        return True
    return False

def table_consol(i ,number, interval, root, f_root, iteration, error, error_value):
    if (i == 0):
        print("\n+" + "-" * 7 + '+' + "-"*16 + "+" + ("-"*12 + "+") * 2 + ("-"*10 + "+") * 2 + "-"*12 + "+")
    if (type(interval) == str):
        print("|{:^7}|{:^16}|{:^12}|{:^12}|{:^10}|{:^10}|{:^12}|".format(number, interval, root, f_root, iteration, error, error_value))
    elif (type(root) == str):
        print("|{:^7}|   [{:<4};{:>4}]  |{:^12.6}|{:^12.2}|{:^10}|{:^10}|{:^12}|".format(number, interval[0], interval[1], root, f_root, iteration, error, error_value))
    else:
        print("|{:^7}|   [{:<4};{:>4}]  |{:^12.6g}|{:^12.2g}|{:^10}|{:^10}|{:^12}|".format(number, interval[0], interval[1], root, f_root, iteration, error, error_value))
    print("+" + "-" * 7 + '+' + "-"*16 + "+" + ("-"*12 + "+") * 2 + ("-"*10 + "+") * 2 + "-"*12 + "+")
    
def method_iteration(self, a, b, eps, n):
           
    flag = 1 # для вывода корня или же что превышен n_max
    iteration = 1 # подсчет итераций
    condition = True # так как вначале не могу задать условие то ставлю TRUE потом в цикле меняю
    lamd = arbitrary_lambda(a,b) # f(x) ~ lamd 
    x0 = a # тоже самое что и x0 = 0 берем произвольное значение из отрезка [0;2]
    global number_root
    global row
    if (set_borders(f, a, b)):
        while condition:
            # итерационые функции зависит от значения f(x)
            if f(a) < 0: 
                x1 = g_2(x0, lamd)
            else:
                x1 = g_1(x0)
            # xn + 1 = g(xn)
            x0 = x1
            # условие для цикла
            condition = abs(f(x0)) > eps
            iteration += 1
            
            if iteration > n:
                flag = 0
                break
        root = x1
        if flag == 1:
            error, value = errors(0)
            row += 1
            interval = "[ " + str(a) + " ; " + str(b) + " ]"  
            table(self, 0, row, [number_root, interval, '{:.6g}'.format(root), '{:.2g}'.format(f(root)), iteration - 1, error, value], 'normal')
            table_consol(1, number_root, [a, b], root, f(root), iteration - 1, error, value)
            number_root += 1
            
        else:
            error, value = errors(1)
            row += 1
            interval = "[ " + str(a) + " ; " + str(b) + " ]" 
            table(self, 0, row, [number_root, interval, '{:.6g}'.format(root), '{:.2g}'.format(f(root)), iteration - 1, error, value], 'normal')
            table_consol(1, number_root, [a, b], root, f(root), n, error, value)
            number_root += 1
    else:
        error, value = errors(2)
        table_consol(1, '-', [a, b], '-', '-', '-', error, value)

def table(self, col, row, value, fontes):
    lenght = len(value)
    for i in range(lenght):
        if fontes == "bold":
            b = Text(self, width=13, height=1, font=("Arial Bold", 12, "bold"))
        elif fontes == "italic":
            b = Text(self, width=13, height=1, font=("Arial Bold", 12, "italic"))
        else:
            b = Text(self, width=13, height=1, font=("Arial Bold", 12))
        b.insert(1.0, value[i])
        b["state"] = "disabled"
        b.grid(column=(col + i), row=row)

def get_extremum(x, y):
    for i in range(len(x)):
        print(round(x[i],3), fsh(round(x[i],3)), fsh(round(x[i],3)) == 0)
        if fsh(round(x[i],3)) == 0:
            plt.plot(x, y, '-bD', markevery=[floor(x[i] * 10)])

def make_grafic(a, b):
    x = np.linspace(a, b, abs(int(a-b))*100)
    y = []
    for i in range(len(x)):
        y.append(f(x[i]))

    fig, ax = plt.subplots()
    plt.title('График функции  y = f(x)')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    ax.plot(x, y)
    for i in range(0, len(x) - 2, 2):
        try:
            x_res = opt.bisect(fsh, x[i], x[i + 2])
            y_res = f(x_res)
        except:
            continue
        else:
            ax.scatter(x_res, y_res, color='black')
    plt.show()
    
def main():
    try:
        left = float(enter_a.get());
        right = float(enter_b.get());
        step = float(enter_h.get());
        eps = float(enter_eps.get());
        n_max = int(enter_n.get());
    except:
        print("Неправильный ввод данных")
    else:
        window_table = Toplevel(window)
        
        roots = []
        global number_root
        global row
        row = 1
        # цикл итераций зависищих от шага
        lbl_t = Label(window_table, text="Таблица значений", font=("Arial Bold", 13, "bold"))
        lbl_t.grid(column=0, row=0, columnspan=7)
        table(window_table, 0, row, ["Номер", "Отрезок", "Корень", "f(корень)", "Итерации", "Ошибка", "Пояснение"], 'bold')
        table_consol(0, "Номер", "Отрезок", "Корень", "f(корень)", "Итерации", "Ошибка", "Пояснение")
        number_root = 1
        for i in np.arange(left, right - step, step):
            method_iteration(window_table, i, i + step, eps, n_max)
        window_table.grab_set()

        make_grafic(left, right)
        
            
window = Tk()
window.title("Методы уточнения корней")
lbl = Label(window, text="Метод итераций", font=("Arial Bold", 13, "bold"))
lbl_a = Label(window, text="Концы отрезка a и b:", font=("Arial Bold", 10, "italic"))
lbl_h = Label(window, text="Шаг h:", font=("Arial Bold", 10, "italic"))
lbl_eps = Label(window, text="Точность eps:", font=("Arial Bold", 10, "italic"))
lbl_n = Label(window, text="Количесво итераций N_max:", font=("Arial Bold", 10, "italic"))

enter_a = Entry(window)
enter_b = Entry(window)
enter_h = Entry(window)
enter_eps = Entry(window)
enter_n = Entry(window)
btn = Button(window, text="Посчитать", command=main)

lbl.grid(column=0, row=0, columnspan=6)
lbl_a.grid(column=0, row=1, columnspan=2)
enter_a.grid(column=2, row=1)
enter_b.grid(column=3, row=1)
lbl_h.grid(column=0, row=3)
enter_h.grid(column=1, row=3)
lbl_eps.grid(column=2, row=3)
enter_eps.grid(column=3, row=3)
lbl_n.grid(column=0, row=4, columnspan=2)
enter_n.grid(column=2, row=4)
btn.grid(column=3, row=4)

window.mainloop()
