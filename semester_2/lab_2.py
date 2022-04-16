from tkinter import *
import tkinter.messagebox as mg
from random import *
import timeit

def limit(text, action):
    return action != '1' or not (any(char.isalpha() for char in text) or any(figure not in '1234567890' for figure in text))

def create_arr(size):
    arr = []
    for i in range(size):
        x = randint(-size, size)
        arr.append(x)
    return arr

def shell_sort_increase(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
                arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return arr

def shell_sort_decrease(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] < el:
                arr[i] = arr[i - inc]
                i -= inc
                arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return arr

def table(row, col, value, lgt):
    lenght = len(value)
    for i in range(lenght):
        if col == 0:
            b = Text(window, width=lgt[0], height=lgt[1], font=("Arial Bold", 12, "bold"))
        else:
            b = Text(window, width=lgt[2], height=lgt[3], font=("Arial Bold", 12))
        b.insert(1.0, value[i])
        b["state"] = "disabled"
        b.grid(row=(row + i), column=col)

def click_button():

    
    if input1_entry.get() == '' or int(input1_entry.get()) < 5 or int(input1_entry.get()) > 10:
        mg.showwarning("Error! ENTRY - FIRST ARRAY", "Предупреждение! Размер первого массива не введен или указан неверно!")
        flag = False

    elif input2_entry.get() == '' or int(input2_entry.get()) < 10 or int(input2_entry.get()) > 50:
        mg.showwarning("Error! ENTRY - SECOND ARRAY", "Предупреждение! Размер второго массива не введен или указан неверно!")
        flag = False

    elif input3_entry.get() == '' or int(input3_entry.get()) < 50 or int(input3_entry.get()) > 100:
        mg.showwarning("Error! ENTRY - THIRD ARRAY", "Предупреждение! Размер третьего массива не введен или указан неверно!")
        flag = False

    else:
        print("\nДемонстрация работы")
        size_arr_1 = int(input1_entry.get())
        size_arr_2 = int(input2_entry.get())
        size_arr_3 = int(input3_entry.get())

        arr = create_arr(size_arr_1)
        lbl_dem = Label(window, text="Демонстрация работоcпособности программы.", font=("Arial Bold", 13, "bold"))
        lbl_random_arr = Label(window, text="Случайный массив -", font=("Arial Bold", 11, "italic"))
        lbl_random_arr_v = Text(window, width=20, height=1, font=("Arial Bold", 12))
        lbl_random_arr_v.insert(1.0, arr)
        lbl_random_arr_v["state"] = "disabled"
        print(arr)
        arr = shell_sort_increase(arr)
        lbl_in_arr = Label(window, text="Упорядочный массив - ", font=("Arial Bold", 11, "italic"))
        lbl_in_arr_v = Text(window, width=20, height=1, font=("Arial Bold", 12))
        lbl_in_arr_v.insert(1.0, arr)
        lbl_in_arr_v["state"] = "disabled"
        print(arr)
        arr = shell_sort_decrease(arr)
        lbl_dec_arr = Label(window, text="Обратно-упорядочный массив - ", font=("Arial Bold", 11, "italic"))
        lbl_dec_arr_v = Text(window, width=20, height=1, font=("Arial Bold", 12))
        lbl_dec_arr_v.insert(1.0, arr)
        lbl_dec_arr_v["state"] = "disabled"
        print(arr)

        lbl_dem.grid(column=0, row=5, columnspan=3)
        lbl_random_arr.grid(column=0, row=6)
        lbl_random_arr_v.grid(column=1, row=6, columnspan=2)
        lbl_in_arr.grid(column=0, row=7)
        lbl_in_arr_v.grid(column=1, row=7, columnspan=2)
        lbl_dec_arr.grid(column=0, row=8)
        lbl_dec_arr_v.grid(column=1, row=8, columnspan=2)
        table(9, 0, ['', 'Случайный массив', 'Упорядочный массив', 'Обратно-упорядочный массив'], [40, 2, 10, 2])

        print("\nТаблица времени.")
        arr_of_size = [size_arr_1, size_arr_2, size_arr_3]
        for j in range(1,4):
            l = 'N' + str(j)
            arr_of_m = [l]

            start_time = timeit.default_timer()
            arr = create_arr(arr_of_size[j-1])
            alg_time = timeit.default_timer() - start_time
            arr_of_m.append(round(alg_time, 6))
            print('\n' + arr_of_m[0], arr, round(alg_time, 6))

            start_time = timeit.default_timer()
            arr = shell_sort_increase(arr)
            alg_time = timeit.default_timer() - start_time
            arr_of_m.append(round(alg_time, 6))
            print(arr_of_m[0], arr, round(alg_time, 6))

            start_time = timeit.default_timer()
            arr = shell_sort_decrease(arr)
            alg_time = timeit.default_timer() - start_time
            arr_of_m.append(round(alg_time, 6))
            print(arr_of_m[0], arr, round(alg_time, 6))

            table(9, j, arr_of_m, [40, 2, 10, 2])

window = Tk()
window.title("Метод Шелла(SHELL SORT)")
main_label = Label(window, text="Упорядочение массива методом Шелла(SHELL SORT).", font=("Arial Bold", 13, "bold"))
lbl1 = Label(window, text="Введите размер первого массива 5-10:", font=("Arial Bold", 11, "italic"))
lbl2 = Label(window, text="Введите размер второго массива 10-50:", font=("Arial Bold", 11, "italic"))
lbl3 = Label(window, text="Введите размер третьего массива 50-100:", font=("Arial Bold", 11, "italic"))

btn = Button(window, text="Начать", font=("Arial Bold", 12), command=click_button)
input1_entry = Entry(window)
input2_entry = Entry(window)
input3_entry = Entry(window)
input1_entry.config(validate='key', validatecommand=(input1_entry.register(limit), '%P', '%d'))
input2_entry.config(validate='key', validatecommand=(input2_entry.register(limit), '%P', '%d'))
input3_entry.config(validate='key', validatecommand=(input3_entry.register(limit), '%P', '%d'))
main_label.grid(column=0 , row=0, columnspan=3)          
lbl1.grid(column=0, row=1)
input1_entry.grid(column=1, row=1, columnspan=2)
lbl2.grid(column=0, row=2)
input2_entry.grid(column=1, row=2, columnspan=2)
lbl3.grid(column=0, row=3)
input3_entry.grid(column=1, row=3, columnspan=2)
btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
