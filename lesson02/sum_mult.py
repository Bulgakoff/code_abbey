a = 11
b = 9
c = 1


def mult_sum(aa, bb, cc):
    qwer = str(aa * bb + cc)
    print(qwer)
    qw = [int(q) for q in qwer]
    result = sum(qw)

    print(qw)
    print(result)


mult_sum(a, b, c)

qwe = [int(qw) for qw in input('enter : ').split()]
print(qwe)
