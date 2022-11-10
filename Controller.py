import Model
import View

def start_app():
    View.launch_interface()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list
        Model.update_book()

def save_file():
    save_switch = True
    if Model.phonebook == []:
        save_switch = View.empty_save_warning()
    if save_switch == True:
        with open(Model.path, "w", encoding="UTF-8") as data:
            data.write(('\n'.join(Model.phonebook)))

def save_backup():
    with open(Model.path, "r", encoding="UTF-8") as source:
        backup = source.read()
    backup_switch = True
    if backup.strip() == '':
        backup_switch = View.empty_save_warning()
    if backup_switch == True:
        with open(Model.path_backup, "w", encoding="UTF-8") as data:
            data.write(backup)

def restore_from_backup():
    with open(Model.path_backup, "r", encoding="UTF-8") as source:
        backup = source.read()
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(backup)
    open_file()
    Model.update_book()


# def try_enter_int(enter_text):
#     while True:
#         text = input(f'{enter_text}')
#         try:
#             return int(text)
#         except:
#             print ('\nНеправильно набран номер')
        
