def actMatrix():
    matrix = [['a', 'y', 'i'], ['g', 'y', 'e'], ['o', 'o', 'q']]
    for elem in matrix:
        for item in elem:
            print(item, end=' ')
        print()
    print()
    dic = {}
    val_l = ['a', 'e', 'i', 'o', 'u', 'y']
    max_in = -1
    max_val = 0
    counter = 0
    for elem in range(len(matrix)):
        for item in range(len(matrix[0])):
            if matrix[item][elem] in val_l:
                counter += 1
        dic[elem] = counter
        counter = 0
    for elem, item in dic.items():
        if max_val < item:
            max_in = elem
            max_val = item
    for elem in range(len(matrix)):
        if elem == max_in:
            for item in range(len(matrix)):
                matrix[item].remove(matrix[item][elem])
    for elem in matrix:
        for item in elem:
            print(item, end=' ')
        print()


actMatrix()
