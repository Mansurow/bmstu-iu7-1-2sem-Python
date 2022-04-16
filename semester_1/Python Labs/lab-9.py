#Написать программу, реализующую меню:
#1. Ввод строки.
#2. Настройка шифрующего алгоритма.
#3. Шифрование строки, используя шифр Виженера.
#4. Расшифровывание строки.
import string
choice = None

text = ''
key = ''
# словарь для английского алфавита
#---------------------------------------------------
alp_eng = {key: value for key, value in enumerate(string.ascii_letters)}
# словарь для русского алфавита
#---------------------------------------------------
alp_rus = {}
key_rus =0
for value_rus in range(ord('а'),ord('а')+32):
    alp_rus[key_rus] = chr(value_rus)
    key_rus += 1
for value_rus in range(ord('А'),ord('А')+32):
    alp_rus[key_rus] = chr(value_rus)
    key_rus += 1
# Меню
#---------------------------------------------------
print('------ Меню --------')   
print('1-Ввод строки.')
print('2-Настройка шифрующего алгоритма.')
print('3-Шифрование строки, используя шифр Виженера.')
print('4-Расшифровывание строки.')
print('5-Вывод строки.')
print('6-Посмотреть алфавит')
print('0-Выход')

while choice != '0':
    choice = input('Выбор: ') # ввод выбора
    
    # функция сравнения ключа и слов с словарем ключей
    #---------------------------------------------------
    def encode_value(text,alphabet): 
        list_code = []
        
        for letter in text:
            if letter == ' ':
                list_code.append(100)
            for key in alphabet:
                if letter == alphabet[key]:
                    list_code.append(key)
        return list_code

    # функция шифровка слова
    #--------------------------------------------------
    def encode(text,key,alphabet):
        p = encode_value(text,alphabet)
        k = encode_value(key,alphabet)
        j = 0
        b = ''
        for i in range(len(text)):
            if j >= len(key):
                j =0
            if p[i] == 100:
                b += ' '
                continue
            c = (p[i]+k[j])%len(alphabet)
            j += 1
            for v in alphabet.keys():
                if c == v:
                    b += alphabet.get(c)
                if c == 100:
                    b += ' '
        text = b       
        return text

    # функция расшировка слова
    #---------------------------------------------------
    def decode(text,key,alphabet):
        c = encode_value(text,alphabet)
        k = encode_value(key,alphabet)
        j = 0
        b = ''
        for i in range(len(text)):
            if j >= len(key):
                j =0
            if c[i] == 100:
                b += ' '
                continue    
            p = (c[i]-k[j])%len(alphabet)
            j += 1
            for v in alphabet.keys():
                if p == v:
                    b += alphabet.get(p)
        text = b       
        return text
    
    # условия для выбора
    #---------------------------------------------------
    if choice == '1':
        print('Выбирете алфавит.')
        while True:
            alp_choice = input('Введите Еnglish или Русский: ')
            if alp_choice == 'English':
                text = str(input('Ввведите строку: '))
                letter = 0
                for i in range(0,len(text)):
                    if text[i] not in alp_eng.values():
                        if text[i] == ' ':
                            continue
                        letter  += 1
                if letter == 0:
                    break
                else:
                    print('В cлове(ах) есть русские буквы!')
            elif alp_choice == 'Русский':
                text = str(input('Ввведите строку: '))
                letter = 0
                for i in range(0,len(text)):
                    if text[i] not in alp_rus.values():
                        if text[i] == ' ':
                            continue
                        letter  += 1
                if letter == 0:
                    break
                else:
                    print('В cлове(ах) есть английские буквы!')
            else:
                print('Ошибка ввода!!!')
        d = 0 #используется для вывода условия если зашифрован, расшифрован или введен без действий
    #---------------------------------------------------
    elif choice == '2':
        if text == '':
            print('Текст или слова для шифрования не введенно!\n')
            continue
        while True:
            if alp_choice == 'English':
                key = input('Введите ключ для шифрования на Английском: ')# ввод ключа
                letter = 0
                for i in range(0,len(key)):
                    if key[i] not in alp_eng.values():
                        letter  += 1
                if letter == 0:
                    break
                else:
                    print('В ключе есть русские буквы и пробелы!')
            elif alp_choice == 'Русский':
                key = input('Введите ключ для шифрования на Русском: ')# ввод ключа
                letter = 0
                for i in range(0,len(key)):
                    if key[i] not in alp_rus.values():
                        letter  += 1
                if letter == 0:
                    break
                else:
                    print('В ключе есть английские буквы и пробелы!')
            else:
                print('Ошибка ввода!!!')
    #---------------------------------------------------    
    elif choice == '3':
        if text == '' or key ==  '':
            print('Слово или ключ для шифрования не введенно!\n')
            continue
        if alp_choice == 'English':
            text = encode(text,key,alp_eng)
        else:
            text = encode(text,key,alp_rus)
        print('Ваш текс или слово зашифрована:',text)
        d = 1
    #---------------------------------------------------
    elif choice == '4':
        if text == '':
            print('Текст или слова для шифрования не введенно!\n')
            continue
        key = input('Введите ключ: ')
        if alp_choice == 'English':
            text = decode(text,key,alp_eng)
        else:
            text = decode(text,key,alp_rus)
        d = 2
    #---------------------------------------------------
    elif choice == '5':
        if text == '':
            print('Текст или слова для шифрования не введенно!\n')
            continue
        if d == 0:
            print('Ваш текс или слово:',text)
        elif d == 1:
            print('Ваш текс или слово зашифрована:',text)
        elif d == 2:
            print('Ваш текс или слово расшифрована:',text)
        else:
            print('Ошибка!!!')

    #---------------------------------------------------
    elif choice == '6':
        print('Английский алфавит:')
        for i in alp_eng.items():
            print(i)
        print('\nРусский алфавит:')
        for i in alp_rus.items():
            print(i)
    #---------------------------------------------------       
    elif choice == '0':
        print('Выход')
    else:
        print('Введенного номера нет', choice)
    print()
