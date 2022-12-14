import tkinter
from tkinter import Canvas, Entry, Button, PhotoImage, Label
from gui.gui import *
import threading

from gui.script import Script


class Home():

    def __init__(self,parent):
        self.parent = parent

    def clearFrame(self):
        for widgets in self.parent.frame.winfo_children():
            widgets.destroy()


    def draw(self):

        self.clearFrame()

        global homeButtonImage

        canvas = Canvas(
            self.parent.frame,
            bg = Color.WHITE,
            width = SUBSCREEN_WIDTH,
            height = SUBSCREEN_HEIGHT,
            bd = 0,
            highlightthickness = 0,
            relief = tkinter.RIDGE
        )

        canvas.place(x = 0, y = 0)
        line = 0

        line += TITLE_SIZE
        drawCenteredCanvasText(canvas,"ESP32-CAM MicroPython GUI",line,TITLE_SIZE,SUBSCREEN_WIDTH)
        line += TITLE_SIZE * 3
        drawCenteredCanvasText(canvas,"This is a program for ESP32-CAM",line,SUBTITLE_SIZE,SUBSCREEN_WIDTH)
        line += TITLE_SIZE * 4
        drawCenteredCanvasText(canvas,"You're able to compile and deploy MicroPython in ESP32-CAM",line,NORMAL_TEXT_SIZE,SUBSCREEN_WIDTH)
        line += TITLE_SIZE * 1.5
        drawCenteredCanvasText(canvas,"Made by @bitstuffing with love",line,NORMAL_TEXT_SIZE,SUBSCREEN_WIDTH)
        line += TITLE_SIZE * 2
        drawCenteredCanvasText(canvas,"Tap to Continue to start process",line,NORMAL_TEXT_SIZE,SUBSCREEN_WIDTH)

        homeButtonImage = PhotoImage(file=getFilePath("button.png"))
        
        button = Button(
            canvas,
            text = "Continue",
            image=homeButtonImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: threading.Thread(target=self.buttonClick,daemon=True).start(),
            relief=tkinter.FLAT,
            bg=Color.WHITE,
            activebackground=Color.WHITE,
            compound=tkinter.CENTER)
        
        button.pack(side=tkinter.TOP)

        button.place(x=0, y=0, relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        canvas.update()
        self.parent.window.update()

        return canvas
    
    
    def buttonClick(self): #TODO
        print("clicked")
        self.parent.handleButton(buttonName="console")
        
