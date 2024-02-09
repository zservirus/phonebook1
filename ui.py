from logger import *

def interface():
    clear_screen()
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    var = ''
    while var != '4':
        print(
            'Меню:\n'
            '1.Добавить контакт\n'
            '2.Вывести на экран все контакты\n'
            '3.Поиск контакта\n'
            '4.Выход\n'
        )
        var = input('выберите варинт действия:')
        while var not in ('1', '2', '3', '4'):
            print('неккоректный ввод')
            var = input('выберите варинт действия:')

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                interface_search()
            case '4':
                exit()

def interface_search():
    var = ''
    while var != '4':
        print(
            'Меню поиска:\n'
            '1. По Фамилия\n'
            '2. По Имени\n'
            '3. По Отчеству\n'
            '4. По Телефону\n'
            '5. По Городу\n'
            '6. выход в меню'
        )
        var = input('выберите варинт поиска: ')
        while var not in ('1', '2', '3', '4', '5', '6'):
            print('неккоректный ввод')
            var = input('выберите варинт поиска: ')
            clear_screen()
        match var:
            case '1':
                search = input('Введите Фамилия контакта: ')
            case '2':
                search = input('Введите Имя контакта: ')
            case '3':
                search = input('Введите Отчество контакта: ')
            case '4':
                search = input('Введите телефон контакта: ')
            case '5':
                search = input('Введите Город контакта: ')
            case '6':
                interface()
        id_var = int(var) - 1
        search_contact(0, id_var, search)
