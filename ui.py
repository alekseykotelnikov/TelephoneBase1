

def initial():
    print('''Здравствуйте, Вас приветствует "Телефонный справочник"!
Он сейчас пуст,давайте загрузим данные.
В каком виде будем загружать?''')
    how = input('Строками (row) или колонками (col): ')
    return how


def added_abonent(guide):
    str = ''
    str += ' ' + input('Введите фамилию: ')
    str += ' ' + input('Введите имя: ')
    str += ' ' + input('Введите номер телефона: ')
    str += ' ' + input('Введите примечание: ')
    guide.append(str.split())
    return guide


def next_operation():
    n = int(input('Что делаем дальше?\n1-Снова загрузим справочник\n2-Выгрузим справочник\n3-Добавить абонента\n4-Закончим работу\nВыберите действие: '))
    how = ' '
    if n == 1:
        how = input('Как загружаем, строками (row) или колонками (col): ')
    if n == 2:
        how = input('Как будем выгружать, строками (row) или колонками (col): ')
    if n == 4:
        print('Спасибо за работу, до новых встреч!')
    return n, how
