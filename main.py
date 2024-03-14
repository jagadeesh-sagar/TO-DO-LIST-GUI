import tkinter as tk
def add2(entry):
    r=entry.get()
    list1.append(r)
    listbox.insert(tk.END,r)
    entry.delete(0,tk.END)
def insert():
    entry=tk.Entry(root,width=10)
    entry.pack()
    button1=tk.Button(root,text="enter",command=lambda k=entry:add2(k))
    button1.pack()
def add():
    insert()
root=tk.Tk()
root.title("to do list in gui")
root.geometry("1000x700")
listbox=tk.Listbox(root,height=8)
listbox.pack()
list1=['Wake up early','breakfast','jogging','bathing']
for i in list1:
    listbox.insert(tk.END,i)
def delete_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)


listbox.bind("<<ListboxSelect>>", lambda event: delete_selected())

button1=tk.Button(root,text="ADD",command=add)
button1.pack()

root.mainloop()


