# Типа дан файл
# Создать функцию, которая создаёт файл состоящий из
# самых длинных слов каждой строки
# И потом отсортировать этот файл по длине слов
# А потом в основной проге найти кол-во используемых символов

try:
    inputFile = open('input.txt','r', encoding='utf-8')
    symbols = ['.', ',', '!', '?', ':']
    text = inputFile.readlines()
    def makeOutFile():
        outputFile = open('output.txt','w')
        for i in text:
            elem = i.split(' ')
            if i == '\n':
                continue
            for j in range(len(elem)):
                if '\n' in elem[j]:
                    elem[j] = elem[j].replace('\n','')
                for symbol in symbols:
                    if symbol in elem[j]:
                        elem[j] = elem[j].replace(symbol,'')
            maxLenght = elem[0]
            for i in elem:
                if len(maxLenght) < len(i):
                    maxLenght = i
            maxLenght = maxLenght + '\n'
            outputFile.write(maxLenght)    
        outputFile.close()
        print('файл с саммыми длинными словами записан output.txt!')
        outputFileRead = open('output.txt','r')
        longWords = outputFileRead.readlines()
        n = 1
        # метод быстрой сортировки
        while n < len(longWords):
            for i in range(len(longWords)- n):
                if len(longWords[i]) > len(longWords[i+1]):
                    longWords[i], longWords[i+1] = longWords[i+1],longWords[i]
            n += 1
        outputFileRead.close()
        outputFileRewrite = open('output1.txt','w')
        for i in longWords:
            outputFileRewrite.write(i)
        print('файл с саммыми длинными словами записан output1.txt по длине рассортирован!')
    makeOutFile()
    print()
    for i in text:
        p = 0
        v = 0
        f = 0
        d = 0
        elem = i.split(' ')
        if i == '\n' or i == '':
                continue
        for j in range(len(elem)):
                if '\n' in elem[j]:
                    elem[j] = elem[j].replace('\n','')
        for j in elem:
           if '.' in j :
               p += 1
           if '!' in j :
               v += 1
           if '?' in j :
               f += 1
           if ':' in j :
               d += 1
        print(*elem)
        print('    В строке', p, '"." ,', v, '"!" ,', f, '"?" ,', d, '":".\n')
    inputFile.close()
except FileNotFoundError:
    print('Файл input.txt не найден!')
