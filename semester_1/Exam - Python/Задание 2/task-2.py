# Есть файл, в нем строки содержащие латинские буквы и числа.
# Нужно написать функцию, которая формирует файл в котором будут буквы
# из строк отсортированные по сумме чисел в исходном файле в этой строке.
# А если в строке только заглавные буквы и числа, то тогда оставить эти строки
# на тех местах, где они стояли изначально.

try:
    inputFile = open('input.txt','r', encoding='utf-8')
    def makeOutput():
        arrOfSumm = []
        arr = inputFile.readlines()
        print('Полученные данные:')
        for i in range(len(arr)):
            print('   ' + str(i+1) + ' - ' + arr[i])
        list_el = [0 for i in range(len(arr))]
        for elem in arr:
            n = 0
            summ = 0
            elem_i = elem.split(' ')
            for i in elem_i:  
                if i == i.upper():
                    n += 1
            if n != len(elem_i):
                for j in elem_i:
                    try:
                        j = float(j)
                        summ += j
                     
                    except ValueError:
                        continue
                arrOfSumm.append([summ, elem])
            else:
                for i in range(len(list_el)):
                    if i == arr.index(elem):
                        list_el[i] = elem
    
        n = 1
        while n < len(arrOfSumm):
            for i in range(len(arrOfSumm) - n):
                if arrOfSumm[i][0] > arrOfSumm[i + 1][0]:
                    arrOfSumm[i], arrOfSumm[i + 1] = arrOfSumm[i + 1], arrOfSumm[i]
            n += 1
        n = -1
        for i in range(len(list_el)):
            if list_el[i] == 0:
                n += 1
                list_el[i] = arrOfSumm[n][1]
                

        outputFile = open('output.txt','w')
        print('\nПреобразованные данные:')
        for i in range(len(list_el)):
            if '\n' not in list_el[i]:
                list_el[i] += '\n'
            print('   ' + str(i+1) + ' - '+ list_el[i])
            outputFile.write(list_el[i])
        outputFile.close()
    makeOutput()
    inputFile.close()
except FileNotFoundError:
    print('Файл input.txt не найден!')
