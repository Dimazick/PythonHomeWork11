#Блок стндартная алгоритмика
#задача 1 Найти факториал числа
# def can_Factorial(a: int):
#     if a < 0:
#         return False
#     else:
#         return True
#
# def findtorial(a:int):
#     if can_Factorial(a):
#         fact = 1
#         if a > 0:
#             for i in range(1, a+1):
#                 fact *= i
#         return fact
#     else:
#         print("Факториал это для целых и положительных.")
#         return None
import string
from typing import List

#
# print("Найдем факториал числа")
# try:
#     number = int(input("введите число >> "))
# except:
#     print("Ошибка, введите число! Раз уж вы промахнулись по циферкам, то примем число=1")
#     number = 1
#
# print("Введено число = ", number)
# print("Факториал такового числа = ", findtorial(number))


#Задача 2 найти максимум и минимум в последовательности чисел с консоли.
# def get_numbers():
#     print("Заполним последовательность, внимание, при вводе 0 последовательность будет считаться заполненной")
#     numbers = []
#     while True:
#         try:
#             number = int(input("введите число последовательности>>  "))
#         except:
#             print("не попал по циферке. заканчиваем упражнение...")
#             number = 0
#         if number == 0:
#             break
#         else:
#             numbers.append(number)
#     return numbers
#
# def find_max(numbers):
#     maxim = numbers[0]
#     for i in numbers:
#         if i > maxim:
#             maxim = i
#     return maxim
#
# def find_min(numbers):
#     minim = numbers[0]
#     for i in numbers:
#         if i < minim:
#             minim = i
#     return minim
#
# def print_numbers(numbers):
#     print("введена следующая последовательность чисел: ")
#     for i in numbers:
#         print(i, end=' ')
#     print()
#
# chisla = get_numbers()
# print_numbers(chisla)
# print("максимум в последовательности  = ", find_max(chisla))
# print("минимум в последовательности  = ", find_min(chisla))

#Задача 2*
# def get_numbers():
#     print("Заполним последовательность нулями и единицами, внимание, при вводе буквы или цифры отличной от 0 или 1 последовательность будет считаться заполненной")
#     numbers = []
#     while True:
#         try:
#             number = int(input("0 or 1 >>  "))
#         except:
#              print("не попал по циферке. заканчиваем упражнение...")
#              break
#         if number == 0 or number == 1:
#             numbers.append(number)
#         else:
#             break
#     return numbers
#
# def print_numbers(numbers):
#     print("введена следующая последовательность чисел: ")
#     for i in numbers:
#         print(i, end=' ')
#     print()
#
# def list_in_one_number(massiv:list):
#     ciferka = ''
#     for i in massiv:
#         i = str(i)
#         ciferka += i
#     print("имеется двоичное число =", ciferka)
#     print("переведем его в обычное десятиричное число...")
#     binary = int(ciferka)
#     numb_tenx = 0
#     count = 0
#     while binary != 0:
#         magic_number = binary % 10
#         numb_tenx += magic_number*2**count
#         binary = binary // 10
#         count += 1
#
#     return numb_tenx
#
#
# ciferki = get_numbers()
# print_numbers(ciferki)
# print("ololo", list_in_one_number(ciferki))

#Задачи про строки
# word1 = "функция"
# print(word1, "получим из этого слова слова фут и ция")
# print(word1[0:2] + "т")
# print(word1[4:])
# print("***")
#
# word2 = "переменная"
# print(word2, " получим из слова пена и ремень")
# print(word2[0:2] + word2[7:9])
# print(word2[2:7] + "ь")
# print("***")
#
# word3 = "декларация"
# print(word3," получим слова кара и дел")
# print(word3[2] + word3[4:7])
# print(word3[0:2]+word3[3])
# print("***")
#
# word4="инкапсуляция"
# print("Из слова инкапсуляция путем вырезок и склеек его букв получить слова пуля и инкас")
# print(word4[4]+word4[6:9])
# print(word4[0:4] + word4[5])
# print("***")
#
# word5 = "полиморфизм"
# print(word5, "получить слова лимон и профи")
# print(word5[2:6]+"н")
# print(word5[0]+word5[6:4:-1]+word5[7:9])

