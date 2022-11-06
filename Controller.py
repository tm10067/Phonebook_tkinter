import Model
import View

def main_menu():
    while True:
        print('\nТелефонный справочник - главное меню:')
        print('0. Показать все контакты (текущая версия)')
        print('1. Открыть файл с контактами (перезаписывает текущую версию)')
        print('2. Записать текущую версию в файл с контактами')
        print('3. Добавить контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Поиск по контактам')
        print('7. Записать резервную копию файла')
        print('8. Восстановить файл с резервной копии')
        print('9. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        if choice == 0:
            View.printPhoneBook()
        elif choice == 1:
            open_file()
            View.printPhoneBook()
        elif choice == 2:
            save_file()
            print('\nФайл сохранен!\n')
        elif choice == 3:
            Model.add_contact()
            print('\nКонтакт добавлен\n')
        elif choice == 4:
            Model.change_contact()           
        elif choice == 5:
            Model.remove_contact()
            print('\nКонтакт удален\n')
        elif choice == 7:
            save_backup()
            print('\nРезервная копия сохранена!\n')
        elif choice == 8:
            save_backup()
            print('\nФайл восстановлен с резервной копии!\n')
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

def save_backup():
    with open(Model.path, "r", encoding="UTF-8") as source:
        backup = source.read()
    with open(Model.path_backup, "w", encoding="UTF-8") as data:
        data.write(backup)

def restore_from_backup():
    with open(Model.path_backup, "r", encoding="UTF-8") as source:
        backup = source.read()
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(backup)

