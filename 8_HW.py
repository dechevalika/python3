

# меню
def menu():
    print('-----------------------')
    num1 = '1. Просмотр'
    num2 = '2. Изменить данные'
    num3 = '3. Добавить запись'
    num4 = '4. Удалить'
    num5 = '5. Поиск'
    print(num1, num2, num3, num4, num5, sep = '\n')
    num_user = int(input('Введите номер функции: '))
    if num_user == 1:
        lst = read_data()
        screen(lst)
        back()
    elif num_user == 4:
        lst = read_data()
        delete_data(lst)
        back()
    elif num_user == 2:
        lst = read_data()
        change_data(lst)
        back()
    return num_user


# чтение из файла
def read_data():
    with open('tel.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        print('-----------------------')
        return lst


# 0. возврат в меню 
def back():
    back = int(input('Чтобы вернуться в меню, введите 0: '))
    menu()
    print('-----------------------')
    return back


# 1. просмотр 
def screen(lst):
    i = 1
    for elem in lst:
        print(f'{i}) ', elem.strip())
        i += 1


# 2. изменение
def change_data(lst):
    screen(lst)
    num_change = int(input('Какую запись вы хотите изменить? Введите номер записи: '))
    new_change = input('Введите новые данные: ')
    lst[num_change - 1] = new_change
    print(lst)
    write_data(lst)


# 3. добавление
def add_data():
    pass


# 4. удаление
def delete_data(lst):
    screen(lst)
    num_delete = int(input('Чтобы удалить запись, введите номер: '))
    del lst[num_delete - 1]
    write_data(lst)


# 5. поиск 
def search_data():
    pass


# запись в файл
def write_data(lst):
    num_answer = str(input('Сохранить данные? Y/N: '))
    if num_answer == 'Y':
       with open('tel.txt', 'w', encoding='utf-8') as file:
        lst = file.writelines('%s\n' % i for i in lst)
        print('Успешное сохранение')
        return lst
    else:
        back()
    

def main():
    menu()
    
    
if __name__ == '__main__':
    main()