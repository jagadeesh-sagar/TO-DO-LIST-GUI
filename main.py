import tkinter as tk
root=tk.Tk()
root.title("to do list in gui")
root.geometry("1000x700")
listbox=tk.Listbox(root,height=5)
listbox.pack()
list1=['Wake up early','breakfast','jogging','bathing']

root.mainloop()


