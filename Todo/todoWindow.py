#! usr/bin/python
#
# This is the To-Do list program creates a list full of tasks entered
# in the command line as syste arguments then manipulated based to user
# enter flags then (still not developed ->) displayed on a transparent
# widget on a desktop
#
# Notes:
# Functions need testing:
#
# Functions need to be build or debugged:
#
# Current error: Instead of refreshing the widget the program creates a window
# but doesn't refresh the window to in new data and show it
#
from Tkinter import *
import Tkinter as Tk, re
import tkFont
import datetime, time

class TodoWin(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.wm_attributes("-alpha",0.3)
        self.title('Todo')
        self.resizable(False,False)
        self.wm_overrideredirect(True)
        self.textDisplay()
        self.winGeometry()
        self.updater()



    def updater(self):
        self.after(10000,self.textDisplay)
        self.update_idletasks()
    def textDisplay(self,event=None):
        winFont = tkFont.Font(family='Times New Roman',size=10)
        timeNow = datetime.datetime.now()
        timeString = str(timeNow.hour)+":"+str(timeNow.minute)+":"+str(timeNow.second)+'\n\n'
        fileText = Text(self, width=45, height=20)
        fileText.configure(font=winFont)
        fileText.delete("1.0",END)
        fileText.insert(END,timeString)
        fileText.pack()
        filename = 'list.txt'

        with open(filename,'r') as f:
            fileText.insert(INSERT,f.read())

    def winGeometry(self):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws)-200
        y = hs -600
        self.geometry('%dx%d+%d+%d'%(200,250,x,y))


if __name__ == '__main__':
    main = TodoWin()
    main.mainloop()
