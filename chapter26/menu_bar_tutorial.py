import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('MENUBAR')

def func():
    print('func')
#menu
# menubar=tk.Menu(win)
# ************************ simple menubar *******************
# menubar.add_command(label='save',command=func)
# menubar.add_command(label='save as',command=func)
# menubar.add_command(label='copy',command=func)
# menubar.add_command(label='paste',command=func)

main_menu =tk.Menu(win)
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New window',command=func)
file_menu.add_command(label='open File ',command=func)
file_menu.add_separator()
file_menu.add_command(label='open recent',command=func)
main_menu.add_cascade(label='File',menu=file_menu)

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='cut',command=func)
edit_menu.add_command(label='copy',command=func)
edit_menu.add_command(label='paste',command=func)
main_menu.add_cascade(label='Edit',menu=edit_menu)

win.config(menu=main_menu)

win.mainloop()