# Задача 8 про полиндром
# stroka1 = input("введите строку, которую будем проверять на полиндромность >>")
# print(f"проверим строку <<< {stroka1} >>> на полиндромность")
# stroka_for_chek = stroka1.replace(" ", "")
# stroka_for_chek = stroka_for_chek.translate(str.maketrans("", "", string.punctuation))
# stroka_for_chek = stroka_for_chek.lower()
#
#
# if stroka_for_chek == stroka_for_chek[-1::-1]:
#     print("эта строка полиндром, убедитесь сами: ")
#     print(stroka_for_chek)
#     print(stroka_for_chek[-1::-1])
# else:
#     print("эта строка не полиндром! ")

#Задача 9
# massiv1 = [0, 1, 2, 3, 4, 5, 6, 6, 9, 3, 17]
# massiv2 = [7, 6, 5, 4, 3, 2, 1]
#
# print(massiv1)
# print(massiv2)
# print("*****")
#
# def creating3massiv(list1, list2):
#     list3=[]
#     for i in range(len(list1)):
#         if (list1[i] in list2) and (list1[i] not in list3):
#             list3.append(list1[i])
#     return list3
#
# if len(massiv1) > len(massiv2):
#     massiv3 = creating3massiv(massiv1, massiv2)
# else:
#     massiv3 = creating3massiv(massiv2, massiv1)
#
# print(massiv3)


#11.53
# def removing10(massiv:list):
#     for i in range(len(massiv)):
#         if massiv[i] % 10 == 0:
#             massiv[i] = 0
#     return massiv
#
# def changingOn2(massiv: list):
#     for i in range(len(massiv)):
#         if massiv[i] % 2 == 0:
#             massiv[i] /= 2
#         else:
#             massiv[i] *= 2
#     return massiv
#
# def changingOnMN(massiv: list, m, n):
#     for i in range(len(massiv)):
#         if i % 2 != 0:
#             massiv[i] += n
#         elif massiv[i] % 2 != 0:
#             massiv[i] -= m
#     return massiv

#11.88
# price_of_cars = [11500, 5100, 19000, 15000]
# price_of_moto = [2200, 2500, 4000, 5300]
#
# def average_price(price_list: list):
#     return sum(price_list)/len(price_list)
#
# def find_min_on_price(price_list: list):
#     min = price_list[0]
#     for i in range(1, len(price_list)):
#         if price_list[i]< min:
#             min = price_list[i]
#     return min
#
# def check_price_other_min(price_list, other_min):
#     for i in price_list:
#         if i > other_min:
#             return True
#     return False
#
#
# a = average_price(price_of_cars)
# b = average_price(price_of_moto)
# min_in_carprice= find_min_on_price(price_of_cars)
# print(f"цены на автомобили {price_of_cars}")
# print(f"цены на MOTO {price_of_moto}")
# print(f"средняя цена автомобиля = {a}, средняя цена мотоцикла = {b}, дороже ли машиныв 3 раза?")
# print(b * 3 < a)
# print()
# print(f"Минимальная цена автомобиля = {min_in_carprice}")
# print("есть ли мотоциклы дороже, чем самая дешевая машина? ")
# print(check_price_other_min(price_of_moto, min_in_carprice))

#11.132
# massiv = [1, 2, 3, 9, 111, 17, -4, 0, -255, 123]
#
# def find_max(lst:list):
#     maximum = max(lst)
#     return maximum
#
# def find_min(lst:list):
#     return min(lst)
#
# def find_SoMax(lst:list):
#     maxim = find_max(lst)
#     max_id = lst.index(maxim)
#     if max_id != 0:
#         soMax = lst[0]
#         for i in range(1, max_id):
#             if soMax < lst[i]:
#                 soMax = lst[i]
#     else:
#         soMax= lst[1]
#     for i in range(max_id+1, len(lst)):
#         if soMax < lst[i]:
#             soMax = lst[i]
#     return soMax
#
# def find_SoMin(lst:list):
#     minimum = find_min(lst)
#     min_id = lst.index(minimum)
#     if min_id != 0:
#         soMin = lst[0]
#         for i in range(1, min_id):
#             if soMin > lst[i]:
#                 soMin = lst[i]
#     else:
#         soMin= lst[1]
#     for i in range(min_id+1, len(lst)):
#         if soMin > lst[i]:
#             soMin = lst[i]
#     return soMin
#
# print(f"есть массив {massiv}")
# print(f"максимальный элемент = {find_max(massiv)}")
# print(f"второй по значению =  {find_SoMax(massiv)}")
# print(f"самый минимальный элемент = {find_min(massiv)}")
# print(f"и втрой с конца {find_SoMin(massiv)}")

