from tkinter import *
import tkinter.messagebox as ms
from math import *

global arr_1
arr = []

def point(x, y, fill, w):
    canvas.create_line(x, y, x + 1, y, fill=fill, width=w)
    canvas.create_line(x, y + 1, x, y, fill=fill, width=w)

def paint(event):
    r = 50
    x, y = (event.x), (event.y)
    x_1 = x - r
    x_2 = x + r
    y_1 = y - r
    y_2 = y + r
    canvas.create_oval(x_1, y_1, x_2, y_2, outline="black")
    point(x, y, 'blue', 5)
    point(x + r, y, 'red', 5)
    point(x - r, y, 'red', 5)
    point(x, y + r, 'red', 5)
    point(x, y - r, 'red', 5)
    arr.append([x, y])
def clear_canvas():
    canvas.delete("all")
    arr.clear()

def find_circle():
    r_c = 50;
    count_1 = 0
    count_2 = 0
    circle_1 = []
    circles = []
    n = len(arr)
    for i in range(n):
        x = arr[i][0]
        y = arr[i][1]
        r_1 = (x + r_c)**2 + y**2
        j = 0
        while(j < n):
            if (j != i):
                x0 = arr[j][0]
                y0 = arr[j][1]
                if ((x0 + r_c)**2 + y0**2 <= r_1) or ((x0 - r_c)**2 + y0**2 <= r_1) or (x0**2 + (y0 + r_c)**2 <= r_1) or (x0**2 + (y0 - r_c)**2 <= r_1):
                    count_1 += 1
            j += 1
        
        if (count_1 > count_2):
           print(count_1, count_2)
           count_2 = count_1
           count_1 = 0
           circle_1 = arr[i]
    if len(circle_1) != 0:
        canvas.create_oval(circle_1[0] - r_c, circle_1[1] - r_c, circle_1[0] + r_c, circle_1[1] + r_c, outline="blue", width=2)
window = Tk()
window.title("Решение планиметрических задач")
canvas = Canvas(window, width=800, height=600, bg='white')
btn_opr = Button(window, text = "Отметить круг", command=find_circle)
lbl_task = Label(window, text="Отметьте круг который больше пересечений")
btn_clear = Button(window, text="Очистить", command=clear_canvas)

canvas.grid(column=0, row=0, columnspan=4, rowspan=50)
lbl_task.grid(column=5, row=0, columnspan=4)
btn_opr.grid(column=5, row=1, columnspan=4)
btn_clear.grid(column=5, row=2, columnspan=4)
canvas.bind("<Button-1>", paint)
window.mainloop()
