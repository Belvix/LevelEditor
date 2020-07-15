from tkinter import *
import pygame
import settings

class Elder:
    def __init__(self):
        self.root = Tk()
        self.root.title("Menu")
        self.master = self.root
        self.myFrame = Frame(self.master)
        self.myFrame.pack()
        self.sendButton = Button(self.myFrame, text='send', command=self.sendData)
        self.myButton = Button(self.myFrame, text='close', command=self.end)
        self.widthM = Label(self.myFrame, text="No of tiles W:")
        self.heightM = Label(self.myFrame, text="No of tiles H")
        self.widthM.grid(row=0, column=0)
        self.heightM.grid(row=1, column=0)
        self.wEntry = Entry(self.myFrame, borderwidth=5)
        self.hEntry = Entry(self.myFrame, borderwidth=5)
        self.wEntry.grid(row=0, column=1)
        self.hEntry.grid(row=1, column=1)
        self.sendButton.grid(row=2, column=0)
        self.myButton.grid(row=3, column=0)
        self.width = 0
        self.height = 0
        try:
            self.master.protocol("WM_DELETE_WINDOW", on_closing)
        except:
            pass
    def on_closing():
        self.sendData()
        root.destroy()
        
    def end(self):
        pygame.quit()
        sys.exit()

    def sendData(self):
        if int(self.wEntry.get()) != 0:
            settings.n_width = int(self.wEntry.get())
        else:
            settings.n_width = 10
        if self.hEntry.get() != '':
            settings.n_height = int(self.hEntry.get())
        else:
            settings.n_height = 10
        print(settings.n_width, settings.n_height)
        self.master.destroy()
