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
arrOfFields = []
database = {}
k = 0

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
            numberOfFields = int(input('Введите количество полей в записи: '))
            for i in range(numberOfFields):
                print('Введите название', i+1, '-го поля: ', end='')
                nameOfField = input()
                arrOfFields.append(nameOfField)
            print('БД "', nameOfDatabase, '" была создана.')
            k = 1
        if k == 0:
            while True:
                answer = input('Перезаписать БД да/нет? ')
                if answer == 'да' or answer == 'y':
                    fileOfDatabase = open(nameOfDatabase + '.bin','wb')
                    database.clear()
                    numberOfFields = int(input('Введите количество полей в записи: '))
                    for i in range(numberOfFields):
                        print('Введите название', i+1, '-го поля: ', end='')
                        nameOfField = input()
                        arrOfFields.append(nameOfField)
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
        except FileNotFoundError:
            nameOfDatabase = input('Введите название БД: ')
            
        try:
            fileOfDatabase = open (nameOfDatabase + '.bin','rb')
            
            try:
                database = p.load(fileOfDatabase)
            except:
                database = {}   
            if database == {} and arrOfFields == []:
                k = 0
                numberOfFields = int(input('Введите количество полей в записи: '))
                for i in range(numberOfFields):
                    print('Введите название', i+1, '-го поля: ', end='')
                    nameOfField = input()
                    arrOfFields.append(nameOfField)
            else:
                if k == 0: 
                    for n in database.keys():
                        k += 1
                        
            if arrOfFields == []:
                data = database.setdefault(0)
                for i in data.keys():
                    arrOfFields.append(i)
                    
            numberOfFields = len(arrOfFields)
            fileOfDatabase.close()
            database_i = {}
            fileOfDatabase = open (nameOfDatabase + '.bin','wb')
            
            for i in range(numberOfFields):
                print('Введите данные в поле "', arrOfFields[i], '": ', end='')
                dataOfField = input()
                database_i.update({arrOfFields[i]:dataOfField})
                
            database.update({k:database_i})
            k += 1
    
            p.dump(database, fileOfDatabase)
            
            fileOfDatabase.close()
            
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            
    #-----------------------------------------------
    elif choice == '3':
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
                print(database)
                if arrOfFields == []:
                    data = database.setdefault(0)
                    for i in data.keys():
                        arrOfFields.append(i)
                print('-'*6 + '-'*21*len(arrOfFields))
                print('|{:^4}|'.format('№'), end='')
                for j in range(len(arrOfFields)):
                    print('{:^20}|'.format(arrOfFields[j]), end='')
                print('\n' + '-'*6 + '-'*21*len(arrOfFields))
                for i in database.keys():
                    print('|{:^4}|'.format(i+1), end='')
                    data = database.setdefault(i)
                    for field in data.keys():
                        print('{:^20}|'.format(data.setdefault(field)), end='')
                    print()
                print('-'*6 + '-'*21*len(arrOfFields))
                fileOfDatabase.close()
            except MemoryError:
                print('БД повреждена!')
            except EOFError:
                print('БД пуста!')
        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
             
    #-----------------------------------------------   
    elif choice == '4':
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
              
                if arrOfFields == []:
                    data = database.setdefault(0)
                    for i in data.keys():
                        arrOfFields.append(i)
                field_1 = input('Введите название искомого поля в записи: ')

                if field_1 in arrOfFields:
                    print('Введите искомые данные по полю', field_1, ': ', end='')
                    dataOfField_1 = input()
                    arrOfNotice = []
                    for key in database.keys():
                        data = database.setdefault(key)
                        for field in data.keys():
                            if field == field_1 and data.setdefault(field) == dataOfField_1:
                                arrOfNotice.append(key)
                    b = 0
                    print('---------------------------')
                    if arrOfNotice != []:
                        for notice in database.keys():
                            if notice == arrOfNotice [b]:
                                if b < len(arrOfNotice)-1:
                                    b += 1
                                data = database.setdefault(notice)
                                for field in data.keys():
                                    dataOfNotice = field + ': ' + data.setdefault(field)
                                    print(dataOfNotice)
                                print('---------------------------')
                    else:
                        print('Данные не были найдены!')
                else:
                    print('Записей с полем', field_1, ' нет.')
                    
                fileOfDatabase.close()
                
            except MemoryError:
                print('БД повреждена!')
            except EOFError:
                print('БД пуста!')

        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
            
        
    #--------------------------------------------------------------------------
    elif choice == '5':
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
              
                if arrOfFields == []:
                    data = database.setdefault(0)
                    for i in data.keys():
                        arrOfFields.append(i)
                field_1 = input('Введите название искомого поля в записи: ')
                field_2 = input('Введите название искомого поля в записи: ')
                if field_1 in arrOfFields and field_2 in arrOfFields:
                    print('Введите искомые данные по полю', field_1, ': ', end='')
                    dataOfField_1 = input()
                    print('Введите искомые данные по полю', field_2, ': ', end='')
                    dataOfField_2 = input()
                    arrOfNotice = []
                    for key in database.keys():
                        data = database.setdefault(key)
                        for field in data.keys():
                            if (field == field_1 and data.setdefault(field) == dataOfField_1):
                                for field in data.keys():
                                    if (field == field_2 and data.setdefault(field) == dataOfField_2):
                                        arrOfNotice.append(key)
                                
                    b = 0
                    print('---------------------------')
                    if arrOfNotice != []:
                        for notice in database.keys():
                            if notice == arrOfNotice [b]:
                                if b < len(arrOfNotice)-1:
                                    b += 1
                                data = database.setdefault(notice)
                                for field in data.keys():
                                    dataOfNotice = field + ': ' + data.setdefault(field)
                                    print(dataOfNotice)
                                print('---------------------------')
                    else:
                        print('Данные не были найдены!')
                else:
                    print('Введенные поля не существуют!')
                    
                fileOfDatabase.close()
                
            except MemoryError:
                print('БД повреждена!')
            except EOFError:
                print('БД пуста!')

        except FileNotFoundError:
            print('БД с именем', nameOfDatabase, 'нет!')
                        
    #-----------------------------------------------        
    elif choice == '0':
        print('До свидания.')
    else:
        print('Команду', choice, 'нет !!!')
    print()
