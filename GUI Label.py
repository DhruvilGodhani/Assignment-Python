from tkinter import*
w=Tk()
w.geometry("300x300")
l1=Label(text="First")
l2=Label(text="Second")
l3=Label(text="Third")
l4=Label(text="Forth")

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)
l4.grid(row=0,column=3)

w.mainloop()