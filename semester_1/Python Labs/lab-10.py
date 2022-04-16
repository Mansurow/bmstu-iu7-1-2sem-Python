text = ['Она несла в руках 35+66*9/11 отвратительная, тревожные желтые цветы 35-68*10/21. Черт их знает, как их зовут, но они первые почему-то',
        '35-68*10/15 появляются в Москве. И эти цветы очень отчетливо выделялись на черном ее',
        'вессеннем пальто. Она несла нам желтые цветы. Нехороший цвет но выразительный. Она повернула с Тверской в',
        'переулок и тут обернулась. Ну, Тверскую вы знаете. По Тверской шли тысячи людей, но я вам',
        'ручаюсь, что 35+68*10/21 увидела она меня одного и поглядела н ето что тревожно а даже как будто',
        'болезненно.']

choice = None
print('Текст для работы:')
print(text)
print()

print('--------------МЕНЮ-----------------')
print('1 - Выравнивание текста по левому краю.')
print('2 - Выравнивание текста по правому краю.')
print('3 - Выравнивание текста по ширине.')
print('4 - Удаление заданного слова.')
print('5 - Замена одного слова другим во всем тексте')
print('6 - Вычисление арифметического выражения')
print('7 - Удалить самое длинное слово в самом коротком по числу предложении.')
print('0 - Выход')

