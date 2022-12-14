from pathlib import Path
import tkinter
from tkinter import *
import threading
from gui.gui import *
from gui.home import Home
from gui.script import Script

class App():

    global window

    global section
    global canvas
    global canvas2
    global breadcrum
    global sidebarNavigator
    global currentWindow
    global section

    def handleButton(self,buttonName):
        
        self.canvas.update_idletasks()

        if buttonName == "home":
            self.section = "Welcome" 
            self.currentWindow = Home(self)
        elif buttonName == "console":
            self.section = "Compile" 
            self.currentWindow = Script(self)
        self.homeButtonClick()
        
            
    def homeButtonClick(self): 
        print("Home button clicked")
        self.canvas.itemconfig(self.breadcrum, text=self.section)
        self.sidebarNavigator.place(x=0, y=133)    

    def main(self):
        self.window = Tk()
        self.window.title("ESP32-CAM GUI")
        self.window.iconphoto(False,tkinter.PhotoImage(file=getFilePath("openhardware.png")))
        self.window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
        self.window.configure(bg = BACKGROUND_COLOR)

        self.section = "Welcome" 

        self.canvas = Canvas(
            self.window,
            bg = BACKGROUND_COLOR,
            height = WINDOW_HEIGHT,
            width = 930,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.canvas2 = Canvas(
            self.window,
            bg = Color.WHITE,
            height = SUBSCREEN_HEIGHT,
            width = 230 - 30,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas2.place(x = 15, y = 72)

        self.currentWindow = Home(self)

        buttonImage = PhotoImage(file=getFilePath("button.png"))
        homeButton = Button(
            self.canvas2,
            text = "Welcome",
            image=buttonImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleButton("home"), 
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF',
            compound='center')
        
        homeButton.pack(side="top")
        homeButton.place(x=0, y=0, relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        consoleButton = Button(
            self.canvas2,
            text = "Compile",
            image=buttonImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleButton("console"), 
            relief="flat",
            bg='#FFFFFF',
            activebackground='#FFFFFF',
            compound='center')
        
        consoleButton.pack(side="top")
        consoleButton.place(x=0, y=0, relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        
        self.sidebarNavigator = Frame(background="#FFFFFF")
        self.sidebarNavigator.place(x=0, y=133, height=47, width=7)

        self.breadcrum = self.canvas.create_text(
            alignRight(WINDOW_WIDTH,len(self.section),SUBTITLE_SIZE),
            SUBTITLE_SIZE/2,
            anchor="nw",
            text=self.section,
            fill=Color.WHITE,
            font=("Montserrat Bold", SUBTITLE_SIZE))

        #App name
        self.canvas.create_text(             
            TITLE_SIZE/2, 
            TITLE_SIZE/2,
            anchor="nw",
            text="ESP32-CAM Utility",
            fill=Color.WHITE,
            font=("Montserrat Bold", TITLE_SIZE)
        )

        self.window.resizable(False, False)
        self.window.mainloop()

