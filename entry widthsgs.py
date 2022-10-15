import tkinter
root=tkinter.Tk()
root.geometry("500x500")
name_var=tkinter.StringVar()
password_var=tkinter.StringVar()

def submit():
    name=name_var.get()
    password=password_var.get()
    username=tkinter.Label(text="Your name is "+name)
    userpas=tkinter.Label(text="Your password is "+password)
    username.grid(row=6,column=3,padx=500,pady=10)
    userpas.grid(row=7,column=3,padx=500,pady=10)
    name_var.set("")
    password_var.set("")
name_label=tkinter.Label(root,text='Username',font=('Arial','10','bold'))
name_entry=tkinter.Entry(root,textvariable=name_var,font=('Arial','10','normal'))
password_label=tkinter.Label(root,text='Password',font=('Arial','10','normal'))
password_entry=tkinter.Entry(root,textvariable=password_var,font=('Arial','10','normal'),show='.')

sub_btn=tkinter.Button(root,text='submit',command=submit)
name_label.grid(row=1,column=3,padx=500,pady=10)
name_entry.grid(row=2,column=3,padx=500,pady=10)

password_label.grid(row=3,column=3,padx=500,pady=10)
password_entry.grid(row=4,column=3,padx=500,pady=10)

sub_btn.grid(row=5,column=3,padx=500,pady=10)
root.mainloop()