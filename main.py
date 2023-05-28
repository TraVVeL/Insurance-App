"""Разработка бизнес-процессов страховой компанией автомобилей,
    включая:
     * оформление полисов;
     * обработку страховых случаев;
     * претензий клиентов;

    Оформление полиса:
     1. срок страхования с @date_start _/ --- :EXAMPLE: __.__.__г.
        по @date_end --- :EXAMPLE: __.__.__г.
     2. Страхование распространяется на страховые случаи, произошедшие в период использования ТС в течение срока
        страхования с @insurance_date_start по @insurance_date_end --- EXAMPLE1 __.__.__г. EXAMPLE2 __.__.__г.
     3. Страхователь (полное наименования: Имя, Фамилия, Отчество) @full_name --- :EXAMPLE: Борисов Дмитрий Евгеньевич
     4. Собственник ТС (полное наименование: Имя, Фамилия, Отчество) @car_owner_name --- :EXAMPLE: Борисова Светлана Николаевна
     5. Марка, модель ТС @car_brand, @car_model _/ --- :EXAMPLE: Daewoo Nexia
        Идентификационный номер ТС @car_id _/ @state_number --- :EXAMPLE: XW3L32EDCA245992
        Государственный регистрационный знак ТС --- @state_number --- :EXAMPLE: E776BP35
     8. Паспорт ТС, свидетельство о регистрации ТС, паспорт самоходной машины
        вид документа @document_view _/ --- :EXAMPLE: Свидетельство о регистрации ТС
        серия @series _/ --- :EXAMPLE: 3501
        номер @number --- :EXAMPLE: 260548
     9. Лица, допущенные к управлению ТС (Фамилия, Имя, Отчество) @admitted_person _/ --- :EXAMPLE: Гераничев Дмитрий Евгеньевич
        Водительское удостоверение (серия, номер) @drive_license _/ --- :EXAMPLE: 3510 521615
        Коэффициент КБМ @coefficient --- :EXAMPLE: 0.7
     10. Дата заключения договора @conclusion_date --- :EXAMPLE: 19 апреля 21г.
"""

from placeholder import Placeholder
from ShowTabel import show_table
from Verify_Input import *

root = tk.Tk()
root.geometry()
root.title('Страхование')
root.resizable()
root.attributes('-fullscreen', False)

root.maxsize(width=root.winfo_screenwidth(), height=root.winfo_screenwidth())


def admin_login():
    # Создаем окно для ввода имени пользователя и пароля
    login_window = tk.Tk()
    login_window.geometry("300x300")
    # Создаем текстовые поля для ввода имени пользователя и пароля
    username_label = tk.Label(login_window, text="Имя пользователя:")
    username_label.place(x=75, y=10)
    username_entry = tk.Entry(login_window)
    username_entry.place(x=75, y=30, width=150, height=30)

    password_label = tk.Label(login_window, text="Пароль:")
    password_label.place(x=75, y=80)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.place(x=75, y=100, width=150, height=30)

    # Функция для обработки кнопки входа
    def login_handler():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "pass":
            login_window.destroy()
            show_table_1_btn.place(x=10, y=options_frame.winfo_screenheight() / 1.25 - 300)
            show_table_2_btn.place(x=10, y=options_frame.winfo_screenheight() / 1.25 - 200)
            show_table_3_btn.place(x=10, y=options_frame.winfo_screenheight() / 1.25 - 100)

        else:
            error_label = tk.Label(login_window, text="Неправильное имя пользователя или пароль")
            error_label.place(x=25, y=250)
            # messagebox.showwarning("Ошибка", "Неверный пароль или логин!")

    # Создаем кнопку для входа
    login_button = tk.Button(login_window, text="Войти", command=login_handler, width=20, height=2)
    login_button.place(x=75, y=170)


    # Запускаем окно для ввода имени пользователя и пароля
    login_window.mainloop()


