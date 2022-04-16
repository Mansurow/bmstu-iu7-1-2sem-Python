from tkinter import *

def bubblesort_with_flag_increase(arr):
    n = len(arr)
    for i in range(n-1):
        flag = True
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j +  1], arr[j]
                flag = False
        if flag:
            break
    return arr


def bubblesort_with_flag_decrease(arr):
    n = len(arr)
    for i in range(n-1):
        flag = True
        for j in range(n-1-i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j +  1], arr[j]
                flag = False
        if flag:
            break
        
    return arr

def limit(text, action):
    return action != '1' or not (any(char.isalpha() for char in text) or any(figure not in '1234567890 -' for figure in text))

def click():
    str_arr = n_entry.get()
    str_arr = str_arr.split(' ')
    arr = []
    for i in str_arr:
        arr.append(int(i))
    print(arr)
    arr = bubblesort_with_flag_increase(arr)
    print(arr)
    lbl_in_arr['state'] = 'normal'
    lbl_in_arr.delete(0.0, END)
    lbl_in_arr.insert(1.0, arr)
    lbl_in_arr['state'] = 'disable'

    arr = bubblesort_with_flag_decrease(arr)
    print(arr)
    lbl_dec_arr['state'] = 'normal'
    lbl_dec_arr.delete(0.0, END)
    lbl_dec_arr.insert(1.0, arr)
    lbl_dec_arr['state'] = 'disable'
window = Tk()
window.title("Сортировка пузырька с флагом.")

n_lbl = Label(window, text="Введите массив через пробел(1 2 3 4 5):", font=("Arial Bold", 11, "italic"))
n_entry = Entry(window)
n_entry.config(validate='key', validatecommand=(n_entry.register(limit), '%P', '%d'))
n_btn = Button(window, text="Начать", font=("Arial Bold", 12), command=click)
lbl_inc = Label(window, text="Упорядочный массив -", font=("Arial Bold", 11, "italic"))
lbl_dec = Label(window, text="Обратно-упорядочный массив -", font=("Arial Bold", 11, "italic"))
lbl_in_arr = Text(window, width=20, height=1, font=("Arial Bold", 12), state="disable")
lbl_dec_arr = Text(window, width=20, height=1, font=("Arial Bold", 12), state="disable")


n_lbl.grid(column=0, row=0)
n_entry.grid(column=1, row=0)
n_btn.grid(column=1,row=1)
lbl_inc.grid(column=0, row=2)
lbl_in_arr.grid(column=1, row=2)
lbl_dec.grid(column=0, row=3)
lbl_dec_arr.grid(column=1, row=3)
window.mainloop()
