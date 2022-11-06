import Model
import View

def main_menu():
    while True:
        print('\nТелефонный справочник - главное меню:')
        print('0. Показать все контакты')
        print('1. Открыть файл с контактами')
        print('2. Записать файл с контактами')
        print('3. Добавить контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Поиск п контактам')
        print('9. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        if choice == 0:
            View.printPhoneBook()

        elif choice == 2:
            save_file()
            print('\nФайл сохранен!\n')
        elif choice == 3:
            add_contact()
            print('\nКонтакт добавлен\n')
        elif choice == 4:
            change_contact()           
        elif choice == 5:
            remove_contact()
            print('\nКонтакт удален\n')

        elif choice == 9:
            break
        else:
            print("'\nНеправильно набран номер!\n'")

def start():
    open_file()
    main_menu()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():
    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))
    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, '; '.join(contact))
    View.printPhoneBook()


