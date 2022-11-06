import Model


def printPhoneBook():
    print("\n***Телефонный справочник***")
    for i, item in enumerate(Model.phonebook, 1):
        print(i , item)

