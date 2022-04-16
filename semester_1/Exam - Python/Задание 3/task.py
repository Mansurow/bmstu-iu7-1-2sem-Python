# В файле in.txt записаны строки, длина каждой 
# не превышает 100 символов.
# Столбцом символов в рамках этой задачи 
# считать последовательность символов 
# на одной и той же позиции в каждой строке файла.
# Требуется переписать в файл out.txt 
# содержимое исходного файла так, чтобы туда 
# не попали столбцы из символов #, если они есть. 
# Также к каждой строке через пробел нужно 
# добавить число слов-палиндромов длиной 
# больше одного, которые в ней присутствуют.
# Считывать файл в память целиком нельзя.

inFile = open('in.txt','r', encoding = 'UTF-8')
outFile = open('out.txt','w')

arrOfSymbols = []
arrOfNumberOfPolindrom = []
b = None
while True:
    x = inFile.readline()
    if x == '':
        break
    
    arrOfWorlds = x.split()
    for i in range(len(arrOfWorlds)):
        if '\n' in arrOfWorlds[i]:
            arrOfWorlds[i] = arrOfWorlds[i].replace('\n','')
        if '#' in arrOfWorlds[i]:
            arrOfWorlds[i] = arrOfWorlds[i].replace('#','')
            
    numberOfPolindrom = 0        
    for i in arrOfWorlds:
        if len(i) > 1:
            polindrom = ''
            for j in i:
                polindrom = j + polindrom
            if i.lower() == polindrom.lower():
                numberOfPolindrom += 1
    arrOfNumberOfPolindrom.append(numberOfPolindrom)
    if b == None:
        b = len(x)
        
    if '\n' in x:
        x = x.replace('\n', '')
        
    if arrOfSymbols == []:
        for i in range(len(x)):
            arrOfSymbols.append([x[i]])
    else:
        for j in range(len(x)):
            if j >= len(arrOfSymbols):
                arrOfSymbols.append([])
            if b < len(x) and j >= b:
                arrOfSymbols[j].append('')
            arrOfSymbols[j].append(x[j])
    b = len(x)

for i in arrOfSymbols:
    if '#' in i:
        arrOfSymbols.remove(i)
for i in range(len(arrOfSymbols[0])):
    for j in range(len(arrOfSymbols)):
        if arrOfSymbols[j][i] == '':
            outFile.write(arrOfSymbols[j][i]+ ' '+ str(arrOfNumberOfPolindrom[i]) + '\n')
            break
        elif j == len(arrOfSymbols)-1:
            outFile.write(arrOfSymbols[j][i]+ ' '+ str(arrOfNumberOfPolindrom[i]) + '\n')
            continue
        outFile.write(arrOfSymbols[j][i])
    
inFile.close()
outFile.close()
