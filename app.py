from wikidata_connection.simple_query import SingleQuery
import tkinter as tk
from tkinter import ttk
from GUI.GUI import show
from wikidata_connection.query import Query


def create_query_view():
    root = tk.Tk()
    root.title("Example")

    mainframe = ttk.Frame(root, padding="20 20 40 40")
    mainframe.pack()

    variable = tk.StringVar(mainframe)
    variable.set("one")  # default value


    w = tk.OptionMenu(mainframe, variable, "one", "two", "three")
    w.pack()

    text_show = tk.Text(root)
    text_show.pack(side=tk.LEFT, expand=True, padx=10, pady=5)

    entry1_var = tk.StringVar()
    entry2_var = tk.StringVar()

    entry1_var.set('First Entry')
    entry2_var.set('Second Entry')

    entry1_ent = tk.Entry(mainframe, textvariable=entry1_var)
    entry1_ent.pack(side=tk.LEFT, expand=True, padx=10, pady=5)
    entry1_var.get()
    entry2_ent = tk.Entry(mainframe, textvariable=entry2_var)
    entry2_ent.pack(side=tk.LEFT, expand=True, padx=10, pady=5)
    entry2_var.get()

    print_button = tk.Button(mainframe, text="RUN", command=exit)
    print_button.pack(side=tk.LEFT, expand=True, padx=10, pady=5)

    root.mainloop()


def results_view(query: Query):
    root = tk.Tk()
    label = tk.Label(root, text="Results", font=("Arial", 30)).grid(row=0,
                                                                    columnspan=3)
    cols = query.head  # ('Position', 'Name', 'Score')
    listBox = tk.ttk.Treeview(root, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    show(listBox, query.results)

    showScores = tk.Button(root, text="New query", width=15, command=exit).grid(row=4, column=0)
    closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(
        row=4, column=1)

    root.mainloop()


create_query_view()

# query = SingleQuery([1,2,3,4], 1, 100)
# query.create_query()
# print(query.query)
# query.run_query()
# print(query.results)
# results_view(query)