def registration_certificate_authority():
    """Оформление полисов"""

    policy_frame = tk.Frame(main_frame)

    # Определение положений Entry на экране

    y_pos = [i for i in range(100, 901, 80)]
    # entries = {}

    for (idx, label), placeholder in zip(enumerate(LABEL_POLICY_1), PLACEHOLDER_POLICY_1):
        label = tk.Label(policy_frame, text=label, background=AQUA)
        label.place(x=100, y=y_pos[idx], width=LABEL_W, height=ENTRY_H)

        entry = Placeholder(policy_frame, placeholder=placeholder, font=('Bold', 12))
        entry.bind("<KeyRelease>", lambda event: check_input(event, policy_frame,
                                                             ENTRIES_POLICY_DATA.items(), SQL_COLUMN_POLICY))
        entry.place(x=350, y=y_pos[idx], width=ENTRY_W, height=ENTRY_H)
        # entries[label.cget("text")] = entry

    for (idx, label), placeholder in zip(enumerate(LABEL_POLICY_2), PLACEHOLDER_POLICY_2):
        label = tk.Label(policy_frame, text=label, background=AQUA)
        label.place(x=860, y=y_pos[idx], width=LABEL_W, height=ENTRY_H)
        entry = Placeholder(policy_frame, placeholder=placeholder, font=('Bold', 12))
        entry.bind("<KeyRelease>", lambda event: check_input(event, policy_frame,
                                                             ENTRIES_POLICY_DATA.items(), SQL_COLUMN_POLICY))
        entry.place(x=1110, y=y_pos[idx], width=ENTRY_W, height=ENTRY_H)
        # entries[label.cget("text")] = entry

    button_submit = tk.Button(policy_frame, text='Отправить', command=lambda: save_data(length=17,
                                                                                        COLUMN=SQL_COLUMN_POLICY))
    button_submit.place(x=860, y=900, width=ENTRY_W + LABEL_W, height=ENTRY_H)

    policy_frame.place(relx=0.0, rely=0.0, anchor=tk.NW)
    policy_frame.configure(width=root.winfo_screenwidth() - 270, height=root.winfo_screenheight() - 20,
                           background=BACKGROUND_MAIN)

    # return entries


def insurance_claim_process():
    """Обработка страховых случаев"""
    insurance_frame = tk.Frame(main_frame)

    # Определение положений Entry на экране

    y_pos = [i for i in range(100, 901, 80)]
    # entries = {}

    for (idx, label), placeholder in zip(enumerate(LABEL_INSURANCE_1), PLACEHOLDER_INSURANCE_1):
        label = tk.Label(insurance_frame, text=label, background=AQUA)
        label.place(x=100, y=y_pos[idx], width=LABEL_W, height=ENTRY_H)

        entry = Placeholder(insurance_frame, placeholder=placeholder, font=('Bold', 12))
        entry.bind("<KeyRelease>", lambda event: check_input(event, insurance_frame,
                                                             ENTRIES_INSURANCE_DATA.items(), SQL_COLUMN_INSURANCE))
        entry.place(x=350, y=y_pos[idx], width=ENTRY_W, height=ENTRY_H)
        # entries[label.cget("text")] = entry

    for (idx, label), placeholder in zip(enumerate(LABEL_INSURANCE_2), PLACEHOLDER_INSURANCE_2):
        label = tk.Label(insurance_frame, text=label, background=AQUA)
        label.place(x=860, y=y_pos[idx], width=LABEL_W, height=ENTRY_H)
        entry = Placeholder(insurance_frame, placeholder=placeholder, font=('Bold', 12))
        entry.bind("<KeyRelease>", lambda event: check_input(event, insurance_frame,
                                                             ENTRIES_INSURANCE_DATA.items(), SQL_COLUMN_INSURANCE))
        entry.place(x=1110, y=y_pos[idx], width=ENTRY_W, height=ENTRY_H)
        # entries[label.cget("text")] = entry

    button_submit = tk.Button(insurance_frame, text='Отправить', command=lambda: save_data(length=20,
                                                                                           COLUMN=SQL_COLUMN_INSURANCE))
    button_submit.place(x=860, y=900, width=ENTRY_W + LABEL_W, height=ENTRY_H)

    insurance_frame.place(relx=0.0, rely=0.0, anchor=tk.NW)
    insurance_frame.configure(width=root.winfo_screenwidth() - 270, height=root.winfo_screenheight() - 20,
                              background=BACKGROUND_MAIN)

    # return entries


