import tkinter as tk
from tkinter import messagebox
import Model
import Controller
     
missing = '<не указано>'

def no_selection_error():
    messagebox.showerror('Ошибка: не выбран пункт', 'Ничего не выбрано!')

def empty_save_warning():
    empty_save = messagebox.askquestion('Внимание: пустой список', 'Вы хотите записать пустой список?', icon='warning')
    if empty_save == 'yes':
        return True
    else:
        return False

def launch_interface():
    window = tk.Tk()
    window.geometry(f"660x500")
    window.title("Телефонный справочник")

    Model.name = tk.StringVar()
    Model.surname = tk.StringVar()
    Model.last_name = tk.StringVar()
    Model.phone = tk.StringVar()

    frame = tk.Frame()
    frame.pack()
    frame1 = tk.Frame()
    frame1.pack()
    frame2 = tk.Frame()
    frame2.pack()
    frame3 = tk.Frame()
    frame3.pack()
    frame4 = tk.Frame()
    frame4.pack()

    tk.Label(frame, text='Телефонный справочник', height = 2).pack()

    tk.Label(frame1, text='Имя:', width = 10).pack(side=tk.LEFT)
    tk.Entry(frame1, textvariable=Model.name, width = 40).pack()

    tk.Label(frame2, text='Фамилия:', width = 10).pack(side=tk.LEFT)
    tk.Entry(frame2, textvariable=Model.surname, width = 40).pack()

    tk.Label(frame3, text='Отчество:', width = 10).pack(side=tk.LEFT)
    tk.Entry(frame3, textvariable=Model.last_name, width = 40).pack()

    tk.Label(frame4, text='Телефон:', width = 10).pack(side=tk.LEFT)
    tk.Entry(frame4, textvariable=Model.phone, width = 40).pack()

    tk.Button(window, text='Очистить', width=10, command=Model.reset_contact).place(x=520,y=50)
    tk.Button(window, text='Изменить', width=10, command=Model.change_contact).place(x=520,y=80)
    tk.Button(window, text='Обновить список', width=30,command=Model.update_book).place(x=20,y=150)
    tk.Button(window, text='Открыть файл', width=30,command=Controller.open_file).place(x=20,y=180)
    tk.Button(window, text='Записать в файл', width=30, command=Controller.save_file).place(x=20,y=210)
    tk.Button(window, text='Добавить контакт', width=30, command=Model.add_contact).place(x=20,y=240)
    tk.Button(window, text='Выбрать контакт', width=30, command=Model.select_contact).place(x=20,y=270)
    tk.Button(window, text='Удалить контакт', width=30, command=Model.delete_contact).place(x=20,y=300)
    tk.Button(window, text='Найти контакты', width=30, command=Model.filter_contacts).place(x=20,y=330)
    tk.Button(window, text='Сделать резервную копию', width=30, command=Controller.save_backup).place(x=20,y=360)
    tk.Button(window, text='Восстановить из резервной копии', command=Controller.restore_from_backup, width=30).place(x=20,y=390)
    tk.Button(window, text='Выход', width=30, command=window.destroy).place(x=20,y=420)

    scroll_bar = tk.Scrollbar(window, orient=tk.VERTICAL)
    Model.select = tk.Listbox(window, yscrollcommand=scroll_bar.set, width=60, height=19)
    scroll_bar.config(command=Model.select.yview)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    Model.select.place(x=250, y=150)

    window.mainloop()