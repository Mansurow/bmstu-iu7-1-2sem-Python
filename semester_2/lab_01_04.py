from tkinter import *

def transmition(figure):
    figure = str(float(figure))
    figure_arr = figure.split('.')
    print(figure_arr)
    intOfFigure = int(figure_arr[0])
    floatOfFigure = float('0.'+ figure_arr[1])
    arrOf_int = []
    arrOf_float = []
    tras = 0
    while True:
        module = intOfFigure - 4*(intOfFigure//4)
        intOfFigure = intOfFigure//4
        arrOf_int.append(module)
        if intOfFigure < 4:
            arrOf_int.append(intOfFigure)
            break
    figurein4 = ''
    print(arrOf_int)
    for i in range(len(arrOf_int)-1,-1,-1):
        figurein4 += str(arrOf_int[i])
    figurein4 += '.'
    print(floatOfFigure)
    while True:
        floatOfFigure = floatOfFigure * 4
        module = floatOfFigure // 1
        floatOfFigure -= module
        arrOf_float.append(int(module))
        if floatOfFigure % 1 == 0:
            break
    print(arrOf_float)
    for i in range(len(arrOf_float)):
        figurein4 += str(arrOf_float[i])  
    print(figurein4)
    return figurein4
def getDateOfEntry():
    figure = entryFor10.get()
    figure4 = transmition(figure)
    entryFor4.delete(0, END)
    entryFor4.insert(0, figure4)
    
window = Tk()
window.title('Калькулятор перевода')
lbl1 = Label(window, text="Перевод из 10 сс в 16 сс.", font=("Arial Bold", 12))
lbl2 = Label(window, text="Ввод в 10 сс", font=("Arial Bold", 12))
lbl3 = Label(window, text="Вывод в 4 сс", font=("Arial Bold", 12))

entryFor10 = Entry(window)
entryFor4 = Entry(window)
btn = Button(window, text="Перевести", command=getDateOfEntry)

lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
entryFor10.grid(column=0, row=2)
btn.grid(column=0, row=3)
lbl3.grid(column=0, row=4)
entryFor4.grid(column=0, row=5)
window.mainloop()
