# python tkinter tutorial
# tee-kinter , tk-inter(tk-interface),kinter

# starter code 
# from tkinter import *
# import tkinter
import re
import os
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
win=tk.Tk()
win.title('GUI')


# create labels
# widgets ------> label,button,radio buttons - tk, ttk
name_label=ttk.Label(win,text='Enter your name : ')
name_label.grid(row=0,column=0, sticky=tk.W)

emial_label=ttk.Label(win,text="Enter your email : ")
emial_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter your age : ')
age_label.grid(row=2,column=0, sticky=tk.W)

gender_label=ttk.Label(win,text='select your gender : ')
gender_label.grid(row=3,column=0, sticky=tk.W)

# create entry box....
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=20,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=20,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.IntVar()
age_entrybox=ttk.Entry(win,width=20,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

# create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=16,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female',"other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1,sticky=tk.W)

# radio button
# student, teacher
usertype =tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="student",value='student',variable=usertype)
radiobtn1.grid(row=4,column=0,sticky=tk.W)
radiobtn1=ttk.Radiobutton(win,text="teacher",value='teacher',variable=usertype)
radiobtn1.grid(row=4,column=1,sticky=tk.W)

# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text="check if you want to subscribe to our newsletter ",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


# create button
# def action():
#     username = name_var.get()
#     useremail = email_var.get()  
#     userage = age_var.get()
#     usergender = gender_var.get()
#     user_type= usertype.get()
#     if checkbtn_var.get() ==0:
#         subscribed='NO'
#     else:
#         subscribed = 'Yes'   
#     print(f"{username} is {userage} year old , {useremail} \n user gender :{usergender} \n usertype :{user_type} \n Subscribe : {subscribed}")

#     with open('file.txt','a') as f:
#         f.write(f"{username},{userage},{useremail},{usergender},{user_type},{subscribed}\n")

#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     name_label.configure(foreground='Blue')
#     submit_button.configure(foreground='Blue')
    
# write to csv file
def action():
    username = name_var.get()
    useremail = email_var.get()  
    userage = age_var.get()
    usergender = gender_var.get()
    user_type= usertype.get()
    if checkbtn_var.get() ==0:
        subscribed='NO'
    else:
       subscribed = 'Yes' 

    with open('file2.csv','a',newline='') as f:
        dict_writer= DictWriter(f,fieldnames=['User Name','User Email Address','User Age','User Gender','User Type','Subscribed'])
        if os.stat('file2.csv').st_size ==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            "User Name" : username,
            'User Email Address' : useremail,
            'User Age':userage,
            'User Gender':usergender,
            'User Type': user_type,
            'Subscribed' : subscribed
        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue')


submit_button=tk.Button(win,text="submit",command=action)
submit_button.grid(row=6,column=0,sticky=tk.W)



# pack , grid
win.mainloop()