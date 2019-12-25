import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('Detail')
label_frame=tk.LabelFrame(win,text='Contact detail')
label_frame.grid(row=0,column=0,padx=40,pady=10)
label_frame.configure(foreground='Blue')

name_label=ttk.Label(label_frame,text='Enter your Name please : ',font=('Helvetica',14,'italic'))
age_label=ttk.Label(label_frame,text='Enter your Age please : ',font=('Helvetica',14,'italic'))
# name_label.focus()
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=2,padx=5,pady=5,sticky=tk.W)

name_var=tk.StringVar()
age_var=tk.StringVar()

name_entry=ttk.Entry(label_frame,width=20,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=20,textvariable=age_var)
name_entry.grid(row=0,column=1,padx=5,pady=5)
age_entry.grid(row=0,column=3,padx=5,pady=5)

def submit():
    
    # m_box.showwarning('title','content of this message box !!')

    name=name_var.get()
    age=age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error','please fill both name and age !!')
    else:
        try:
            # age='frrfnrnf'
            # age='20'
            age=int(age)
        except ValueError:
            m_box.showerror('Error','only digits are allowed in age  !!')
        else:
            if age < 18:
                m_box.showwarning('Warning','you are not 18,visit this content on your own risk !!')
            print(f'{name} and age :{age}')

submit_btn=ttk.Button(label_frame,text='submit',command=submit)
submit_btn.grid(row=2,columnspan=4,pady=10)

win.mainloop()