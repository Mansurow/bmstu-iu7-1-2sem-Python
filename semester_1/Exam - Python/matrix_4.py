import math

list_el = [1, 2, 3, 4, 5, 8, 7, 9, 10, 12, 11, 13, 14, 15, 15, 14, 13, 11, 17, 10, 9, 7, 3, 5, 4, 3, 2, 1]
print(list_el)
z = []
for elem in range(len(list_el)):
    if elem <= len(list_el):
        if list_el.count(list_el[elem]) > 1:
            if not(list_el[elem] in z):
                z.append(list_el[elem])

dic = {}
list_r = []
counter = index_el = 0
for elem in range(len(list_el)):
    if len(list_el) > 1:
        if list_el[index_el] == list_el[-(index_el + 1)]:
            counter += 1
            index_el += 1
            if index_el == math.floor((len(list_el) - 1) / 2):
                list_r = list_el[:index_el + 1] + list_el[-(index_el + 1):]
                dic[counter] = list_r
                break
        else:
            list_r = list_el[:index_el + 1] + list_el[-(index_el + 1):]
            dic[counter] = list_r
            list_el = list_el[index_el + 1:-(index_el + 1)]
            counter = index_el = 0
index_el = 0
print(dic)
print()
for elem, item in dic.items():
    if elem > index_el:
        index_el = elem
        list_r = item
print(list_r)
print()
print(z)
