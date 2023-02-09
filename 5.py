""" 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. """

k = int(input('Введите число: '))
lst = []


for i in range(0, k + 1):
    if i <= 1:
        lst.append(i)
    else:
        summa = lst[i - 1] + lst[i - 2]
        lst.append(summa)

lst_n = lst[::-1]

for i in range(len(lst_n)):
    if lst_n[i] == 0:
        lst_n.pop(i)
    elif i % 2 == 0:
        lst_n[i] = -lst_n[i]

lst = lst_n + lst

print(lst)
