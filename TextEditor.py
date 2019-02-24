# coding: latin-1

import Tkinter as tk
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import time
import pyautogui


lineColPosList=[]




def callback(event):
    lineColPosList = textPad.index(CURRENT).split('.')
    print textPad.index(CURRENT)
    status["text"]="Line" + lineColPosList[0] + " Column " + lineColPosList[1]
    
root = tk.Tk(className="Intelligent Code Editor")
textPad = ScrolledText(root, width=500, height=100,fg="white",bg="black")
textPad.config(font=("Arial",15),insertbackground="white")
lineColPosList = textPad.index(CURRENT).split('.')

textPad.bind("<Button-1>", callback)
textPad.bind("<Key>", callback)
textPad.focus()
status = Label(root, text="Line" + lineColPosList[0] + " Column " + lineColPosList[1], bd=1, relief=SUNKEN, anchor=W) 
status.pack(side=BOTTOM, fill=X)

def replaceText(inputText):
    inputText = inputText.replace('of','[]')
    inputText = inputText.replace('function','')
    inputText = inputText.replace('increment','')
    inputText = inputText.replace('initialize','')
    inputText = inputText.replace('condition','')
    inputText = inputText.replace('math','')
    inputText = inputText.replace('equals','=')
    inputText = inputText.replace('plus','+')
    inputText = inputText.replace('multiplies','*')
    inputText = inputText.replace('minus','-')
    inputText = inputText.replace('divides','/')
    inputText = inputText.replace('by','/')
    inputText = inputText.replace('xor','^')
    inputText = inputText.replace('and','&')
    inputText = inputText.replace('or','|')
    inputText = inputText.replace('percent','%')
    inputText = inputText.replace('less than','<')
    inputText = inputText.replace('greater than','>')
    inputText = inputText.replace('less than or equals','<=')
    inputText = inputText.replace('greater than or equals','>=')
    inputText = inputText.replace('not equals','!=')
    inputText = inputText.replace('zero',"0")
    inputText = inputText.replace('one',"1")
    inputText = inputText.replace('two',"2")
    inputText = inputText.replace('three',"3")
    inputText = inputText.replace('four',"4")
    inputText = inputText.replace('five',"5")
    inputText = inputText.replace('six',"6")
    inputText = inputText.replace('seven',"7")
    inputText = inputText.replace('eight',"8")
    inputText = inputText.replace('nine',"9")
    inputText = inputText.replace('ten',"10")
    inputText = inputText.replace('hundered',"100")
    inputText = inputText.replace('thousand',"1000")
    inputText = inputText.replace('integer','int')
    inputText = inputText.replace('character','char')
    return inputText

def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    #if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
    root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Just another texteditor that eases coding through its intelligent processing abilities")

def editorStatusActionFunction(action):
    editorStatusFile = open("./editorStatus.txt","w")
    editorStatusFile.write(action)
    editorStatusFile.close()
def executeEditorCommands(inputList):
    if(inputList[1] == "save"):
        editorStatusActionFunction("save")
        save_command()
    elif(inputList[1] == "about"):
        editorStatusActionFunction("about")
        about_command()
    elif(inputList[1] == "exit"):
        exit_command()
    elif(inputList[1] == "open"):
        editorStatusActionFunction("open")
        open_command()
    elif(inputList[1] == "close"):
        editorStatusFile =open("./editorStatus.txt","r")
        content =editorStatusFile.read()
        content = content.split(' ')
        if content[0]=="save":
            pyautogui.keyDown("alt")
            pyautogui.press("c")
            pyautogui.keyUp("alt")
        elif content[0]=="open":
            pyautogui.keyDown("alt")
            pyautogui.press("c")
            pyautogui.keyUp("alt")
        elif content[0]=="about":
            pyautogui.keyDown("alt")
            pyautogui.press("o")
            pyautogui.keyUp("alt")
    elif(inputList[1] == "goto"):
        lineNumber = inputList[len(inputList)-1]
        lineNumber = replaceText(lineNumber)
        textPad.mark_set("insert",lineNumber+".0")
    return
def open_file():
    resultFile = open("intermediate.txt","r")
    resultFile2 = open("intermediate2.txt","r")
    content = resultFile.read()
    prev_content = resultFile2.read()
    resultFile2.close()
    wordsContent = content.split(' ')
    if(content != prev_content and wordsContent[0]!="editor"):
        textPad.insert(INSERT,content)
    elif(content != prev_content and wordsContent[0] == "editor"):
        executeEditorCommands(wordsContent)
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




