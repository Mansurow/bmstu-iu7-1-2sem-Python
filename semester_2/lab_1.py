'''
    Лабораторная работа №1 (Мансуров В.М, группа ИУ7-26Б, вариант 15)
                          Условие
    Составить приложение, используя модуль создания оконных приложений Tkinter, 
    реализуя индивидуальное задание. Интерфейс должен предоставлять ввод символов:
    как числовых, так и знаковых операций - и с использованием клавитуры и кнопок
    приложения. Также в приложении необходимо создать меню, в котором  должны 
    следующие пункты:
    - заданные действия
    - очистка полей ввода/вывода
    - информация о программе и авторе
    Индивидуальное задание:
    15. Сложение и вычитание вещественных чисел в 6-й системе счисления.
'''

from tkinter import *

#-------------------------------------------------
'''
sumAndSubOfSNS - функция сложения и вычитания с 3 параметрами:
    f_1 - цифра 1 в 6-й сс
    f_2 - цифра 2 в 6-й сс
    symbol - действие сложение или вычитание
arrOfFigure_1 - массив числа f_1 раззделенный на целую и дробную часть
arrOfFigure_2 - массив числа f_2 раззделенный на целую и дробную часть
transitionOfOne - число 0 или 1 используются для перехода в другой разряд чисел если в предущем > 5
N - длина чисел для цикла
sumOfFigures - результат сложение или вычитание двух чисел
summPartes - результат сложение или вычитание одного разряда чисел
'''
def sumAndSubOfSNS(f_1, f_2, symbol):
    f_1 = str(float(f_1))
    f_2 = str(float(f_2))


    arrOfFigure_1 = f_1.split('.')
    arrOfFigure_2 = f_2.split('.')
    transitionOfOne = 0

    # добавляем 0 в целую и дробну часть например если 50.11 и 5 то 50.11 и 05.00
    if len(arrOfFigure_1[0]) > len(arrOfFigure_2[0]):
        f_2 = (len(arrOfFigure_1[0]) - len(arrOfFigure_2[0]))*'0' + f_2
    if len(arrOfFigure_1[0]) < len(arrOfFigure_2[0]):
        f_1 = (len(arrOfFigure_2[0]) - len(arrOfFigure_1[0]))*'0' + f_1

    if len(arrOfFigure_1[1]) > len(arrOfFigure_2[1]):
        f_2 = f_2 + (len(arrOfFigure_1[1]) - len(arrOfFigure_2[1]))*'0'
    if len(arrOfFigure_1[1]) < len(arrOfFigure_2[1]):
        f_1 = f_1 + (len(arrOfFigure_2[1]) - len(arrOfFigure_1[1]))*'0'
    # Условие если одно из чисел отрицательное


    N = len(f_1)
    sumOfFigures = ''
    summPartes = 0
    for i in range(N-1,-1,-1):
        if f_1[i] == '.' or f_2[i] == '.':
            sumOfFigures = '.' + sumOfFigures
            continue
        if symbol == '+':
            summPartes = int(f_1[i]) + int(f_2[i]) + transitionOfOne
            if summPartes >= 6:
                summPartes -= 6
                transitionOfOne = 1
            else:
                transitionOfOne = 0
        else:
            if float(f_1) < float(f_2):
                summPartes = int(f_2[i]) - int(f_1[i]) - transitionOfOne
            if float(f_1) > float(f_2):
                summPartes = int(f_1[i]) - int(f_2[i]) - transitionOfOne

            if summPartes < 0:
                summPartes += 6
                transitionOfOne = 1
            else:
                transitionOfOne = 0
        sumOfFigures = str(summPartes) + sumOfFigures
    # условие если число будет отрицательное
    if float(f_1) < float(f_2) and symbol == '-':
        sumOfFigures = '-' + sumOfFigures
    # условие если результатв цикле получется 50 + 4  = 130 то добавляем, а в цикле 30, поэтому в начало 1 и получаем 120
    if symbol == '+' and transitionOfOne == 1:
        sumOfFigures = '1' + sumOfFigures
    # условие если число получается целое 2.0 то переводим в 2
    if float(sumOfFigures) % 1 == 0:
        sumOfFigures = str(int(float(sumOfFigures)))
    print(sumOfFigures)
    return sumOfFigures

