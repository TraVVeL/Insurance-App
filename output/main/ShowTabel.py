import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
import os
from data import LABEL_INSURANCE_1, LABEL_INSURANCE_2, LABEL_POLICY_1, LABEL_POLICY_2, LABEL
from tkinter import messagebox


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        # Создаем Treeview-виджет с горизонтальной и вертикальной прокруткой
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            # Устанавливаем опцию stretch для каждого заголовка столбца
            table.heading(head, text=head, anchor=tk.CENTER, command=lambda c=head: self.sortby(table, c, 0))
            table.column(head, anchor=tk.CENTER, width=100, minwidth=50, stretch=True)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        # Создаем горизонтальный Scrollbar-виджет и связываем его с Treeview-виджетом
        hscrollbar = ttk.Scrollbar(self, orient='horizontal', command=table.xview)
        table.configure(xscrollcommand=hscrollbar.set)

        # Размещаем Treeview-виджет и Scrollbar-виджет на форме
        table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.table = table

    def sortby(self, tv, col, descending):
        data = [(tv.set(child, col), child) for child in tv.get_children('')]
        data.sort(reverse=descending)
        for index, item in enumerate(data):
            tv.move(item[1], '', index)
        tv.heading(col, command=lambda: self.sortby(tv, col, int(not descending)))


def show_table(db_path, table_name):

    if os.path.isfile(db_path):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                rows_count = cursor.fetchone()[0]
            except sqlite3.OperationalError:
                rows_count = False

            if rows_count:
                cursor.execute(f"SELECT * FROM {table_name}")
                data = cursor.fetchall()

                concatenated_list = LABEL_POLICY_1 + LABEL_POLICY_2 if table_name == 'policy' else (
                    LABEL_INSURANCE_1 + LABEL_INSURANCE_2 if table_name == 'insurance' else LABEL)

                root = tk.Tk()
                Table(root, headings=concatenated_list, rows=tuple(data)).pack(expand=tk.YES, fill=tk.BOTH)
            else:
                messagebox.showinfo("Пустая таблица", "Таблица не содержит данных.")

    else:
        messagebox.showinfo("Пустая таблица", "Таблица не содержит данных.")
