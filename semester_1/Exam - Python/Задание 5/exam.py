# Даны два файла: in1.txt и in2.txt, в каждом по N строк.
# В первом файле записаны номера строк второго файла
# от 1 до N (не по порядку), номера не повторяются.
# В каждой строке второго файла записаны 2 натуральных числа через пробел.
# Требуется вывести в файл out.txt суммы чисел
# из файла in2.txt, каждую с новой строки,
# по порядку в соответствии с номерами, определёнными
# в файле in1.txt.
# Выводить только те суммы, в которых количество
# чётных цифр больше, чем нечётных.
# Файлы в память целиком не считывать,
# числовой тип к строковому для подсчёта количества
# чётных цифр не приводить.

def even_counter(num):
    counter = 0
    while num:
        if num % 2 == 0:
            counter += 1
        else:
            counter -= 1
        num = num // 10
    return counter > 0

out_file = open('out.txt', 'w')
sum_file = open('in2.txt', 'r')
sums = []
for line in sum_file:
    numbers = line.split()
    result = int(numbers[0]) + int(numbers[1])
    sums.append(result)
sum_file.close()
print(sums)
number_file = open('in1.txt', 'r')
for line in number_file:
    indx = int(line)
    result = sums[indx - 1]
    if even_counter(result):
        out_file.write(str(result) + '\n')

number_file.close()
out_file.close()
