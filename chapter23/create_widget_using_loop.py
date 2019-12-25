# for loop
import os
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
win=tk.Tk()
win.title("LOOP")

labels=['what is your name : ','what is your age : ','what is your gender : ','Country :' ,'state :' ,'city :','address :']
for i in range(len(labels)):
    cur_lable = 'lable'+str(i) # lable0, label1,label2
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

# entry box
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
    cur_entrybox=ttk.Entry(win,width=20,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1)
    counter+=1
    # cur_var=tk.StringVar()

    # cur_entrybox =ttk.Entry(win,width=20,textvariable=cur_var)
    # cur_entrybox.grid(row=i,column=1)
    
def submit():
    for i in user_info:
        i=user_info[i].get()
        print(i)

    with open('file.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['Name','Age','Gender','Country','State','City','Address'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        # dict_writer.writerow=(dict([user_info[i]:i for i in user_info])
        dict_writer.writerow({
            'Name' : user_info['name'].get(),
            'Age' : user_info['age'].get(),
            'Gender' : user_info['gender'].get(),
            'Country' : user_info['country'].get(),
            'State' : user_info['state'].get(),
            'City' : user_info['city'].get(),
            'Address' : user_info['address'].get()
        })

submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=7,columnspan=2)
win.mainloop()