while choice != '0':
    choice = input('Выбор: ')

    #---------------------------------------------------------------------------
    #Удаление заданного слова из текста
    # delElem - удаляемое слово
    # delElemLower - все слово становится с маленькими буквами
    # n - количество удаленных слов
    def deleteWord(arr):
        delElem = input('Введите слово которое нужно удалить из текста: ')
        n = 0
        
        for i in range(len(arr)):
            arrLower = []
            delElemLower = delElem.lower()
            arr_i = arr[i].split(' ')
            for k in arr_i:
                if k == ' ':
                    continue
                arrLower.append(k.lower())
            arr[i] = ''
            for j in range(len(arr_i)):
                if delElemLower + '.' == arrLower[j]:
                   arr[i] += '. '
                   n += 1
                   continue
                if delElemLower == arrLower[j] or delElemLower + ',' == arrLower[j]: #or delElemLower + '.' == arrLower[j]:
                    n += 1
                    continue
                if arr_i[j] == arr_i[-1]:
                    arr[i] += arr_i[j]
                    continue
                arr[i] += arr_i[j] + ' '                
        return arr, n, delElem
    #---------------------------------------------------------------------------
    #Замена заданного слова на другое
    # changeElem - слово которое заменяем
    # newСhangeElem - слово на что заменяем
    # changeElemLower - заменяемое слово все с маленькой буквы
    # n - количество замененных слов
    def changeWord(arr):
        changeElem = input('Введите слово которое нужно заменить в тексте: ')
        newChangeElem = input('Введите слово на которое нужно заменить: ')
        n = 0
        for i in range(len(arr)):
            arrLower = []
            changeElemLower = changeElem.lower()
            arr_i = arr[i].split(' ')
            for k in arr_i:
                if k == ' ':
                    continue
                arrLower.append(k.lower())
            arr[i] = ''
            for j in range(len(arr_i)):
                if changeElemLower == arrLower[j] or changeElemLower + ',' == arrLower[j]:
                    arr[i] += newChangeElem + ' '
                    n += 1
                    continue
                if arr_i[j] == arr_i[-1]:
                    arr[i] += arr_i[j]
                    continue
                arr[i] += arr_i[j] + ' '
        return arr, n, changeElem
    #---------------------------------------------------------------------------
    #функция для того чтобы забрать из текста все ариф. выражение
    #и поместить их в отдельный массив
    # expressionElem - переменая для вытаскивания ариф. выражений
    # expressions - массив с ариф.выражениями
    # figures - массив с цифрами 0-9
    # arif - массив со ариф. знаками
    # k - используется для expressionElem
    # changeFigure - меняем в числах 10.3 на 10,3 или 8.0 на 8
    def arifmetika(arr):
        figures = '1234567890'
        arif = '+-*/:'
        expressionElem = ''
        expressions = []
        k = 0
        for i in range(len(arr)):
            for j in arr[i]:
                if j in figures:
                    expressionElem += j
                    k = 1
                elif k != 0 and j in arif:
                    expressionElem += j
                    k = 1
                if j not in figures and j not in arif and k!=0:
                    k = 0
                    expressions.append(expressionElem)
                    expressionElem = ''
            for g in expressions:
                if g in arr[i]:
                    figure = round(eval(g),3)
                    changeFigure = ''
                    for t in str(figure):
                        if int(figure) == figure:
                            if t == '.':
                                break
                            changeFigure += t      
                        else:
                            if t == '.':
                                changeFigure += ','
                                continue
                            changeFigure += t
                         
                    arr[i] = arr[i].replace(g,changeFigure)
        return expressions , arr
    #---------------------------------------------------------------------------
    # функция для нахождения самого длиного слова
    # в самом коротком предложении и само предложение
    # shortSentence - самое короткое предложение в тексте без точки
    # sentence - самое короткое предложение в тексте c точкой
    # longWord - самое длинное слово в sentence
    def finderLongerWord(arr):
        arr = ''.join(arr)
        arr = arr.split('.')
        shortSentense = arr[0].split(' ')
        for i in arr:
            i = i.split(' ')
            if len(i) != 1:
                if len(i) < len(shortSentense):
                    shortSentense = i
        if [True for i in shortSentense if len(shortSentense) >1 or i != ' ']:
            longWord = shortSentense[0]
            for i in shortSentense:
                if len(i) > len(longWord):
                    longWord = i
            sentense = ''
            for i in shortSentense:
                if i != shortSentense[-1]:
                    sentense += i + ' '
                    continue
                sentense += i + '.'
            return longWord, sentense
        else:
            print('Error')
            
    # удаление longWord из sentence
    def deleteLongerWordInShortSentence(arr):
        word, sentence = finderLongerWord(arr)
        for i in range(len(arr)):
            arr_i = arr[i].split(' ')
            if sentence in arr[i]:
                for j in arr_i:
                    if j == word:
                        arr_i.remove(word)
                arr[i] = ''
                for j in range(len(arr_i)):
                    if arr_i[j] == word or arr_i[j] == word + '.' or arr_i[j] == word + ',':
                        continue
                    if j < len(arr_i)-1:
                        arr[i] += arr_i[j] + ' '
                    else:
                        arr[i] += arr_i[j]
            #if sentence in arr[i]: 
            #    arr[i] = arr[i].replace(word,'')   
        return  arr, word, sentence
    
    #---------------------------------------------------------------------------
    # выравнивание по левому краю
    if choice == '1':
        for i in text:
            print('    ' + i)
    #---------------------------------------------------------------------------
    # выравнивание по правому краю
    # c - массив длин каждого элемента массива text
    # maxc - число длины самого длинного элемента в text
    # b - разница между длиной самого длиного элемента и других элементов text
    elif choice == '2':
        c = []
        for i in text:
            c.append(len(i))
        maxc = max(c)
        for i in text:
            if len(i) < maxc:
                b = maxc - len(i)
                print('    ' + b*' ' + i)
            else:
                print('    ' + i)
        print()
    #---------------------------------------------------------------------------
    # выравнивание по ширине
    # lenElText - массив длин каждого элемента text
    # maxlenEl - число длины самого длинного элемента в text
    # text_i - массив для слов из эелементов text
    # numberOfWords - количесвто слов в text_i
    # lenStr - длина в общем text_i без пробелов
    # spaces - число пробелов между словами
    # add - дополнительные пробелы пееред последним словом
    elif choice == '3':
        lenStr = 0
        numberOfWords = 0
        lenElText = []
        for i in text:
            lenElText.append(len(i))
        maxlenEl = max(lenElText)
        for i in range(len(text)):
            text_i = text[i].split(' ')
            for j in range(len(text_i)):
                numberOfWords += 1
                for k in range(len(text_i[j])):
                    lenStr += 1
            if numberOfWords == 0 or lenStr == 0 or numberOfWords == 1:
                spaces = 0
                add = 0
            else:
                spaces = (maxlenEl - lenStr) / (numberOfWords-1)
                add = (spaces - int(spaces)) * (numberOfWords-1)
            print('    ', end='')
            for j in range(len(text_i)):
                if add == 0:
                    if j < len(text_i)-1:
                        print(text_i[j] + ' ' * int(spaces), end = '')
                    else:
                        print(text_i[j])
                else:
                    if j < len(text_i)-1:
                        print(text_i[j] + ' ' * int(spaces), end = '')
                    else:
                        print(' ' * round(add) + text_i[j])
            numberOfWords = 0
            lenStr = 0
    #---------------------------------------------------------------------------
    # удаление слова 
    elif choice == '4':
        text, n, delElem  = deleteWord(text)
        if n == 0:
            print('В тексте нет "', delElem, '"')
        else:
            print(*text)
            print('\nВ тексте было удаленно', n, 'слова "', delElem, '"')
    #---------------------------------------------------------------------------
    # замена слова
    elif choice == '5':
        text, n, changeElem  = changeWord(text)
        if n == 0:
            print('В тексте нет "',changeElem, '"')
        else:
            print(*text)
            print('\nВ тексте были заменены', n, 'слова "', changeElem, '"')
        
    #---------------------------------------------------------------------------
    # вычисление ариф. выражений
    elif choice == '6':
        expr, text = arifmetika(text)
        for i in expr:
            print(i, '=', '{:.5g}'.format(eval(i)))
        print()
        print(*text)
    #---------------------------------------------------------------------------
    # удалений длинного слова из короткого предложения
    elif choice == '7':
        text, word, sentence = deleteLongerWordInShortSentence(text)
        print('Измененный текст:')
        print(*text)
        print('\nСамое короткое предложение:', sentence)
        print('Самое длинное слово в самом коротком предложении:', word)
        
    #---------------------------------------------------------------------------
    # выход
    elif choice == '0':
        print('До свидания')
    #---------------------------------------------------------------------------
    else:
        print('Ошибка ввода!!!', 'Значения выбора -', choice, 'нет!')
    print()
