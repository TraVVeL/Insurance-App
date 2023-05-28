import tkinter as tk


class Placeholder():
    def __init__(self, master, placeholder='', placeholdercolor='grey', color='black', **kwargs):
        self.e = tk.Entry(master, fg=placeholdercolor, **kwargs)
        self.e.bind('<FocusIn>', self.focus_in)
        self.e.bind('<FocusOut>', self.focus_out)
        self.e.insert(0, placeholder)
        self.placeholder = placeholder
        self.placeholdercolor = placeholdercolor
        self.color = color


    def pack(self, side=None, **kwargs):
        self.e.pack(side=side, **kwargs)

    def place(self, side=None, **kwargs):
        self.e.place(side=side, **kwargs)

    def grid(self, column=None, **kwargs):
        self.e.grid(column=column, **kwargs)


    def focus_in(self, e):
        if self.e.get() == self.placeholder:
            self.e.delete(0, tk.END)
        self.e.configure(fg=self.color)

    def focus_out(self, e):
        if self.e.get() == '':
            self.e.configure(fg=self.placeholdercolor)
            self.e.delete(0, tk.END)
            self.e.insert(0, self.placeholder)

    def bind(self, sequence=None, func=None, add=None, **kwargs):
        self.e.bind(sequence=sequence, func=func, add=add, **kwargs)

    def get(self):
        """Return the text."""
        return self.tk.call(self._w, 'get')
