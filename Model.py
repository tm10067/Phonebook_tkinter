import View
import Controller

phonebook = []
path = 'PhoneBookConsole/phone.txt'
path_backup = 'PhoneBookConsole/phone_back.txt'

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    phonebook.append(contact)
    print(f"\nДобавлен контакт: {contact}")

def remove_contact():
    View.printPhoneBook("Телефонный справочник", phonebook)
    choice = Controller.try_enter_int('\nВведите номер контакта для удаления: ')
    if choice - 1 < len(phonebook): 
        print(f"\nУдален контакт: {phonebook[choice - 1]}")
        phonebook.pop(choice - 1)
    else:
        print("\nТакого элемента нет")
        return

def change_contact():
    View.printPhoneBook("Телефонный справочник", phonebook)
    choice = Controller.try_enter_int('\nВведите номер контакта для изменения: ')
    if choice - 1 < len(phonebook):
        contact = phonebook.pop(choice - 1).split('; ')
    else:
        print("\nТакого элемента нет")
        return
    choice2 = int(input('\nЧто изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))    
    if 0 <= choice2 <= 3:
        contact[choice2] = input('Введите новое значение: ')
        print(f"\nИзменен контакт: {contact}")
        phonebook.insert(choice - 1, '; '.join(contact))
    else:
        print("\nТакого элемента нет")
        return

def find_contact():
    choice = int(input('\nЧто ищем (0-имя, 1-фамилия, 2-отчество, 3-телефон, 4-порядковый номер): '))
    list_search = []    
    if 0 <= choice <= 3:
        search = input('\nВведите искомое значение: ')
        for i in range(len(phonebook)):
            sub_list_search = phonebook[i].split('; ')
            sub_string_search = sub_list_search[choice]
            if search.lower() in sub_string_search.lower().replace('-',''):
                print ()
                list_search.append(phonebook[i])
        if list_search == []:
            print("\nНичего не найдено")
            return
        else:
            View.printPhoneBook("Результат поиска", list_search)
            return
    elif choice == 4:
        search = Controller.try_enter_int('\nВведите искомый индекс: ')
        if search <= len(phonebook):
            print()
            print(phonebook[int(search)])
            return
        else:
            print("\nНичего не найдено")
            return
    else:
        print("\nТакого элемента нет")
        return