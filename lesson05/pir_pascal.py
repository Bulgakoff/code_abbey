x = [[1, 2, 3],
     [3, 4, 5],
     [6, 7, 8]]

print(x)
print('///////////////first first first first first ///////////////////////')
x = [[1, 2, 3],
     [3, 4, 5],
     [6, 7, 8]]
print(f' in line ---->{x}')


def print_fir(x):
    for i in x:
        # print()  # после каждой строки принт добавляет перенос , print -это топор переноса
        for j in i:
            print(f'{j}', end=' ')  # print -это топор переноса
        print()  #


print_fir(x)  # после каждой строки принт добавляет перенос print -это топор переноса

print('///in line ---->[[1, 2, 3], [3, 4, 5], [6, 7, 8]]second //////////////////')


def print_sec(x):
    for i in range(len(x)):  # получаем индекс определенного диапазона
        # что бы 3 элеменотов напечатать берем либо range(len(3)), либо 3 +1=4
        for j in range(len(x[i])):
            print(x[i][j], end=' ')  # вспоминаем что это список списков ====== колбаса
        print()  # топор


print_sec(x)
print('////////x[1][2] = 1000///x[1][2] = 1000///x[1][2] = 1000///x[1][2] = 1000///////////')
x[1][2] = 1000
print_fir(x)

print('////////заполнение  матрицы нулями///////////')

mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def create_x_zero(m, n):
    maat = []
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append(0)
        # print(internal_arr)
        maat.append(internal_arr)

    # for q in maat:
    #     for w in q:
    #         print(w, end=' ')
    #     print()
    return maat


result = create_x_zero(4, 5)
print(result)
result = print_fir(create_x_zero(4, 10))
print('////////еркальная матрица///////////')
x = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]


def mirror_arr(qwe):
    d = []
    for p in qwe:
        d.append(reversed(p))
    return d


result = print_fir(mirror_arr(x))

print('////////Зеркальная матрица22222!!!!!!!///////////')


def swap(q, w, e):
    temp = q[w]
    q[w] = q[e]
    q[e] = temp

def mirror_2d(qwe):
    for arr in qwe:
        for i in range(len(arr) // 2):
            swap(arr, i, len(arr) - 1 - i)


mirror_2d(x)# здесь сoздали ящик тут в этом мест ереально появился объект ИЗМЕНЕННЫЙ Ё!!!!!!!!!!!!!
print_fir(x)

