# Практика
# Мансуров Владислав Михайлович ИУ7-16Б
# Условие задания:
# n - число компаний 1 <= n <= 400

# inputFail - открытие файла INPUT.txt для чтения
# outputFail - открытие файла OUTPUT.txt для перезаписи или создания
# numberOfCompany - количество компания взятых с первой линнии INPUT.txt
# matrixEarningsOfLand - квадратная матрица данных о заработке компания за земли
# maxElement - максимальный элемент matrixEarningsOfLand
# indexOfCompany - индекс компания от 0
# indexOfLand - индекс земель от 0
# x_break - переменная для выхода из цикла при выполнения условия при = 1
# arrOfAssignedLands - массив упорядоченных элементов присвоенных земель по индексу компаний

# Функция которая ищет для каждой компании подходящую землю 
def takeLandtoCompany (matrix):
    maxElement = matrix[0][0]
    indexOfCompany = 0
    indexOfLand = 0
    
    for i in range(numberOfCompany):
        for j in range(numberOfCompany):
            if matrix[i][j] > maxElement:
                maxElement = matrix[i][j]
                indexOfCompany = i
                indexOfLand  = j
                
    for i in range(len(matrix)):
        if i == indexOfCompany:
            for j in range(len(matrix)):
                matrix[i][j] = -1
        matrix[i][indexOfLand] = -1
    
    return matrix, indexOfLand, indexOfCompany

# Вывод матрицы 
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print('{:^6g}'.format(j),end='')
        print()
    print()

try:
    x_break = 0
    inputFile = open('INPUT.txt', 'r')
    ouputFile = open('OUTPUT.txt','w')
    
    numberOfCompany = int(inputFile.readline())
    print('Число компаний претендующих на земли в городе:',numberOfCompany)
    # создаем нулевую матрицу порядка n
    matrixEarningsOfLand = [[0]*numberOfCompany for i in range(numberOfCompany)]
    
    for i in range(numberOfCompany):
        row = inputFile.readline()
        if '\n' in row:
            row = row.replace('\n', '')
        arrOfRow = row.split(' ')
        for j in range(len(arrOfRow)):
            if len(arrOfRow) != numberOfCompany or len(matrixEarningsOfLand) != numberOfCompany:
                x_break = 1
                print('В файле INPUT.txt матрица данных должны быть квадратной!')
                print('Ошибка в', i+1, 'cтроке:', *arrOfRow)
                break
            try:
                if float(arrOfRow[j]) == int(float(arrOfRow[j])):
                    matrixEarningsOfLand[i][j] = int(float(arrOfRow[j]))
                else:
                    matrixEarningsOfLand[i][j] = float(arrOfRow[j])
            except ValueError:
                x_break = 1
                print('В файле INPUT.txt матрица должна состоять из цифр!')
                break
        if x_break == 1 :
            break
    
    if x_break != 1:
        print('Матрица данных о доходе компаний на земли a_ij,\nгде i - номер компании j - номер земли.')
        printMatrix(matrixEarningsOfLand)
        arrOfAssignedLands = [0 for i in range(numberOfCompany)] # cоздаем нулевой массив
        for i in range(numberOfCompany):
            matrixEarningsOfLand, indexOfLand, indexOfCompany = takeLandtoCompany(matrixEarningsOfLand)
            for j in range(numberOfCompany):
                if j == indexOfCompany:
                    arrOfAssignedLands [j] = indexOfLand + 1
        
        for i in range(len(arrOfAssignedLands)) :
            print('"', i+1,'"-ая компания получает "', arrOfAssignedLands[i], '"-ую землю.')
            ouputFile.write(str(arrOfAssignedLands[i]) + ' ')
        print('Данные записаны в файл OUTPUT.txt как -', *arrOfAssignedLands)
except ValueError:
    print('В файле INPUT.txt первая линия должна быть одно целое число!')
except FileNotFoundError:
    print('Файл INPUT.txt не был найден.')
    
inputFile.close()
ouputFile.close()



