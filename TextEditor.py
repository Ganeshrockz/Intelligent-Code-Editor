# coding: latin-1

import Tkinter as tk
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import time


lineColPosList=[]




def callback(event):
    lineColPosList = textPad.index(CURRENT).split('.')
    print textPad.index(CURRENT)
    status["text"]="Line" + lineColPosList[0] + " Column " + lineColPosList[1]
    
root = tk.Tk(className="Intelligent Code Editor")
textPad = ScrolledText(root, width=500, height=100,fg="white",bg="black")
textPad.config(font=("Arial",20),insertbackground="white")
lineColPosList = textPad.index(CURRENT).split('.')

textPad.bind("<Button-1>", callback)
textPad.bind("<Key>", callback)
textPad.focus()
status = Label(root, text="Line" + lineColPosList[0] + " Column " + lineColPosList[1], bd=1, relief=SUNKEN, anchor=W) 
status.pack(side=BOTTOM, fill=X)


def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = self.textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")

def open_file():
    resultFile = open("intermediate.txt","r")
    resultFile2 = open("intermediate2.txt","r")
    content = resultFile.read()
    prev_content = resultFile2.read()
    resultFile2.close()
    if(content != prev_content):
        textPad.insert(INSERT,content)
        textPad.insert(INSERT,'\n')
    resultFile.close()
    resultFile2 = open("intermediate2.txt","w")
    resultFile2.write(content)
    resultFile2.close()
    textPad.after(1000,open_file)


open_file()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)


textPad.pack()
root.mainloop()