def customer_claim():
    """Претензии клиентов"""
    claim_frame = tk.Frame(main_frame)

    label = tk.Label(claim_frame, text='Куда', font=('Bold', 12), background=AQUA)
    label1 = tk.Label(claim_frame, text='Кому', font=('Bold', 12), background=AQUA)
    label.place(x=975, y=100, width=150, height=ENTRY_H)
    label1.place(x=975, y=150, width=150, height=ENTRY_H)

    label_2 = tk.Label(claim_frame, text='ПИСЬМО ПРЕТЕНЗИЯ О НАРУШЕНИИ УСЛОВИЙ ДОГОВОРА', font=('Bold', 12),
                       background=AQUA)
    label_2.place(x=claim_frame.winfo_screenwidth() / 4.5, y=300, width=800, height=ENTRY_H)

    entry = tk.Entry(claim_frame, font=('Bold', 12))
    entry.place(x=1125, y=100, width=200, height=ENTRY_H)
    entry1 = tk.Entry(claim_frame, font=('Bold', 12))
    entry1.place(x=1125, y=150, width=200, height=ENTRY_H)

    text = tk.Text(claim_frame, font=('Bold', 12))
    text.place(x=claim_frame.winfo_screenwidth() / 6, y=400, width=1000, height=450)

    submit = tk.Button(claim_frame, text='отправить', command=lambda: check_claim(entry, entry1, text))
    submit.place(x=922, y=875, width=ENTRY_W, height=ENTRY_H)

    claim_frame.place(relx=0.0, rely=0.0, anchor=tk.NW)
    claim_frame.configure(width=root.winfo_screenwidth() - 270, height=root.winfo_screenheight() - 20,
                          background=BACKGROUND_MAIN)


def about_page():
    about_frame = tk.Frame(main_frame)
    about_frame.pack(pady=20)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def hide_indicators():
    policy_indicate.config(bg=LIGHT_GRAY)
    indicate_btn.config(bg=LIGHT_GRAY)
    claim_indicate.config(bg=LIGHT_GRAY)


def indicate(lb, page):
    hide_indicators()
    lb.config(bg=AQUA)
    delete_pages()
    page()
    label_main_text.destroy()
    label_main.destroy()


options_frame = tk.Frame(root, bg=BACKGROUND_MENU)

policy_button = tk.Button(options_frame, text='Оформление полиса',
                          font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                          command=lambda: indicate(policy_indicate, registration_certificate_authority))
policy_button.place(x=10, y=70)
policy_indicate = tk.Label(options_frame, text='', bg=LIGHT_GRAY)
policy_indicate.place(x=3, y=70, width=5, height=60)

insurance_btn = tk.Button(options_frame, text='Обработка страховых\nслучаев',
                          font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                          command=lambda: indicate(indicate_btn, insurance_claim_process))
insurance_btn.place(x=10, y=170)
indicate_btn = tk.Label(options_frame, text='', bg=LIGHT_GRAY)
indicate_btn.place(x=3, y=170, width=5, height=60)

claim_btn = tk.Button(options_frame, text='Претензии клиентов',
                      font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                      command=lambda: indicate(claim_indicate, customer_claim))
claim_btn.place(x=10, y=250)
claim_indicate = tk.Label(options_frame, text='', bg=LIGHT_GRAY)
claim_indicate.place(x=3, y=250, width=5, height=60)

show_table_entry = tk.Button(options_frame, text='Войти',
                             font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                             command=admin_login)
show_table_entry.place(x=10, y=options_frame.winfo_screenheight() / 1.25)

# Создаем окно приложения и кнопку для отображения таблицы
show_table_1_btn = tk.Button(options_frame, text='Просмотр базы данных \nполисов',
                             font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                             command=lambda: show_table(db_path='policy.db', table_name='policy'))

# Создаем окно приложения и кнопку для отображения таблицы
show_table_2_btn = tk.Button(options_frame, text='Просмотр базы данных \nстраховых случаев',
                             font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                             command=lambda: show_table(db_path='insurance.db', table_name='insurance'))

# Создаем окно приложения и кнопку для отображения таблицы
show_table_3_btn = tk.Button(options_frame, text='Просмотр базы данных \nпретензий',
                             font=('Bold', 15), fg=AQUA, bg=LIGHT_GRAY, bd=0, width=21, height=2,
                             command=lambda: show_table(db_path='claim.db', table_name='claim'))

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=250, height=root.winfo_screenheight())

main_frame = tk.Frame(root, background=BACKGROUND_MAIN)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)

label_main_text = tk.Label(text="ПАМЯТКА", font=('Bold', 25), background=AQUA)
label_main_text.place(x=main_frame.winfo_screenwidth() / 7.7, y=0, width=main_frame.winfo_screenwidth(), height=100)

label_main = tk.Label(text=INSURANCE_TEXT, font=('Bold', 12), background='#336666')
label_main.place(x=main_frame.winfo_screenwidth() / 7.7, y=100, width=main_frame.winfo_screenwidth(), height=1000)

middle_line = tk.Label(options_frame, text='', bg=AQUA)
middle_line.place(x=247, y=0, width=3, height=2000)
main_frame.configure(width=root.winfo_screenwidth(), height=root.winfo_screenheight())

root.mainloop()
