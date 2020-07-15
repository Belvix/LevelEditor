from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image

#grass = Image.open("Images/Grass.png")

class Box:
    def __init__(self):
        #global grass
        self.root = Tk()        
        self.master = self.root
        self.myFrame = Frame(self.master)
        self.myFrame.pack()
        #grass = ImageTk.PhotoImage(grass)
        self.val = 1
        self.lbl = Label(self.myFrame, text='h')
        self.lbl.pack()




