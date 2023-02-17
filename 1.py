""" 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """

txt = input("Введите текст:\n")
abc = 'абв'
lst = [i for i in txt.split() if abc not in i]
print(f'Результат: {" ".join(lst)}')
