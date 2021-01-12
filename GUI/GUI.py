def show(listbox, data):
    for data_row in data:
        listbox.insert("", "end", values=data_row)

