# Даны 2 текстовых файла in1.txt и in2.txt в которые записаны
# неубывающие последовательности натуральных чисел (по одному числу в строке
# не превышая 3000)
# Не используя  списки и методы сортировки а также считая файлы в память
# сформировать out.txt с числами в которой все числа в неубывающей 
# последовательности из исходных файлов.
# Сформировать out1.txt в который записать римские представления чисел 
# из файла out.txt выравнивая по центру

in1 = open('in1.txt', 'r')
in2 = open('in2.txt', 'r')
out = open('out.txt', 'w')
out1 = open('out1.txt', 'w')
def takeslesh(n):
   try:
       if n != '' and n != ' ':
            n = n.replace('\n','')
            n = int(n)
   except ValueError:
       pass
   return n

n1 = in1.readline()
n2 = in2.readline()
n1 = takeslesh(n1)
n2 = takeslesh(n2)

print('Что записали в out.txt!!!')
while True:
    if n1 == '' and n2 == '':
        break
    if n1 == '':
        while n2 != '':
            print(n2)
            out.write(str(n2) + '\n')
            n2 = in2.readline()
            n2 = takeslesh(n2)
    elif n2 == '':
        while n1 != '':
            print(n1)
            out.write(str(n1) + '\n')
            n1 = in1.readline()
            n1 = takeslesh(n1)
    else:
        if n1 < n2:
            print(n1)
            out.write(str(n1) + '\n')
            n1 = in1.readline()
            n1 = takeslesh(n1)
        elif n1 > n2:
            print(n2)
            out.write(str(n2) + '\n')
            n2 = in2.readline()
            n2 = takeslesh(n2)
        elif n1 == n2:
            print(n1)
            out.write(str(n1) + '\n')
            n1 = in1.readline()
            n2 = in2.readline()
            n1 = takeslesh(n1)
            n2 = takeslesh(n2)

out.close()
in1.close()
in2.close()


out = open('out.txt', 'r')
print('\nЧто записали в out1.txt!!')
for i in out:
    i = takeslesh(i)
    j = ''
    # тысячные до 3000
    M = i // 1000
    if M == 3:
        j += 'MMM'
    if M == 2:
        j += 'MM'
    if M == 1:
        j += 'M'
        
    # сотни 
    D = i // 100
    if D > 9:
        c = D // 10
        D = D - 10*c
        
    if D == 9:
        j += 'CM'
    if D == 8:
        j += 'DCCC'
    if D == 7:
        j += 'DCC'
    if D == 6:
        j += 'DC'
    if D == 5:
        j += 'D'
    if D == 4:
        j += 'CD'
    if D == 3:
        j += 'CCC'
    if D == 2:
        j += 'CC'
    if D == 1:
        j += 'C'
    # десятки
    X = i // 10
    if X > 9:
        c = X // 10
        X = X - 10*c
        
    if X == 9:
        j += 'XC'
    if X == 8:
        j += 'XLLL'
    if X == 7:
        j += 'XLL'
    if X == 6:
        j += 'XL'
    if X == 5:
        j += 'L'
    if X == 4:
        j += 'XL'
    if X == 3:
        j += 'XXX'
    if X == 2:
        j += 'XX'
    if X == 1:
        j += 'X'
    # еденицы   
    I = i
    if I > 9:
        c = I // 10
        I = I - 10*c
        
    if I == 9:
        j += 'IX'
    if I == 8:
        j += 'VIII'
    if I == 7:
        j += 'VII'
    if I == 6:
        j += 'VI'
    if I == 5:
        j += 'V'
    if I == 4:
        j += 'IV'
    if I == 3:
        j += 'III'
    if I == 2:
        j += 'II'
    if I == 1:
        j += 'I'
    print('{:^10}'.format(j))
    out1.write('{:^10}\n'.format(j))
          
out1.close()
