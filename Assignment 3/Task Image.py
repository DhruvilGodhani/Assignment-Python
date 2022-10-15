from tkinter import *
import random
window = Tk()
window.geometry("500x500")


def press(): 
    filechoices=["1.png","2.png"
            ,"3.png","4.png"
            ,"5.png","6.png"]
    filename=PhotoImage(file=random.choice(filechoices)) 
   
    image=Label(window,image=filename).pack()

button1=Button(window,text="Roll the Dies",command=press)
button1.pack()
window.mainloop()