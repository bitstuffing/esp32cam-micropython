import tkinter
from tkinter import Canvas, Entry, Button, PhotoImage, Label
from gui.gui import *
import threading

def Home(parent):

    HOME_WIDTH = SUBSCREEN_WIDTH
    HOME_HEIGHT = SUBSCREEN_HEIGHT

    global homeButtonImage

    canvas = Canvas(
        parent,
        bg = "#FFFFFF",
        width = HOME_WIDTH,
        height = HOME_HEIGHT,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 230, y = 72)
    line = 0

    line += TITLE_SIZE
    drawCenteredCanvasText(canvas,"ESP32-CAM MicroPython GUI",line,TITLE_SIZE,HOME_WIDTH)
    line += TITLE_SIZE * 3
    drawCenteredCanvasText(canvas,"This is a program for ESP32-CAM",line,SUBTITLE_SIZE,HOME_WIDTH)
    line += TITLE_SIZE * 4
    drawCenteredCanvasText(canvas,"You're able to launch scripts from this console",line,NORMAL_TEXT_SIZE,HOME_WIDTH)
    line += TITLE_SIZE * 1.5
    drawCenteredCanvasText(canvas,"Made by @bitstuffing with love",line,NORMAL_TEXT_SIZE,HOME_WIDTH)
    line += TITLE_SIZE * 2
    drawCenteredCanvasText(canvas,"Tap to Continue to show next view",line,NORMAL_TEXT_SIZE,HOME_WIDTH)

    homeButtonImage = PhotoImage(file=getFilePath("button.png"))
    
    button = Button(
        canvas,
        text = "Continue",
        image=homeButtonImage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: threading.Thread(target=buttonClick,args=(parent,),daemon=True).start(),
        relief="flat",
        bg='#FFFFFF',
        activebackground='#FFFFFF',
        compound='center')
    
    button.pack(side="top")

    button.place(x=0, y=0, relx=0.5, rely=0.85, anchor=tkinter.CENTER)
    
    def buttonClick(self): #TODO
        print("clicked")