#-----------------------------------------------------
'''
resultOfSumOrSub - функция вывода сложения и вычитание всего вырадения например 2+3+4-1-2.0 
expression - выражение из текстого поля для ввода
expression_arr - массив разденный на числа и знаки "+" и '-' например [2 + 3 + 4 - 1 - 2.0]
number - используются для получения числа до знаков
result - результат функции sumAndSubOfSNS
entryOutput - поле результата
newresult - используются для записи числа без 0 вначале, например 05 то 5
'''
def resultOfSumOrSub():
    expression = entryInput.get()
    expression_arr = []
    number = ''
    countsum = 0
    countsub = 0
    for i in expression:
        if i == '+':
            if expression[0] == '-' and countsum == 0:
                countsum = 1
                expression_arr.append(number)
                expression_arr.append('+')
                number = ''
                continue
            expression_arr.append(number)
            expression_arr.append('+')
            number = ''
            continue
        if i == '-':
            if expression[0] == '-' and countsub == 0:
                countsub = 1
                continue
            expression_arr.append(number)
            expression_arr.append('-')
            number = ''
            continue
        number += i
    expression_arr.append(number)
    if expression[0] == '-':
        expression_arr[0] = '-' + expression_arr[0]
    for j in range(1,len(expression_arr),2):
        if j == 1:
            if expression_arr[j-1][0] == '-' and expression_arr[j] != '-':
                result = sumAndSubOfSNS(expression_arr[j+1], expression_arr[j-1][1:], expression_arr[j-1][0])
            elif expression_arr[j-1][0] == '-' and expression_arr[j] == '-':
                result = sumAndSubOfSNS(expression_arr[j-1][1:], expression_arr[j+1], '+')
                result = '-' + result
            else:
                result = sumAndSubOfSNS(expression_arr[j-1],expression_arr[j+1],expression_arr[j])
        else:
            if result[0] == '-' and expression_arr[j] != '-':
                result = sumAndSubOfSNS(expression_arr[j+1], result[1:], result[0])
            elif result[0] == '-' and expression_arr[j] == '-':
                result = sumAndSubOfSNS(result[1:], expression_arr[j+1], '+')
                result = '-' + result
            else:
                result = sumAndSubOfSNS(result, expression_arr[j+1], expression_arr[j])

    if result[0] == '0' and len(result) > 0 and result[1] != '.':
        print(result)
        newresult = ''
        for i in range(1,len(result)):
            newresult += result[i]
        result = newresult

    entryOutput.delete(0, END)
    if result == '':
        entryOutput.insert(0, '0')
    else:
        entryOutput.insert(0, result)

#-----------------------------------------------------------------------
'''
clearAllEntry - очистка всей полей (ввода и вывода)
entryInput - поле ввода
entryOutput - поле вывода
'''
def clearAllEntry():
    entryInput.delete(0,END)
    entryOutput.delete(0,END)

#----------------------------------------
'''
clearEntryInput - очистка поля ввода
entryInput - поле ввода
'''
def clearEntryInput():
    entryInput.delete(0,END)

#----------------------------------------
'''
clearEntryOutput - очистка поля ввода
entryOutput - поле ввода
'''

def clearEntryOutput():
    entryOutput.delete(0, END)

#----------------------------------------------------
'''
limit - функция ограничения ввода чисел и символов в поле ввода и вывода - параметры:
    text - текст из полей
    action - 0 или 1 
'''
def limit(text, action):
    return action != '1' or not (any(char.isalpha() for char in text) or any(figure  not in '012345.-+' for figure in text))



#----------------------------------------------------
'''
onClickNumber - функция для нажатие кнопки  на панели управления канкулятором и ввод ее значения
buttonValue - полученное значение
'''
def onСlickNumber(event):
    buttonValue = event.widget.cget('text')
    if entryInput.get() == '' and buttonValue == '.':
        entryInput.insert(END, '0.')
    else:
        entryInput.insert(END, buttonValue)

