# В текстовом файле in.txt записан текст, в котором 
# есть вещественные числа с фиксированной точкой 
#(числа отделены от слов пробелами).
# В файл out.txt переписать те из них, 
# которые могут быть числами в восьмеричной системе 
# счисления, каждое с новой строки.
# Далее отделить в файле числа пустой строкой и, 
# приняв эти числа числами в восьмеричной системе 
# счисления, записать их в шестнадцатеричной системе 
# счисления по одному в строке (функции hex, int не использовать).
# Целиком файл в память не считывать.

arr = []

with open('in.txt', 'r', encoding='utf-8') as InFile:
    while True:
        line = InFile.readline().split(' ')
        if line == ['']:
            break
        for i in range(len(line)):
            if line[i][-1] == '\n':
                line[i] = line[i][:-1]
        for i in range(len(line)):
            if line[i].isdigit():
                arr.append(line[i])

arr8 = []

for i in range(len(arr)):
    k = 0
    for j in range(len(arr[i])):
        if int(arr[i][j]) < 8:
            k += 1
        else:
            k = 0
            break
    if k != 0:
        arr8.append(arr[i])
    else:
        continue

with open('out.txt', 'w') as OutFile:
    for i in range(len(arr8)):
        OutFile.write(str(arr8[i]) + '\n')
    OutFile.write('\n')

    arr10 = []

    for i in range(len(arr8)):
        n = len(arr8[i]) - 1
        dig10 = 0
        for j in range(len(arr8[i])):
            dig10 += int(arr8[i][j]) * 8**(n - j)
        arr10.append(dig10)

    arr16 = []

    for i in range(len(arr10)):
        dig16 = ''
        if arr10[i] < 16:
            if arr10[i] == 10:
                arr16.append('A')
            elif arr10[i] == 11:
                arr16.append('B')
            elif arr10[i] == 12:
                arr16.append('C')
            elif arr10[i] == 13:
                arr16.append('D')
            elif arr10[i] == 14:
                arr16.append('E')
            elif arr10[i] == 15:
                arr16.append('F')
            else:
                arr16.append(arr10[i])
        else:
            a = arr10[i]
            while True:
                if a % 16 == 10:
                    dig16 = 'A' + dig16
                elif a % 16 == 11:
                    dig16 = 'B' + dig16
                elif a % 16 == 12:
                    dig16 = 'C' + dig16
                elif a % 16 == 13:
                    dig16 = 'D' + dig16
                elif a % 16 == 14:
                    dig16 = 'E' + dig16
                elif a % 16 == 15:
                    dig16 = 'F' + dig16
                else:
                    dig16 = str(a % 16) + dig16
                a = a // 16
                if a < 16:
                    if a == 10:
                        dig16 = 'A' + dig16
                    elif a == 11:
                        dig16 = 'B' + dig16
                    elif a == 12:
                        dig16 = 'C' + dig16
                    elif a == 13:
                        dig16 = 'D' + dig16
                    elif a == 14:
                        dig16 = 'E' + dig16
                    elif a == 15:
                        dig16 = 'F' + dig16
                    else:
                        dig16 = str(a) + dig16
                    break
            arr16.append(dig16)

    for i in range(len(arr16)):
        OutFile.write(arr16[i] + '\n')
