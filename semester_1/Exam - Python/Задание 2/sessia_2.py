with open('input.txt', 'r+') as file:
    num = 0
    dic_el = {}
    list_el = []
    list_un = []
    for elem in file:
        value = num = count = 0
        elem = elem.split(' ')
        for item in elem:
            if item.isalpha() and not (item == item.upper()): num += 1
        if num > 0:
            for item in elem:
                key_1 = ' '.join(elem)
                dic_el[key_1] = value
                if item.isdigit():
                    value += float(item)
                    dic_el[key_1] = value
        else:
            list_un.append([elem, count])
        count += 1
    for key_, val_ in dic_el.items():
        list_el.append([key_, val_])
    n = 1
    while n < len(list_el):
        for i in range(len(dic_el) - n):
            if list_el[i][1] > list_el[i + 1][1]:
                list_el[i], list_el[i + 1] = list_el[i + 1], list_el[i]
        n += 1
    for elem in list_un:
        list_el.insert(elem[1], [' '.join(elem[0])])
with open('ouput.txt', 'w') as file:
    for elem in list_el:
        file.write(elem[0])
