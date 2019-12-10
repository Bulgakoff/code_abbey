all_vow = ['a', 'u', 'o', 'y', 'i']
vow = 'o a kak ushakov lil vo kashu kakao'


def find_vow(vw, av):
    find_v = []
    for ch in vw:
        if ch in av:
            find_v.append(ch)
    result = len(find_v)
    print(f'quantity letters  {find_v} vowels {result}')



find_vow(vow, all_vow)
print('///////////////////////////////////')



