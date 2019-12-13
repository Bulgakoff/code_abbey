import math


# Простейшие арифметические операции (1)
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +,
# сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(q, w, e):
    if e == '+':
        result = q + w
    elif e == '-':
        result = q - w
    elif e == '*':
        result = q * w
    elif e == '/':
        result = q / w
    else:
        return print('Неизвестная операция')

    return result


try:
    result = arithmetic(1, 2, 8697)
    print(result)
except UnboundLocalError as  q:
    print(f'------>{q}')

print('//////////////////////////////')


# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе

def is_year_leap(unm):
    if unm % 400 == 0 and unm % 4 == 0 and unm % 100 != 0:
        return 'uод высокостный '
    else:
        return 'не высокостный'


print(is_year_leap(2000))
print('//////////////////////////////')


# Квадрат (3)
# Написать функцию square,
# принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
# s = d*d/2   $$$$$$$    s = a*a   $$$$$$$   p = a*4
def square(qwe):
    p = round(qwe * 4)
    s = round(qwe ** 2)
    d = round(qwe * math.sqrt(2))

    return (p, s, d)


result = square(5)
print(result)
print(type(result))

print('//////////////////////////////')
# Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
seasons_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def season(n_month):
    for p in seasons_list:
        if n_month in seasons_list[0]:
            return 'winter'
        elif n_month in seasons_list[1]:
            return 'spring'
        elif n_month in seasons_list[2]:
            return 'summer'
        elif n_month in seasons_list[3]:
            return 'authom'
        else:
            return 'abrakaa'


print(season(5))
# Банковский вклад (5)
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты).
#
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
# которая будет на счету пользователя.
s = round(50000 + 50000 * 10.5 * 10 * 356 / 365 / 100)
print(f'----------{s}')


# final_sum = (first_sum *size_prc * days_prc / 365) / 100

def bank(a, years):
    for year in range(years):
        a *= 1.1
        print(f' в {year} год сумма {round(a)}')
    return round(a)


result = bank(50000, 10)
print(f'--------------=итоговая\ сума ================={result}')
print('///////////////////////Задача 6///////////////////////////////')
# Напишите код, который переводит целое число в строку, при том что его
# можно применить в любой системе счисления. ValueError: int() base must be >= 2 and <= 36, or 0

str_num = 37

str_letter = 'ACD'

print(int('ACD', 32))
print('///////////////////////Задача 7///////////////////////////////')

# Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы,
# а каждое число внутри равно сумме двух расположенных над ним чисел.
# qqq =[]
# def tri_pascale(n):
#     for ggg in range(1, n):
#         if
#         qqq.append(ggg)
#
#
#
#
# tri_pascale(5)







print('///////////////////////Задача 8 number prime///////////////////////////////')


# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе

def is_prime(number):
    d = 2
    while number % d != 0 and d * d <= number:
        d += 1
    # return d * d > number

    return f'{number}  составное число ' if d * d <= number else f'{number} prime число'


print(is_prime(5))

print('# ?///////////2 caase ////////////////////////')


def is_primme(number):
    """Эту функцию можно сильно оптимизировать. Подумайте, как"""

    if number == 1:
        return number != 1  # 1 - не простое число
    lst = []
    for possible_divisor in range(2, number):
        if number % possible_divisor == 0:
            lst.append(possible_divisor)
        print(lst)
        return number % possible_divisor != 0

    return True


print(is_primme(50))

