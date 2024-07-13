import random


def get_password():
    n = random.randint(3, 20)
    """Множество для удаления дубликатов пар"""
    set_pairs = set()
    """Лист для хранения пар пароля"""
    list_pairs = []
    for a in range(1, 20):
        for b in range(1, 20):
            if a == b:
                continue
            elif n % (a + b) == 0:
                list_pairs.append([a, b])
    """[[a, b], [b, a]] -> [[a, b], [a, b]]"""
    for pair in list_pairs:
        pair.sort()
    """Избавляемся от дубликатов пар [a, b] и [a, b]"""
    for i in list_pairs:
        set_pairs.add(tuple(i))
    """set -> list; вложенные tupples -> list"""
    list_pairs = [list(i) for i in set_pairs]
    """Сортировка"""
    list_pairs.sort()
    """Избавляемся от вложенных списков"""
    single_list = []
    for i in list_pairs:
        for j in i:
            single_list.append(j)
    """Преобразовываем список элементов в единую строку с использованием генератора списков и метода join(), 
    используя пустую строку ("") в качестве разделителя"""
    result = "".join([str(i) for i in single_list])
    return print(int(result))


get_password()
