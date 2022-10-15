
from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("200x100")

def fun():
    messagebox.showinfo("Hello Dhruvil","Red Button clicked")  
def a():
    messagebox.showinfo("Hello Dhruvil","Blue Button clicked")
def b():
    messagebox.showinfo("Hello Dhruvil","Green Button clicked")  
def c():
    messagebox.showinfo("Hello Dhruvil","Yellow Button clicked")
    
b1=Button(top,text="Red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=Button(top,text="Blue",command=a,activeforeground="blue",activebackground="pink",pady=10)
b3=Button(top,text="Green",command=b,activeforeground="green",activebackground="pink",pady=10)
b4=Button(top,text="Yellow",command=c,activeforeground="yellow",activebackground="pink",pady=10)

b1.pack(side="left")
b2.pack(side="right")
b3.pack(side="top")
b4.pack(side="bottom")
top.mainloop()
