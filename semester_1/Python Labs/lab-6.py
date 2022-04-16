#по журналу 16 выполняю п.6 - 4 и п.7 - 1 
choice = None
a = []

while choice != '0':
    print('1 - Проинициализировать список первыми N элементами заданного ряда(исходя из 5 лабы).')
    print('2 - Добавить элемент в производьное место массива.')
    print('3 - Удалить элемент производьное место из списка.')
    print('4 - Очистить список.')
    print('5 - Найти значение K-го экстремума в списке, если он является списком чисел.')
    print('6 - Найти наиболее длинную знакочередующаяся последовательность нечётных чисел.')
    print('7 - Найти последовательность, включающую в себя наибольшее количество элементов-cтрок, содержащих только гласные буквы.')
    print('8 - Вывести список.')
    print('0 - Выход.')
    while True:
        choice = input('Выбор - ')
        a.append(choice)
        a = choice.split(' ')
        if a[0] == '':
            a[0] = a[0].replace('',' ')
        if a[0] != ' ':
            a = []
            break
        else:
            a = []
            print('Введите число!')
    
    if choice == '0':
        print('Выход')
    #вызов 8     
    elif choice == '8':
        if a == []:
            print('Список пустой.')
        else:
            print('\nСписок:')
            for i in a:
                print(i)
    # вызов 1            
    elif choice == '1':
        while True:
            x,eps,i,inter = map(float,input("Введите аргумент, точность, шаг печати, максмальное значение интераций: ").split())
            if inter > 0 and i > 0:
                break
            elif i <= 0 or inter <= 0:
                print("Ошибка ввода.")
                print("Шаг печати больше нуля.")
                print("Максимальное значение интераций больше нуля.")
            else:
                print("Ошибка ввода")
        n = 0 # значение n для 
        t = 1 # член ряда
        b = 1 
        S = 0 # sum
        num = 1 # номер интерации
        while abs(t) > eps:
            if num <= int(inter): 
                if (num%2 == 0):
                    t = -(n+1)*(n+2)*x**n/2
                else:
                    t = (n+1)*(n+2)*x**n/2
                S += t # Текущее значение суммы
                a.append(S)
                if num == b:
                    b += i
                num += 1 
                n += 1
            else:
                break;
    #вызов 2        
    elif choice == '2':
        i = input('Введите int или str: ')
        index = int(input('Введите произвольное место элемента: '))

        if type(i) == str:
            if i.isdigit():
                i = int(i)
        a.insert(index, i)
    #вызов 3     
    elif choice == '3':
        index = int(input('Введите произвольное место элемента: '))
        if index < len(a):
            a.remove(a[index])
        else:
            print('Такого элемента с индексом -', index, 'нет.')
    #вызов 4        
    elif choice == '4':
        a.clear()
        print('Список очищен!')
    #вызов 5    
    elif choice == '5':
        if a == []:
            print('Список пустой')
        else:   
            b = 0
            for i in a:
                if type(i) != int and type(i) != float:
                    b += 1
            if b == 0:
                amax = max(a)
                amin = min(a)
                kmax = a.index(amax)
                kmin = a.index(amin)
                print('Максисальное значение списка(чисел):', amax)
                print('Минимальное значение списка(чисел):', amin)
                print('k-ый экстремум:', 'kmax -', kmax, 'kmin -', kmin)
            else:
                print('Список состоит не только из чисел, но и строк!')
        
    #вызов 6    
    elif choice == '6':
        if a == []:
            print('Список пустой')
        else:
            b = a
            c = []
            a = []
            for i in b:
                if type(i) != str and i % 2 != 0  :
                    c.append(i)
            for j in range(0, len(c)):
                 if j % 2 == 0:
                    a.append(abs(c[j]))
                 else:
                    a.append(-abs(c[j]))          
    #вызов 7    
    elif choice == '7':
        if a == []:
            print('Список пустой')
        else:
            b = a
            a = []
            c = 0
            for i in b:
                if type(i) == int or type(i) == float:
                    continue
                for j in range(0,len(i)):
                    if i[j] == 'a' or i[j] == 'e' or i[j] == 'i' or i[j] == 'e' or i[j] == 'o'  or i[j] == 'u'  or i[j] == 'y':
                        c = 0
                    elif i[j] == 'A' or i[j] == 'E' or i[j] == 'I' or i[j] == 'E' or i[j] == 'O'  or i[j] == 'U'  or i[j] == 'Y':
                        c = 0
                    else:
                        c+=1
                        break
                if c == 0:
                    a.append(i)
    else:
        print('Введенного номер нет', choice)
    print()
