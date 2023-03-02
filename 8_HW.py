

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
    elif num_user == 3:
        lst = read_data()
        add_data(lst)
        back()   
    elif num_user == 5:
        lst = read_data()
        search_data(lst)
        back()
    elif num_user > 5:
        print('Вы ввели неверное значение. Выберите пункт меню')
        menu()
    return num_user


# чтение из файла
def read_data():
    with open('tel.txt', 'r', encoding='utf-8') as file:
        # lst = file.readlines()
        lst = []
        for i in file:
            lst.append(i.strip('\n'))
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
    if num_change > len(lst):
        print('Записи с таким номером нет. Выберите одну из записей в списке')
        return change_data(lst)
    else:
        new_change = input('Введите новые данные: ')
        lst[num_change - 1] = new_change
        return write_data(lst)


# 3. добавление
def add_data(lst):
    new = input('Введите данные: ')
    lst.append(new)
    write_data(lst)


# 4. удаление
def delete_data(lst):
    screen(lst)
    num_delete = int(input('Чтобы удалить запись, введите номер: '))
    if num_delete > len(lst):
        print('Записи с таким номером нет. Выберите одну из записей в списке')
        return delete_data(lst)
    else:
        del lst[num_delete - 1]
        return write_data(lst)


# 5. поиск 
def search_data(lst):
    finded = str(input('Введите данные для поиска: '))
    finded_str = ''
    for i in lst:   
        if finded.lower() in i.lower():
            print(str(lst.index(i)+1)+')', i)
            finded_str = i
    if finded.lower() not in finded_str.lower():
        print('Ничего не найдено')
        

# запись в файл
def write_data(lst):
    num_answer = str(input('Сохранить данные? Y/N: '))
    if num_answer.capitalize() == 'Y':
       with open('tel.txt', 'w', encoding='utf-8') as file:
        lst = file.writelines(f'{i}\n' for i in lst)
        print('Успешное сохранение')
        return lst
    elif num_answer.capitalize() == 'N':
        print('Галя, ОТМЕНА!')
        back()
    else:
        print('Введите Y либо N: ')
        write_data(lst)
  
    
if __name__ == '__main__':
    menu()