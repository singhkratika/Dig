from tkinter import*
import time

root=Tk()
root.title("Digital Clock")
root.geometry("400x100")
root.config(bg="black")

def update():
 clock.config(text= time.strftime("%I:%M:%S:%p"))
 clock.after(1000,update)
clock=Label(root,background ="black",foreground ="white",font=("Arial 40 bold"))
clock.pack()
update()
root.mainloop()