import tkinter as tk

def add2(event=None): #event =none is used to handle the event caused by by keryboard(ENTER)
    r = entry.get()
    if r:
        list1.append(r)
        listbox.insert(tk.END, r)
        entry.delete(0, tk.END)

def insert():
    global entry
    entry = tk.Entry(root, width=50, borderwidth=5, insertwidth=5)
    entry.place(x=410, y=120)
    entry.bind("<Return>", add2)  # Bind the Enter key to the add2 function
    button1 = tk.Button(root, text="ENTER", command=lambda: add2()) # YOU CAN EVEN USE ENTER BUTTON FROM KEYBOARD
    button1.place(x=440, y=150)

def add():
    insert()

root = tk.Tk()
root.title("to do list in gui")
root.geometry("1000x700")
listbox = tk.Listbox(root, height=10, width=50)
listbox.place(x=10, y=50)
list1 = ['Wake up early', 'breakfast', 'jogging', 'bathing']
for i in list1:
    listbox.insert(tk.END, i)

def delete_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

listbox.bind("<<ListboxSelect>>", lambda event: delete_selected())

button1 = tk.Button(root, text="ADD", command=add)
button1.place(x=440, y=90)

root.mainloop()
