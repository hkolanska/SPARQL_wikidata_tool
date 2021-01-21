from wikidata_connection.simple_query import SimpleQuery
import tkinter as tk
from tkinter import ttk
from GUI.GUI import show
from wikidata_connection.enums import select_possibilities, where_possibilities, \
    friendly_names
from wikidata_connection.query import Query
import sys


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
            cb = ttk.Checkbutton(self, text=value, variable=self.vars_to_checkbox[-1])
            self.checkbox_pairs.append((number, cb))
            self.text.window_create("end", window=cb)
            self.text.insert("end", "\n")

    def get_marked_numbers(self):
        list_of_numbers = []
        for number, checkbox in self.checkbox_pairs:
            if checkbox.instate(['selected']):
                list_of_numbers.append(number)
        return list_of_numbers


class App():
    def __init__(self):
        self.query = None
        self.select_checkboxes_list = None
        self.where_checkboxes_list = None
        self.limit = None
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
        selectframe = ttk.Frame(root, padding="10 10 5 5")
        selectframe.pack(side="top", fill="y", expand=True)

        variable = tk.StringVar(selectframe)
        variable.set("all")  # default value

        select_text = tk.Label(selectframe, text="Show me ")
        select_text.pack(side="left", fill="x")
        w = tk.OptionMenu(selectframe, variable, *(self.limit_to_select.keys()),
                          command=self.set_limit)
        w.pack(side="left", fill="both", expand=True)

        select_text = tk.Label(selectframe, text="countries and their")
        select_text.pack(side="right", fill="both", expand=True)
        return selectframe

    def create_select_parameters_frame(self, root):
        parametersframe = ttk.Frame(root, padding="10 10 10 10")
        self.select_checkboxes_list = CheckboxList(parametersframe,
                                                   [(key, friendly_names[key])
                                                    for key in
                                                    friendly_names.keys() if
                                                    key < 5])
        self.select_checkboxes_list.grid(row=0, column=0)
        return parametersframe

    def create_where_frame(self, root):
        whereframe = ttk.Frame(root, padding="10 10 10 10")
        select_text = tk.Label(whereframe,
                               text="Choose countries, which are a part of")
        select_text.grid(row=0, column=0)
        self.where_checkboxes_list = CheckboxList(whereframe,
                                                  [(key, friendly_names[key])
                                                   for key in
                                                   friendly_names.keys() if
                                                   key > 4])
        self.where_checkboxes_list.grid(row=1, column=0)
        return whereframe

    def set_order_by(self, selection):
        if self.order_by_to_select[selection] in self.select_checkboxes_list.get_marked_numbers():
            self.order_by = self.order_by_to_select[selection]

    def create_order_by_frame(self, root):
        order_by_frame = ttk.Frame(root, padding="10 10 10 10")
        select_text = tk.Label(order_by_frame, text="Order by")
        select_text.grid(row=0, column=0)
        variable = tk.StringVar(order_by_frame)
        variable.set("Country name")  # default value
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
            # self.query.run_query()
            print(self.query.query)

    def create_query_view(self):
        root = tk.Tk()
        root.title("Create Querry")
        selectframe = self.create_select_frame(root)
        selectframe.grid(row=0, column=0)
        parametersframe = self.create_select_parameters_frame(root)
        parametersframe.grid(row=1, column=0)
        whereframe = self.create_where_frame(root)
        whereframe.grid(row=2, column=0)
        order_by_frame = self.create_order_by_frame(root)
        order_by_frame.grid(row=3, column=0)

        bottomframe = ttk.Frame(root, padding="20 20 40 10")
        bottomframe.grid(row=4, column=0)

        run_button = tk.Button(bottomframe, text="RUN",
                               command=lambda: [self.make_query(),
                                                root.destroy(),
                                                self.results_view()])
        run_button.pack(side="left", expand=True, padx=10, pady=5)
        root.mainloop()

    def results_view(self):
        root = tk.Tk()
        label = tk.Label(root, text="Results", font=("Arial", 30)).grid(row=0,
                                                                        columnspan=3)
        cols = self.query.head  # ('Position', 'Name', 'Score')
        listBox = tk.ttk.Treeview(root, columns=cols, show='headings')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        show(listBox, self.query.results)

        showScores = tk.Button(root, text="New query", width=15,
                               command=lambda: [root.destroy(),
                                                self.create_query_view()]).grid(
            row=4, column=0)
        closeButton = tk.Button(root, text="Close", width=15,
                                command=exit).grid(
            row=4, column=1)

        root.mainloop()


app = App()

app.create_query_view()
