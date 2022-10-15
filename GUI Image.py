import tkinter
m=tkinter.Tk()
m.geometry("500x500")
img=tkinter.PhotoImage(file="C:/Users/DELL/Desktop/Advance Python/6.png")
display=tkinter.Label(image=img)
display.pack()
m.mainloop()