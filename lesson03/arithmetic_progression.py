# a + (a + b) + (a + 2b) + (a + 3b) + ...
# 5 2 3  ///////------->  = 21
# 3 0 10  ///////------->  = 21    s = (2*a1 + d*(n - 1)) *n / 2
s = round((2 * 5 + 2 * (3 - 1)) * 3 / 2)
s = round((2 * 3 + 0 * (10 - 1)) * 10 / 2)

print(f'======---===>{s}')
k_sum = 2
f_elem = 5

qwe = [int(q) for q in input('enter:  ').split()]
print(f'---------на входе ---------->{qwe}')


def ar_prog(qwert):
    d = round((2 * qwert[0] + qwert[1] * (qwert[2] - 1)) * qwert[2] / 2 ) # сумма 3 х элементов прогрессии
    return d

res = ar_prog(qwe)
print(f'---------на выходе ---------->{res}')