#----------------------------------------
'''
information - функция создания новго окна для пункта меню СПРАВКА
infoOfAuthor - информация об авторе 
infoOfProgram - информация о программе
newWindow - новое подокно
lblOfAuthor, lblOfAuthorInformation, lblOfProgram, lblOfProgramInformation  - переменная для заключени графического элемента - текста
'''
def information():
    infoOfAuthor = "Мансуров Владислав Михайлович студент ИУ7-26Б,\n " \
                   "написал программу используя модуль Tkinter,\n " \
                   "чтобы выполнить лабораторнцю работу."
    infoOfProgram = "Программа выполняет рассчеты сложения и вычитание в шестиричной\n" \
                    "системе счисления при этом результат выводится в отдельном \n" \
                    "текстовом окне.Программа работает с вещественными числами \n" \
                    "и также имеет меню, где есть праметры:\n" \
                    "- заданные действия\n" \
                    "- очистка ввода и ввывода\n" \
                    "- информация об авторе и программе"

    newWindow = Toplevel(window)
    lblOfAuthor = Label(newWindow, text="Автор", font=("Arial Bold", 14, 'bold'))
    lblOfAuthorInformation = Label(newWindow, text=infoOfAuthor, justify=LEFT, font=("Arial Bold", 12))
    lblOfProgram = Label(newWindow, text="Программа", font=("Arial Bold", 14, 'bold'))
    lblOfProgramInformation = Label(newWindow, text=infoOfProgram, justify=LEFT, font=("Arial Bold", 12))
    lblOfAuthor.grid(column=0, row=0)
    lblOfAuthorInformation.grid(column=0, row=1)
    lblOfProgram.grid(column=0, row=2)
    lblOfProgramInformation.grid(column=0, row=3)
    newWindow.title('Справка')
    newWindow.minsize(width=525, height=300)
    newWindow.maxsize(width=525, height=300)

window = Tk()
window.title('Калькулятор систем счисления')
#-------------------------------------
# - МЕНЮ и его пункты
main_menu = Menu(window)
clear_submenu = Menu(main_menu)
do_submenu = Menu(main_menu)
do = Menu(do_submenu)
figures = Menu(do_submenu)
window.config(menu=main_menu)

main_menu.add_cascade(label='Файл', menu=do_submenu)
do_submenu.add_cascade(label='Действия', menu=do)
do.add_command(label='clear', command=lambda: entryInput.delete(0,END))
do.add_command(label='⌫', command=lambda: entryInput.delete(len(entryInput.get())-1))
do.add_command(label='+', command=lambda: entryInput.insert(END,'+'))
do.add_command(label='-', command=lambda: entryInput.insert(END,'-'))
do.add_command(label='=', command=resultOfSumOrSub)
do_submenu.add_cascade(label='Цифры', menu=figures)
figures.add_command(label='0', command=lambda: entryInput.insert(END,'0'))
figures.add_command(label='1', command=lambda: entryInput.insert(END,'1'))
figures.add_command(label='2', command=lambda: entryInput.insert(END,'2'))
figures.add_command(label='3', command=lambda: entryInput.insert(END,'3'))
figures.add_command(label='4', command=lambda: entryInput.insert(END,'4'))
figures.add_command(label='5', command=lambda: entryInput.insert(END,'5'))
do_submenu.add_command(label='Выход', command=window.destroy)
main_menu.add_cascade(label='Очистить', menu=clear_submenu)
clear_submenu.add_command(label='Все поля', command=clearAllEntry)
clear_submenu.add_command(label='Ввод',  command=clearEntryInput)
clear_submenu.add_command(label='Вывод', command=clearEntryOutput)
main_menu.add_command(label='Справка', command=information)
#-------------------------------------
# - поля ввода и вывода и текстовые элементы
lbl1 = Label(window, text="Сложение и вычитание в 6-й системе счисления.", font=("Arial Bold", 12))
lbl2 = Label(window, text='Результат', font=("Arial Bold", 12))

entryInput = Entry(window, width=23, relief='groove', font=14)
entryInput.focus_set()
entryOutput = Entry(window, width=20, font=14)
entryInput.config(validate='key', validatecommand=(entryInput.register(limit), '%P', '%d'))
entryOutput.config(validate='key', validatecommand=(entryOutput.register(limit), '%P', '%d'))
#----------------------------------


