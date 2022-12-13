from pathlib import Path
import tkinter
from tkinter import *
import threading
from gui.gui import *
from gui.home import Home

class App():

    global window

    global section
    global canvas
    global breadcrum
    global sidebarNavigator
    global currentWindow
    global section

    def handleButton(self,buttonName):
        
        if buttonName == "home":
            self.homeButtonClick()
            currentWindow = Home(self.window)
        elif buttonName == "other_screen":
            pass
        
            
    def homeButtonClick(self): 
        print("Home button clicked")
        self.canvas.itemconfig(self.breadcrum, text=self.breadcrum)
        self.sidebarNavigator.place(x=0, y=133)    

    def main(self):
        self.window = Tk()
        self.window.title("ESP32-CAM GUI")
        self.window.iconphoto(False,tkinter.PhotoImage(file=getFilePath("micropython.png")))
        self.window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
        self.window.configure(bg = BACKGROUND_COLOR)

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

        currentWindow = Home(self.window)

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
            text = "Scripts",
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
        
        section = "Welcome" 

        self.sidebarNavigator = Frame(background="#FFFFFF")
        self.sidebarNavigator.place(x=0, y=133, height=47, width=7)

        self.breadcrum = self.canvas.create_text(
            alignRight(WINDOW_WIDTH,len(section),SUBTITLE_SIZE),
            SUBTITLE_SIZE/2,
            anchor="nw",
            text=section,
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