#11.139
# bigHouse = [9, 8, 12, 14, 11, 5, 23, 7, 9, 7, 19, 16, 7, 17, 21]
# def find_min(lst:list):
#     a = min(lst)
#     return lst.index(a)
#
# def find_SoMin(lst:list):
#     min_id = find_min(lst)
#     if min_id != 0:
#         soMin_id = 0
#         soMin = lst[soMin_id]
#         for i in range(1, min_id):
#             if soMin > lst[i]:
#                 soMin = lst[i]
#                 soMin_id = i
#     else:
#         soMin_id = 1
#         soMin= lst[soMin_id]
#     for i in range(min_id+1, len(lst)):
#         if soMin > lst[i]:
#             soMin = lst[i]
#             soMin_id = i
#     return soMin_id
#
# print("Имеется многоэтажный дом. в котором живут люди. Рассмотрим получше : ")
# for i in range(0, len(bigHouse)):
#     print(f"На этаже #{i+1} проживает {bigHouse[i]} людей")
#
# print(f"получается что меньше всего у нас живет людей на этажах: {find_min(bigHouse)+1} и {find_SoMin(bigHouse)+1}."
#       f" Проживает на них людей {bigHouse[find_min(bigHouse)]} чел и  {bigHouse[find_SoMin(bigHouse)]} чел соответственно")

#11.185
# points = [80, 78, 77, 76, 74, 73, 72, 71, 69, 65, 63, 60, 55, 51, 50, 47, 41, 39, 37, 33]
# print("Имеется Турнирная таблица : ")
# for i in range(0, len(points)):
#     print(f"место #{i+1} очков {points[i]}")
# userPoint = int(input("выберите число очков, которое набрала команда из турнирной таблицы>> "))
# place = points.index(userPoint)+1 if userPoint in points else print("к сожалению, вы ввели некорректные данные")
# print(f"команда заняла {place} место") if place else print("Попробуй снова")

#11.216
# squares = [20, 95, 22, 15, 217, 37, 85, 75, 93, 177, 221, 365, 155, 132, 400, 301, 207, 111, 166, 298]
# cropes = [170, 1500, 200, 153, 2280, 380, 997, 908, 907, 2503, 3201, 7125, 2250, 2200, 5320, 4185, 6007, 1240, 2730, 5123]
#
# for i in range(0, len(squares)):
#     print(f"в районе области №{i+1} площадь посева равна {squares[i]}ГА,  урожай {cropes[i]} центнеров")
#
# print("средняя урожайность пщеницы: ")
# for i in range(0, len(squares)):
#     print(f"в районе области №{i+1} средняя урожайность {round(cropes[i]/squares[i], 2)} центнеров/ГА")
#
# summaSquares=0
# summaCropes=0
# for i in squares:
#     summaSquares += i
#
# for i in cropes:
#     summaCropes += i
#
#
# print("Средняя урожайность по области = ", round(summaCropes/summaSquares, 2))

#file#10
# firstlyPath = input("input path of file>> ")
# fileFirst = open(firstlyPath, "w")
# fileFirst.write("1 2 4 6 8 7 6 8 1 3 4 7")
# fileFirst.close()
#
# def sumInFile(file_name):
#     fff = open(file_name, 'r')
#     numbs = fff.read()
#     summa = 0
#
#     numbs = numbs.split()
#     intNumbs = []
#     for i in range(0, len(numbs)):
#         intNumbs.append(int(numbs[i]))
#
#     for i in intNumbs:
#         if i % 2 == 0:
#             summa += i
#     return summa
#
# def multInFile(file_name):
#     fff = open(file_name, 'r')
#     numbs = fff.read()
#     multiply = 1
#
#     numbs = numbs.split()
#     intNumbs = []
#     for i in range(0, len(numbs)):
#         intNumbs.append(int(numbs[i]))
#
#     for i in intNumbs:
#         if i % 2 == 0:
#             multiply *= i
#     return multiply
#
# def getNewFile(path, summa, projzv):
#     fff = open(path, "w")
#     text = f"Сумма значейний, кратных двум = {summa}, произведение = {projzv}"
#     fff.write(text)
#     fff.close()
#
# secondlyPath = input("input path of second file>> ")
#
# getNewFile(secondlyPath, sumInFile(firstlyPath), multInFile(firstlyPath))

#file #11

