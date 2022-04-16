# В файле in.txt записана квадратная целочисленная матрица 
# в следующем формате: N строк по N чисел, разделённых 
# пробелами.
# Необходимо изменить матрицу по следующему правилу: 
# числа, образующие периметр матрицы (внешний квадрат) 
# - сместить по часовой стрелке на 1, затем следующий 
# вложенный квадрат (образованный из 2-й строки, 
# предпоследнего столбца, предпоследней строки и 2-го столбца) 
# - сместить против часовой стрелки на 1, 
# затем следующий вложенный - по часовой стрелке на 1, 
# и так далее до центра матрицы.
# Затем в получившейся матрице требуется найти столбцы с 
# наибольшим элементом матрицы и удалить их.
# Записать в файл out.txt матрицу после первого преобразования, 
# затем пустую строку, затем матрицу с удалённым столбцом.
# Дополнительных матриц не вводить.

def clockwise(arr, n, index):
    for k in range(index, n):
        if n - index == 2:
            if k == index:
                arr[k].insert(index, arr[k + 1][index])
                continue
            elif k == n - 1:
                arr[k].insert(n, arr[k - 1][n])
                del arr[k - 1][n]
                del arr[k][index]
        else:
            if k == index:
                arr[k].insert(index, arr[k + 1][index])
                continue
            elif k == n - 1:
                arr[k].insert(n, arr[k - 1][n])
                del arr[k - 1][n]
            elif index < k < n - 1:
                if k == n - 2:
                    arr[k].insert(n - 1, arr[k - 1][n])
                    del arr[k - 1][n]
                    arr[k][index] = arr[k + 1][index]
                    del arr[k + 1][index]
                else:
                    arr[k][index] = arr[k + 1][index]
                    arr[k].insert(n - 1, arr[k - 1][n])
                    del arr[k - 1][n]
    return arr


def counterclockwise(arr, n, index):
    for k in range(index, n):
        if k == index:
            arr[k].insert(n, arr[k + 1][n - 1])
            continue
        elif k == n - 1:
            arr[k].insert(index, arr[k - 1][index])
            del arr[k - 1][index]
        elif index < k < n - 1:
            if k == n - 2:
                arr[k][n - 1] = arr[k + 1][n - 1]
                del arr[k + 1][n - 1]
                arr[k].insert(index + 1, arr[k - 1][index])
                del arr[k - 1][index]
            else:
                arr[k][n - 1] = arr[k + 1][n - 1]
                arr[k].insert(index + 1, arr[k - 1][index])
                del arr[k - 1][index]
    return arr


with open('in.txt', 'r') as InFile:
    N = len(InFile.readline().split(' '))

matrix = []

with open('in.txt', 'r') as InFile:
    for i in range(N):
        matrix.append(InFile.readline().split(' '))

for i in range(N):
    for j in range(N):
        if matrix[i][j][-1] == '\n':
            matrix[i][j] = matrix[i][j][:-1]

for i in range(N // 2):
    if i % 2 == 0:
        matrix = clockwise(matrix, N - i, i)
    elif i % 2 == 1:
        matrix = counterclockwise(matrix, N - i, i)

with open('out.txt', 'w') as OutFile:
    for i in range(N):
        OutFile.write(' '.join(matrix[i]) + '\n')
    OutFile.write('\n')

    max_dig = 0

    for i in range(N):
        for j in range(N):
            if max_dig < int(matrix[i][j]):
                max_dig = int(matrix[i][j])

    MaxInd = []
    for i in range(N):
        for j in range(N):
            if max_dig == int(matrix[i][j]):
                if j not in MaxInd:
                    MaxInd.append(j)

    for i in range(N):
        ind = 0
        for j in range(N):
            if j in MaxInd:
                del matrix[i][j - ind]
                ind += 1
        OutFile.write(' '.join(matrix[i]) + '\n')
