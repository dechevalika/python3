""" 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. """

# СЖАТИЕ
def encod(s):   
    encod = '' 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encod += str(count) + s[i]
        i = i + 1
    return encod
 
print(encod(input('Введите строку: ')))


# ВОССТАНОВЛЕНИЕ
# def decod(s):
#     decod = ''
#     num = ''
#     for i in s:
#         if i.isalpha():
#             decod += i * int(num)
#             num = ''
#         else:
#             num += i
#     return decod

# print(decod(input('Введите строку: ')))
