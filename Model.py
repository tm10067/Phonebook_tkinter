import View

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
    View.printPhoneBook()
    choice = int(input('\nВведите номер контакта для удаления: '))
    if choice - 1 < len(phonebook): 
        print(f"\nУдален контакт: {phonebook[choice - 1]}")
        phonebook.pop(choice - 1)
    else:
        print("\nТакого элемента нет")
        return

def change_contact():
    View.printPhoneBook()
    choice = int(input('\nВведите номер контакта для изменения: '))
    if choice - 1 < len(phonebook):
        contact = phonebook.pop(choice - 1).split(';')
    else:
        print("\nТакого элемента нет")
        return
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))    
    if 0 <= choice <= 3:
        contact[choice2] = input('Введите новое значение: ')
        print(f"\nИзменен контакт: {contact}")
        phonebook.insert(choice - 1, '; '.join(contact))
    else:
        print("\nТакого элемента нет")
        return