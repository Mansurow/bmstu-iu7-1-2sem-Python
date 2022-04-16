#Лабораторная работа № 11
#Имитировать работу базы данных, используя бинарный файл.
#Запись содержит 3-4 поля. Например, запись "книга" содержит поля "автор", "наименование", "год издания".
#Необходимо сделать меню:
#1. Создание БД.
#2. Добавление записи в БД.
#3. Вывод всей БД.
#4. Поиск записи по одному полю.
#5. Поиск записи по двум полям. 
#Для работы с текущей записью используется словарь.
import pickle as p

choice = None
database = {}

print('__________МЕНЮ____________')
print('1 - Создание БД.')
print('2 - Добавления записи в БД.')
print('3 - Вывод всей БД.')
print('4 - Поиск записи по одному полю.')
print('5 - Поиск записи по двум полям.')
print('0 - Выход')
   
while choice != '0':
    choice = input('Выбор: ')

  
    #-----------------------------------------------
    if choice == '1':
        k = 0
        nameOfDatabase = input('Введите название БД: ')
        try:
            fileOfDatabase = open(nameOfDatabase + '.bin','rb')
        except FileNotFoundError:
            fileOfDatabase = open(nameOfDatabase + '.bin','wb')
            arrOfFileds = []
            numberOfFields = int(input('Введите количество полей в записи: '))
            for i in range(numberOfFields):
                print('Введите название', i+1, '-го поля: ', end='')
                nameOfField = input()
                arrOfFileds.append(nameOfField)
            print('БД "', nameOfDatabase, '" была создана.')
            k = 1
        if k == 0:
            while True:
                answer = input('Перезаписать БД да/нет? ')
                if answer == 'да' or answer == 'y':
                    fileOfDatabase = open(nameOfDatabase + '.bin','wb')
                    database.clear()
                    arrOfFileds = []
                    numberOfFields = int(input('Введите количество полей в записи: '))
                    for i in range(numberOfFields):
                        print('Введите название', i+1, '-го поля: ', end='')
                        nameOfField = input()
                        arrOfFileds.append(nameOfField)
                    print('БД "', nameOfDatabase, '" была пересоздана.')
                    break
                elif answer == 'нет' or answer == 'n':
                    break
                
        fileOfDatabase.close()
        
    #-----------------------------------------------
    elif choice == '2':
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
        except NameError:
            nameOfDatabase = input('Введите название БД: ')
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
            try:
                database = p.load(fileOfDatabase)
            except:
                database = {}
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            
        if fileOfDatabase != 0:   
            fileOfDatabase.close()
            fileOfDatabase = open (nameOfDatabase + '.bin','wb')    
            database_i = {}
            nameOfNotice = input('Введите название записи БД: ')
            while True:
                try:
                    k = 0
                    
                except ValueError:
                    k = 1
                    print('Ошибка ввода!')
                if k == 0:
                    break
            for i in range(numberOfFields):
                print('Введите название', i+1, '-го поля: ', end='')
                nameOfField = input()
                print('Введите данные в поле "', nameOfField, '": ', end='')
                dataOfField = input()
                data = {nameOfField:dataOfField}
                database_i.update(data)
            database_i = {nameOfNotice:database_i}
            database.update(database_i)
            p.dump(database, fileOfDatabase)
            fileOfDatabase.close()

        
    #-----------------------------------------------
    elif choice == '3':
        k = 0
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
        except NameError:
            nameOfDatabase = input('Введите название БД: ')
        except FileNotFoundError:
            nameOfDatabase = input('Введите название БД: ')
            
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
            try:
                database = p.load(fileOfDatabase)
            except:
                database = {}
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            k = 1
                    
        if  database == {} and k == 0:
            print('БД пуста!')
        elif k == 0:
            print('---------------------------')
            for notice in database.keys():
                print('Запись -', notice)
                data = database.setdefault(notice)
                for field in data.keys():
                    dataOfNotice = field + ': ' + data.setdefault(field)
                    print(dataOfNotice)
                print('---------------------------')
            fileOfDatabase.close()
        else:
            k = 1
        
    #-----------------------------------------------   
    elif choice == '4':
        k = 0
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
        except NameError:
            nameOfDatabase = input('Введите название БД: ')
        except FileNotFoundError:
            nameOfDatabase = input('Введите название БД: ')
            
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
            try:
                database = p.load(fileOfDatabase)
            except:
                database = {}
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            k = 1
            
        if  database == {} and k == 0:
            print('БД пуста!')
            
        elif k == 0:
            field_1 = input('Введите название искомого поля в записи: ')
            arrOfNotice = []
            for notice in database.keys():
                data = database.setdefault(notice)
                for field in data.keys():
                    if field == field_1:
                        arrOfNotice.append(notice)
            
            if arrOfNotice == []:
                print('Записей с полем', field_1, ' нет.')
            else:
                b = 0
                print('---------------------------')
                for notice in database.keys():
                    if notice == arrOfNotice [b]:
                        if b < len(arrOfNotice) - 1:
                            b += 1
                        data = database.setdefault(notice)
                        print('Запись -', notice)
                        for field in data.keys():
                            dataOfNotice = field + ': ' + data.setdefault(field)
                            print(dataOfNotice)
                        print('---------------------------')
            fileOfDatabase.close()
    #-----------------------------------------------    
    elif choice == '5':
        k = 0
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
        except NameError:
            nameOfDatabase = input('Введите название БД: ')
        except FileNotFoundError:
            nameOfDatabase = input('Введите название БД: ')
            
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
            try:
                database = p.load(fileOfDatabase)
            except:
                database = {}
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            k = 1

        if  database == {} and k == 0:
            print('БД пуста!')
        elif k == 0:
            while True:
                field_1 = input('Введите название искомого поля 1 в записи: ')
                field_2 = input('Введите название искомого поля 2 в записи: ')
                if field_1 != field_2:
                    break
                else:
                    print('Введено одно и тоже название поля!')
            arrOfNotice = []
            for notice in database.keys():
                data = database.setdefault(notice)
                for field in data.keys():
                    if field_1 in data.keys() and field_2 in data.keys():
                         arrOfNotice.append(notice)
            
            if arrOfNotice == []:
                print('Записей с полем', field_1, ' нет.')
                print('Записей с полем', field_2, ' нет.')
            else:
                b = 0
                print('---------------------------')
                for notice in database.keys():
                    if notice == arrOfNotice [b]:
                        if b < len(arrOfNotice) - 1:
                            b += 1
                        data = database.setdefault(notice)
                        print('Запись -', notice)
                        for field in data.keys():
                            dataOfNotice = field + ': ' + data.setdefault(field)
                            print(dataOfNotice)
                        print('---------------------------')
    #-----------------------------------------------        
    elif choice == '0':
        print('До свидания.')
    else:
        print('Команду', choice, 'нет !!!')
    print()
