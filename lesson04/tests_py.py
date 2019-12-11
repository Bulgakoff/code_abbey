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
def square(qwe):
    pass


square(3)

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


# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.

def is_prime(qwe):
    d = 2
    while qwe % d != 0 and d * d <= qwe:
        d += 1
    return d * d > qwe


print(f'+++++++++++++++{is_prime(4)}')


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


print(f'-------====*****{IsPrime(4)}')

s = math.sqrt(50)
print(s)
