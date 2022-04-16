try:
    with open('input.txt', 'r+') as file:
        list = []
        symbols = ['.', ',', '!', '?', ':']
        for elem in file:
            elem = elem.split(' ')
            first_el = elem[0]
            if ' ' in first_el: first_el.replace(' ', '')
            for item in elem:
                if ' ' in item: item = item.replace(' ', '')
                if len(item) > len(first_el):
                    first_el = item

            if '\n' in first_el: first_el = first_el.replace('\n', '')
            for elem in symbols:
                if elem in first_el: first_el = first_el.replace(elem, '')
            if first_el != '': list.append(first_el)
            n = 1
            while n < len(list):
                for i in range(len(list) - n):
                    if len(list[i]) > len(list[i + 1]):
                        list[i], list[i + 1] = list[i + 1], list[i]
                n += 1
except FileNotFoundError:
    print('First create the file input.txt')

try:
    with open('ouput.txt', 'w') as file:
        for elem in list:
            file.write(elem + ' [' + str(len(elem)) + ']' + '\n')
except FileNotFoundError:
    print('Repeat again we can not find the file output and we created it')
    open('ouput.txt', 'a').close()
except:
    print()