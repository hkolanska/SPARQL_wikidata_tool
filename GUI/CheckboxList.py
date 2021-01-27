import tkinter as tk
from tkinter import ttk


class CheckboxList(tk.Frame):
    def __init__(self, root, value_pair_list, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.value_pair_list = value_pair_list

        self.vsb = tk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=20, height=5,
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.checkbox_pairs = []
        self.vars_to_checkbox = []
        for number, value in self.value_pair_list:
            self.vars_to_checkbox.append(tk.IntVar())
            cb = ttk.Checkbutton(self, text=value,
                                 variable=self.vars_to_checkbox[-1])
            self.checkbox_pairs.append((number, cb))
            self.text.window_create("end", window=cb)
            self.text.insert("end", "\n")

    def get_marked_numbers(self):
        list_of_numbers = []
        for number, checkbox in self.checkbox_pairs:
            if checkbox.instate(['selected']):
                list_of_numbers.append(number)
        return list_of_numbers
