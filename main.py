from tkinter import *
from PIL import ImageTk, Image
import os
import random
import time
root = Tk()
pos = 0
def _quit():
    root.quit() 
    root.destroy() 

green = ImageTk.PhotoImage(Image.open("bin/green.jpg"))
arrow = ImageTk.PhotoImage(Image.open("bin/arrow.jpg"))
red = ImageTk.PhotoImage(Image.open("bin/red.jpg"))
T = 250
dur = 0
lvl = 0
def _update():
    global dur,pos
    if(dur == 1):
        return
    a,b = 50,5
    for i in range(36):
        if(i==pos):
            panel = Label(root, image = red)
            panel.place(x=a,y=b)
        if(i==(pos+35)%36):
            panel = Label(root, image = green)
            panel.place(x=a,y=b)
        if(i<10):
            a+= 55
        elif(i<18):
            b+= 55
        elif(i<28):
            a-= 55
        else:
            b-= 55   
    pos=(pos+1)%36
    root.after(T-lvl*30, _update)

def _start():
    status.configure(text="____")
    global dur,pos
    dur,pos,a,b = 0,random.randint(0, 35),50,5
    for i in range(36):
        panel = Label(root, image = green)
        panel.place(x=a,y=b)
        if(i<10):
            a+= 55
        elif(i<18):
            b+= 55
        elif(i<28):
            a-= 55
        else:
            b-= 55 
    _update()
just = 0
def relax():
    global just
    if(just == 0):
        just = 1
        root.after(T, relax)
    else:
        just = 0
        _start()
def key(event):
    global dur,lvl
    if len(event.char) == 1 and str(event.keysym)=='space':
        dur = 1
        if(pos==6):
            lvl = lvl + 1
            relax()
        else:
            status.configure(text=str(lvl*100)+" points")
            lvl = 0
    if(event.char == event.keysym and event.char=='n'):
        lvl,dur = 0,1
        relax()

root.geometry("700x500")
root.title("Game")
root.bind_all('<Key>', key)
status = Label(root, text="---",font=("Helvetica", 20))
status.place(x=320,y=175)
panel = Label(root, image = arrow)
panel.place(x=328,y=60)
close_button = Button(root, text="Close", command=_quit)
close_button.place(x=330,y=380)
_start()
root.mainloop()