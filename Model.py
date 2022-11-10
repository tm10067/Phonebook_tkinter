import View

phonebook = []
path = 'phone.txt'
path_backup = 'phone_back.txt'

name = None
surname = None
last_name = None
phone = None
select = None

def add_contact():
    phonebook.append(f'{name.get() or View.missing}; {surname.get() or View.missing}; {last_name.get() or View.missing}; {phone.get() or View.missing};\n')
    update_book()

def select_contact():
    while True:
        if len(select.curselection()) > 0:
            selected_string = (select.get(select.curselection()))
            index_pick = int(selected_string.split('. ')[0]) - 1
            selected_string_list = phonebook[index_pick].strip().strip(';').split('; ')
            name.set(selected_string_list[0])
            surname.set(selected_string_list[1])
            last_name.set(selected_string_list[2])
            phone.set(selected_string_list[3])
            break
        else:
            View.no_selection_error()
            break

def change_contact():
    if len(select.curselection()) > 0:
        selected_string = (select.get(select.curselection()))
        index_change = int(selected_string.split('. ')[0]) - 1
        phonebook[index_change] = f'{name.get() or View.missing}; {surname.get() or View.missing}; {last_name.get() or View.missing}; {phone.get() or View.missing};\n'
        update_book()
    else:
        View.no_selection_error()

def delete_contact():
    selected_string = (select.get(select.curselection()))
    index_del = int(selected_string.split('. ')[0]) - 1
    del phonebook[index_del]
    update_book()

def reset_contact():
    name.set('')
    surname.set('')
    last_name.set('')
    phone.set('')

def update_book():
    select.delete(0, 'end')
    for i in range(len(phonebook)):
        entry_list = phonebook[i].strip().strip(';').split('; ')
        select.insert('end', f'{i + 1}. {entry_list[1]} {entry_list[0]} {entry_list[2]} | {entry_list[3]}')

def filter_contacts():
    select.delete(0, 'end')
    sub_list_search = list(enumerate(phonebook,1))
    for i in sub_list_search:
        list_filter_entry = i[1].strip().strip(';').split('; ')
        if name.get() in list_filter_entry[0] and surname.get() in list_filter_entry[1] and last_name.get() in list_filter_entry[2] and phone.get() in list_filter_entry[3]:
            select.insert('end', f'{i[0]}. {list_filter_entry[1]} {list_filter_entry[0]} {list_filter_entry[2]} | {list_filter_entry[3]}')