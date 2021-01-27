from wikidata_connection.simple_query import SimpleQuery
import tkinter as tk
from tkinter import ttk
from wikidata_connection.to_choice import friendly_names

from GUI.CheckboxList import CheckboxList


def show(listbox, data):
    for data_row in data:
        listbox.insert("", "end", values=data_row)


class AppUI:
    def __init__(self):
        self.query = None
        self.select_checkboxes_list = None
        self.where_checkboxes_list = None
        self.limit_to_select = {"all": None, "top 5": 5, "top 10": 10,
                                "top 100": 100}
        self.order_by_to_select = {"Country name": 0, 'Population': 1,
                                   'Life expectancy': 2,
                                   'GDB': 3, "Capital": 4}
        self.limit = 0
        self.order_by = 0

    def set_limit(self, selection):
        self.limit = self.limit_to_select[selection]

    def create_select_frame(self, root):
        self.limit = 0
        self.order_by = 0
        select_frame = ttk.Frame(root, padding="10 10 5 5")
        select_frame.pack(side="top", fill="y", expand=True)

        variable = tk.StringVar(select_frame)
        variable.set("all")  # default value

        select_text = tk.Label(select_frame, text="Show me ")
        select_text.pack(side="left", fill="x")
        w = tk.OptionMenu(select_frame, variable,
                          *(self.limit_to_select.keys()),
                          command=self.set_limit)
        w.pack(side="left", fill="both", expand=True)

        select_text = tk.Label(select_frame, text="countries and their")
        select_text.pack(side="right", fill="both", expand=True)
        return select_frame

    def create_select_parameters_frame(self, root):
        parameters_frame = ttk.Frame(root, padding="10 10 10 10")
        self.select_checkboxes_list = CheckboxList(parameters_frame,
                                                   [(key, friendly_names[key])
                                                    for key in
                                                    friendly_names.keys() if
                                                    key < 5])
        self.select_checkboxes_list.grid(row=0, column=0)
        return parameters_frame

    def create_where_frame(self, root):
        where_frame = ttk.Frame(root, padding="10 10 10 10")
        select_text = tk.Label(where_frame,
                               text="Choose countries, which are a part of")
        select_text.grid(row=0, column=0)
        self.where_checkboxes_list = CheckboxList(where_frame,
                                                  [(key, friendly_names[key])
                                                   for key in
                                                   friendly_names.keys() if
                                                   key > 4])
        self.where_checkboxes_list.grid(row=1, column=0)
        return where_frame

    def set_order_by(self, selection):
        if self.order_by_to_select[selection] in \
                self.select_checkboxes_list.get_marked_numbers():
            self.order_by = self.order_by_to_select[selection]

    def create_order_by_frame(self, root):
        order_by_frame = ttk.Frame(root, padding="10 10 10 10")
        select_text = tk.Label(order_by_frame, text="Order by")
        select_text.grid(row=0, column=0)
        variable = tk.StringVar(order_by_frame)
        variable.set("Country name")
        w = tk.OptionMenu(order_by_frame, variable,
                          *(self.order_by_to_select.keys()),
                          command=self.set_order_by)
        w.grid(row=0, column=1)
        return order_by_frame

    def make_query(self):
        if self.select_checkboxes_list and self.where_checkboxes_list:
            select_values = self.select_checkboxes_list.get_marked_numbers()
            where_values = self.where_checkboxes_list.get_marked_numbers()
            self.query = SimpleQuery(select_values, where_values,
                                     limit=self.limit, order_by=self.order_by)
            self.query.create_query()
            self.query.run_query()
            print(self.query.query)

    def create_query_view(self):
        root = tk.Tk()
        root.title("Create Query")
        select_frame = self.create_select_frame(root)
        select_frame.grid(row=0, column=0)
        parameters_frame = self.create_select_parameters_frame(root)
        parameters_frame.grid(row=1, column=0)
        where_frame = self.create_where_frame(root)
        where_frame.grid(row=2, column=0)
        order_by_frame = self.create_order_by_frame(root)
        order_by_frame.grid(row=3, column=0)

        bottom_frame = ttk.Frame(root, padding="20 20 40 10")
        bottom_frame.grid(row=4, column=0)

        run_button = tk.Button(bottom_frame, text="RUN",
                               command=lambda: [self.make_query(),
                                                root.destroy(),
                                                self.results_view()])
        run_button.pack(side="left", expand=True, padx=10, pady=5)
        root.mainloop()

    def results_view(self):
        root = tk.Tk()
        tk.Label(root, text="Results", font=("Arial", 30)).grid(row=0,
                                                                columnspan=3)
        cols = self.query.head
        list_box = tk.ttk.Treeview(root, columns=cols, show='headings')
        for col in cols:
            list_box.heading(col, text=col)
        list_box.grid(row=1, column=0, columnspan=2)
        show(list_box, self.query.results)

        tk.Button(root, text="New query", width=15, command=lambda:
                [root.destroy(), self.create_query_view()]).grid(row=4, column=0)
        tk.Button(root, text="Close", width=15, command=exit).grid(row=4,
                                                                   column=1)

        root.mainloop()