#-----------------------------
# Кнопки управления панелью калькулятора
btn = Button(window, text="=", bg='#4587DB', fg='white', width=2, height=3, font=("Arial Bold", 14, 'bold'), relief='groove', command=resultOfSumOrSub)
btnfordel = Button(window, text="C", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', command=lambda: entryInput.delete(0,END))
btnford = Button(window, text="/", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', state='disabled')
btnform = Button(window, text="*", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', state='disabled')
btnforsum = Button(window, text="+", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnforsub = Button(window, text="-", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfordelonesymbol = Button(window, text="⌫", bg='#D5D5D5', fg='#4587DB', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', command=lambda: entryInput.delete(len(entryInput.get())-1))
btnfor0 = Button(window, text="0", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfor1 = Button(window, text="1", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfor2 = Button(window, text="2", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfor3 = Button(window, text="3", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfor4 = Button(window, text="4", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnfor5 = Button(window, text="5", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove' )
btnfor6 = Button(window, text="6", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove' , state='disabled')
btnfor7 = Button(window, text="7", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove' , state='disabled')
btnfor8 = Button(window, text="8", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16,'bold'), relief='groove' , state='disabled')
btnfor9 = Button(window, text="9", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove' , state='disabled')
btnforA = Button(window, text="A", bg='white', fg='black', width=5, height=1, font=("Arial Bold", 15, 'bold'), relief='groove', state='disabled')
btnforB = Button(window, text="B", bg='white', fg='black', width=5, height=1, font=("Arial Bold", 15, 'bold'), relief='groove' , state='disabled')
btnforC = Button(window, text="C", bg='white', fg='black', width=5, height=1, font=("Arial Bold", 15, 'bold'), relief='groove', state='disabled')
btnforD = Button(window, text="D", bg='white', fg='black', width=5, height=1, font=("Arial Bold", 15, 'bold'), relief='groove', state='disabled')
btnforE = Button(window, text="E", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', state='disabled')
btnforF = Button(window, text="F", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', state='disabled')
btnforpoint = Button(window, text=".", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove')
btnforpercent = Button(window, text="%", bg='white', fg='black', width=2, height=1, font=("Arial Bold", 16, 'bold'), relief='groove', state='disabled')


btnfor0.bind('<Button-1>', onСlickNumber)
btnfor1.bind('<Button-1>', onСlickNumber)
btnfor2.bind('<Button-1>', onСlickNumber)
btnfor3.bind('<Button-1>', onСlickNumber)
btnfor4.bind('<Button-1>', onСlickNumber)
btnfor5.bind('<Button-1>', onСlickNumber)
btnforsum.bind('<Button-1>', onСlickNumber)
btnforsub.bind('<Button-1>', onСlickNumber)
btnforpoint.bind('<Button-1>', onСlickNumber)
#-----------------------------
# - расположение всех графических элементов на окне
lbl1.grid(column=0, row=0, columnspan=8)
entryInput.grid(column=0, row=1, columnspan=6, rowspan=2)
lbl2.grid(column=7, row=1)
entryOutput.grid(column=7, row=2,)
btnforA.grid(column=0, row=3, columnspan=2)
btnfordel.grid(column=2, row=3)
btnford.grid(column=3, row=3)
btnform.grid(column=4, row=3)
btnfordelonesymbol.grid(column=5, row=3)
btnforB.grid(column=0, row=4, columnspan=2)
btnfor7.grid(column=2, row=4)
btnfor8.grid(column=3, row=4)
btnfor9.grid(column=4, row=4)
btnforsub.grid(column=5, row=4)
btnforC.grid(column=0, row=5, columnspan=2)
btnfor4.grid(column=2, row=5)
btnfor5.grid(column=3, row=5)
btnfor6.grid(column=4, row=5)
btnforsum.grid(column=5, row=5)
btnforD.grid(column=0, row=6, columnspan=2)
btnfor1.grid(column=2, row=6)
btnfor2.grid(column=3, row=6)
btnfor3.grid(column=4, row=6)
btnforE.grid(column=0, row=7)
btnforF.grid(column=1, row=7)
btnforpercent.grid(column=2, row=7)
btnfor0.grid(column=3, row=7)
btnforpoint.grid(column=4, row=7)
btn.grid(column=5, row=6, rowspan=2)
#---------------------------------------
# размеры главного окна
window.minsize(width=405, height=280)
window.maxsize(width=405, height=280)
window.mainloop()
