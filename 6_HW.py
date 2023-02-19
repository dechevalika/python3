""" 1. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

# a1 = int(input())
# d = int(input())
# n = int(input())
# progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*progressive)


""" 2. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума) """

# from random import randint

# lst = [randint(-10, 10) for i in range(15)]
# print(lst)
# min_number = int(input())
# max_number = int(input())
# for i in range(len(lst)):
#     if min_number <= lst[i] <= max_number:
#         print(i)