# firstlyPath = input("input path of file>> ")
# fileFirst = open(firstlyPath, "w")
# print("запишем в файл такие цифры: 1 2 -4 -6 8 -7 6 8 -1 -3 4 7")
# fileFirst.write("1 2 -4 -6 8 -7 6 8 -1 -3 4 7")
# fileFirst.close()
#
# def List_from_file(path):
#     f = open(path, 'r')
#     numbs = f.read().split()
#     intNumbs=[]
#     for i in range(0, len(numbs)):
#         intNumbs.append(int(numbs[i]))
#     return intNumbs
#
# def Magic_with_lst(path):
#     intNumbs = List_from_file(path)
#     for i in range(0, len(intNumbs)):
#         k = 0
#         if intNumbs[i] < 0:
#             intNumbs[i] = 1
#             k += 1
#         if k == 0:
#             if i % 2 != 0:
#                 intNumbs[i] = 0
#     print("теперь в файле будут такие цифры ", intNumbs)
#     return intNumbs
#
# def Write_new_info(path):
#     massiv = Magic_with_lst(path)
#     fi = open(path, 'w')
#     text = ''
#     for i in massiv:
#         text += f"{i} "
#
#     fi.write(text)
#     fi.close()
#
# Write_new_info(firstlyPath)

#file#12
dataPath = "data_11.txt"
def GiveMeMatrix(path):
    file = open(path, 'r')
    lineNumbs = []
    for line in file:
        lineNumbs.append(line.split(','))
    numbs = [[int(i) for i in lines]for lines in lineNumbs]
    return numbs

def GiveMonthIncome(path):
    matrix = GiveMeMatrix(path)
    monthIncome = []
    for i in range(0, len(matrix)):
        summa = 0
        for j in range(0, len(matrix[i])):
            summa += matrix[i][j]
        monthIncome.append(summa)

    return monthIncome

def FindMaxMonthIncome(path):
    monthIncome = GiveMonthIncome(path)
    index = 0
    maxim = monthIncome[index]
    for i in range(1, len(monthIncome)):
        if maxim < monthIncome[i]:
            maxim = monthIncome[i]
            index = i
    return index

def FindCoolestShopInMonth(path):
    matrix = GiveMeMatrix(path)
    coolestShop = []
    for i in range(0, len(matrix)):
        coolestShop.append(matrix[i].index(max(matrix[i])))
    return coolestShop

def GiveAvverageIncomeMonth(path):
    matrix = GiveMeMatrix(path)
    AvverageIncMonth = [sum(matrix[i])/len(matrix[i]) for i in range(0, len(matrix))]
    return AvverageIncMonth

def GiveShopsToClose(path):
    matrix = GiveMeMatrix(path)
    avverageInc=GiveAvverageIncomeMonth(path)
    shopsToClose = []
    strings = len(matrix)
    columns = len(matrix[0])
    for j in range(0, columns):
        count = 0
        for i in range(0, strings):
            if matrix[i][j] <= avverageInc[i]:
                count += 1
        if count == strings:
            shopsToClose.append(j)
    if len(shopsToClose) != 0:
        return shopsToClose
    else:
        message = "Все магазины выполнили требования к продолжению работы. Закрывать какую-либо точку не требуется"
        return message

print("Добрый день, уважаемые акционеры компании Эльбрус2023! Вашему вниманию отчет о прошедших 10 месяцах работы.")
print("Доходы магазинов указаны в соответствующих столбцах")
otchet = GiveMeMatrix(dataPath)
for i in range(0, len(otchet)):
    print(f"месяц №{i+1} ")
    for j in range(0, len(otchet[i])):
        print(otchet[i][j], end=" ")
    print()
print(f"Месяц с самым высоким доходом, нашей компании это был {FindMaxMonthIncome(dataPath) + 1}-ый отчетный месяц")
print()
print("Магазины с самой высокой прибылью по месяцам: ")
betterShop = FindCoolestShopInMonth(dataPath)
for i in range(0, len(betterShop)):
    print(f"Магазин № {betterShop[i]+1} лучший в отчетном месяце №{i+1}")
print()
print("Средняя доходность по месяцам: ")
betterShop = GiveAvverageIncomeMonth(dataPath)
for i in range(0, len(betterShop)):
    print(f"в отчетном месяце №{i+1} средняя доходность = {betterShop[i]}")
print()
print("Выясним, какие магазины следует закрыть. Магазин следует закрыть, если его доходность ниже средней по все месяцам")
shopsClose = GiveShopsToClose(dataPath)
if type(shopsClose) == str:
    print(shopsClose)
else:
    for i in range(0, len(shopsClose)):
        print(f"магазин №{shopsClose[i]+1}")














