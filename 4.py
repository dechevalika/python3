''' 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. '''

num = int(input('Введите число: '))
result = ''

while num >= 1:
    int_num = num // 2     
    ost = num % 2      
    result += str(ost)
    num = int_num

print(result[::-1])
