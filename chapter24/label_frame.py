import os
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
win=tk.Tk()
win.title("Label Frame ")

label_frame = tk.LabelFrame(win,text="enyter your detais below")
label_frame.grid(row=0,column=0,padx=100)
label_frame.configure(foreground='Blue')

labels=['what is your name : ','what is your age : ','what is your gender : ','Country :' ,'state :' ,'city :','address :']
for i in range(len(labels)):
    cur_lable = 'lable'+str(i) # lable0, label1,label2
    cur_label=ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

user_info={
    'name' :tk.StringVar(),
    'age' :tk.StringVar(),
    'gender' :tk.StringVar(),
    'country' :tk.StringVar(),
    'state' :tk.StringVar(),
    'city' :tk.StringVar(),
    'address':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox= 'entry' + i
    cur_entrybox=ttk.Entry(label_frame,width=20,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1)
    counter+=1

def submit():
    for i in user_info:
        i=user_info[i].get()
        print(i)


submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,column=0)

for child in label_frame.winfo_children():
    child.grid_configure(padx=2,pady=2)

win.mainloop()