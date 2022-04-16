InFile = open('in.txt', 'r', encoding='utf-8')
OutFile = open('out.txt', 'w', encoding='utf-8')

sym = ['<', '>', '^', 'v']
matrix = []

for line in InFile:
    matrix.append(line.split(' '))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j][-1] == '\n':
            matrix[i][j] = matrix[i][j][:-1]
k_all = 0
index = 0
for i in matrix:
    print(i)
print()
for i in range(len(matrix)):
    k_line = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] in sym:
            k_line += 1
    if k_line > k_all:
        index = i
        k_all = k_line

count = []

for i in range(len(matrix[0])):
    if matrix[index][i] == '<':
        count.append(str(i + 1))
    elif matrix[index][i] == '>':
        count.append(str(len(matrix[0]) - i))
    elif matrix[index][i] == 'v':
        count.append(str(len(matrix) - index))
    elif matrix[index][i] == '^':
        count.append(str(index + 1))
    else:
        count.append('0')

matrix.append(count)
for i in range(len(matrix)):
    OutFile.write(' '.join(matrix[i]) + '\n')
OutFile.write('\n')    
for i in matrix:
    print(i)
print()
for k in range(len(matrix)):
    for j in range(len(matrix[0])-1-k):
        if matrix[len(matrix)-1][j] > matrix[len(matrix)-1][j+1]:
            for i in range(len(matrix)):
                matrix[i][j+1],matrix[i][j] = matrix[i][j],matrix[i][j+1]
for i in matrix:
    print(i)
for i in range(len(matrix)):
    OutFile.write(' '.join(matrix[i]) + '\n')

InFile.close()
OutFile.close()
