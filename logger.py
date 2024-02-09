from data_create import *
from ui import *

def clear_screen(n=1):
    print("------------------------------------" * n)

def copy_contact(var_contact):
    with open('new_phonebook.txt', 'a', encoding='utf-8') as file_copy:
        file_copy.write(var_contact)
        file_copy.write("\n\n")

def create_contact():
    clear_screen()
    surname = input_surname()
    nane = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    clear_screen()
    print(f'Контакт:\n{surname} {nane} {patronymic}: {phone}\n{address}\n\n Добавлен в справочник')
    return f'{surname} {nane} {patronymic}: {phone}\n{address}\n\n'

def add_contact():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(create_contact())
        clear_screen()
def print_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
        clear_screen()
        print("#            ФИО                     телефон")
        clear_screen()
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)
        clear_screen()
    otvet = input('Скопировать контакт в новый справочник? Номера пропишите контактов через запятую: ')
    otvet_list = list(otvet.split(','))
    if otvet != '':
        search_contact(otvet_list)
        print('Контакт скопирован в new_phonebook.txt')
        clear_screen()

def search_contact(index_contact = None, case_search = 0, var_search = ''):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
    if index_contact != '':                     # если задан список номеров строк для копирования
        for i in index_contact:                     # перебираем список по нужным строкам
            copy_contact(contacts_list[int(i)-1])   # копируем выбранные пользователем контакты
    if case_search != 0:                            # Если пользователь ищет по атрибуту
        for str_contact in contacts_list:
            lst_contact = str_contact.split()
            if var_search.lower() in lst_contact[case_search].lower():
                clear_screen()
                print(str_contact)
                clear_screen()
                var_contact = str_contact
                otvet = input('Скопировать контакт в новый справочник? да/нет: ')
                if otvet.lower() == 'да':
                    copy_contact(var_contact)
                    print('Контакт скопирован в new_phonebook.txt')
                    clear_screen()

