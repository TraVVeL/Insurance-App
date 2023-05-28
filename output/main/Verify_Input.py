from tkinter import messagebox
from DataValidator import DataValidator as DV
from DataBase import insert_data
from data import *
import tkinter as tk

final_data = {}



def check_claim(entry, entry1, text):
    final_data.update({'dfrom': entry.get(), 'dto': entry1.get(), 'claim': text.get('1.0', tk.END)})

    save_data(length=3, COLUMN=SQL_COLUMN_CLAIM)


def check_input(event, widget_frame, ENTRIES_DATA, COLUMN):
    entry_name = event.widget.winfo_name()
    entry = event.widget
    text = entry.get()
    func_ = None
    arg = None
    error_text = ""
    fg_color = bg_color = BACKGROUND_MAIN
    hb = hc = 'white'

    for (frame, values), DB_ENTRY in zip(ENTRIES_DATA, COLUMN):
        if str(entry_name) == frame:
            if type(values[0]) == dict:
                func_, arg = list(values[0].keys())[0], list(list(values[0].values())[0].values())[0]
            else:
                func_ = values[0]

            dv_object = DV(text.lower())
            valid = getattr(dv_object, func_)(arg) if func_ and arg else getattr(dv_object, func_)()

            # Update error text and colors based on validation

            if not valid:
                error_text = values[1]
                fg_color = hb = hc = RED
                bg_color = LIGHT_GRAY
            elif valid:
                hb = hc = GREEN
                final_data.update({DB_ENTRY: text})
            entry.configure(highlightbackground=hb, highlightcolor=hc, highlightthickness=2)
            break

    # Create or update error label
    error_label = tk.Label(widget_frame, text=error_text, foreground=fg_color, background=bg_color)
    error_label.place(x=entry.winfo_x() - 250, y=entry.winfo_y() - 35, width=ENTRY_W + LABEL_W, height=ENTRY_H - 10)


def save_data(length, COLUMN):
    db = 'insurance.db' if length == 17 else ('policy.db' if length == 20 else 'claim.db')
    sorted_dict = {v: final_data[v] for v in COLUMN if v in final_data}
    data_to_store = tuple(sorted_dict.values())

    if sorted_dict != {} and len(sorted_dict) == length:
        insert_data([data_to_store], db_path=db)
        messagebox.showwarning("Успешно", "Значения занесены в базу данных!")
    else:
        messagebox.showwarning("Предупреждение", "Ячейки не полностью заполнены или некорректный ввод")
