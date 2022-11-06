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
    print(f"Добавлен контакт: {contact}")

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    print(f"Удален контакт: {phonebook[choice]}")
    phonebook.pop(choice)

def change_contact():
    View.printPhoneBook()
    choice = int(input('Введите номер элемента для изменения: '))
    if choice < len(phonebook):
        contact = phonebook.pop(choice).split(';')
    else:
        return
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))    
    if 0 >= choice >= 3:
        contact[choice2] = input('Введите новое значение: ')
        print(f"Изменен контакт: {contact}")
        phonebook.insert(choice, '; '.join(contact))
    else:
        return