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
        module = intOfFigure - 16*(intOfFigure//16)
        intOfFigure = intOfFigure//16
        arrOf_int.append(module)
        if intOfFigure < 16:
            arrOf_int.append(intOfFigure)
            break
    figurein16 = ''
    print(arrOf_int)
    for i in range(len(arrOf_int)-1,-1,-1):
        if arrOf_int[i] >= 10:
            if arrOf_int[i] == 10:
                figurein16 += 'A'
            elif arrOf_int[i] == 11:
                figurein16 += 'B'
            elif arrOf_int[i] == 12:
                figurein16 += 'C'
            elif arrOf_int[i] == 13:
                figurein16 += 'D'
            elif arrOf_int[i] == 14:
                figurein16 += 'E'
            elif arrOf_int[i] == 15:
                figurein16 += 'F'
        else:
            figurein16 += str(arrOf_int[i])
    figurein16 += '.'
    print(floatOfFigure)
    while True:
        floatOfFigure = floatOfFigure * 16
        module = floatOfFigure // 1
        floatOfFigure -= module
        arrOf_float.append(int(module))
        if floatOfFigure % 1 == 0:
            break
    print(arrOf_float)
    for i in range(len(arrOf_float)):
        if arrOf_float[i] >= 10:
            if arrOf_float[i] == 10:
                figurein16 += 'A'
            elif arrOf_float[i] == 11:
                figurein16 += 'B'
            elif arrOf_float[i] == 12:
                figurein16 += 'C'
            elif arrOf_float[i] == 13:
                figurein16 += 'D'
            elif arrOf_float[i] == 14:
                figurein16 += 'E'
            elif arrOf_float[i] == 15:
                figurein16 += 'F'
        else:
            figurein16 += str(arrOf_float[i])  
    print(figurein16)
    return figurein16
def getDateOfEntry():
    figure = entryFor10.get()
    figure16 =transmition(figure)
    entryFor16.delete(0, END)
    entryFor16.insert(0, figure16)
    
window = Tk()
window.title('Калькулятор перевода')
lbl1 = Label(window, text="Перевод из 10 сс в 16 сс.", font=("Arial Bold", 12))
lbl2 = Label(window, text="Ввод в 10 сс", font=("Arial Bold", 12))
lbl3 = Label(window, text="Вывод в 16 сс", font=("Arial Bold", 12))

entryFor10 = Entry(window)
entryFor16 = Entry(window)
btn = Button(window, text="Перевести", command=getDateOfEntry)

lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
entryFor10.grid(column=0, row=2)
btn.grid(column=0, row=3)
lbl3.grid(column=0, row=4)
entryFor16.grid(column=0, row=5)
window.mainloop()


