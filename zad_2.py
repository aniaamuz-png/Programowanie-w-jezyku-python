def multiple2(list):
    x = []
    for i in list:
        x.append(i * 2)
    return x


print(multiple2([1, 2, 3]))


def mltpl_3(list):
    return [x*2 for x in list]


print(multiple2([4, 5, 6]))
