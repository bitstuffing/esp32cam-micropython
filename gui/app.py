from pathlib import Path
import tkinter
from tkinter import *
import threading
from gui.gui import *
from gui.home import Home
from gui.script import Script

class App():

    window = None

    section = None
    canvas = None
    canvas2 = None
    breadcrum = None
    sidebarNavigator = None
    currentWindow = None
    section = None

    def clearFrame(self, frame=None):
        if frame is None:
            frame = self.frame
        for widgets in frame.winfo_children():
            widgets.destroy()

    def handleButton(self,buttonName):
        
        if buttonName == "home":
            self.section = "Welcome" 
            self.clearFrame(self.frame)
            self.currentWindow = Home(self).draw()
        elif buttonName == "console":
            self.section = "Compile" 
            self.clearFrame(self.frame)
            self.currentWindow = Script(self).draw()
        self.homeButtonClick()
        
            
    def homeButtonClick(self): 
        print("Home button clicked")
        self.clearFrame(self.sidebarNavigator)
        self.drawSideBar()


    def main(self):
        # build main window
        self.window = Tk()
        self.window.title("ESP32-CAM GUI")
        self.window.iconphoto(False,tkinter.PhotoImage(file=getFilePath("openhardware.png")))
        self.window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
        self.window.configure(bg = BACKGROUND_COLOR)
        self.window.resizable(False, False)

        #TOP FRAME - sidebar
        self.sidebarNavigator = Frame(self.window)
        self.sidebarNavigator.place(x=15, y=15, width=WINDOW_WIDTH-40, height=TITLE_SIZE*2)
        #MAIN FRAME - content
        self.frame = Frame(self.window)
        self.frame.place(x=FRAME_DOWN_X, y=FRAME_DOWN_Y, width=SUBSCREEN_WIDTH, height=SUBSCREEN_HEIGHT)
        #LEFT FRAME - menu
        self.frame2 = Frame(self.window)
        self.frame2.place(x=15, y=FRAME_DOWN_Y, width=WINDOW_WIDTH-SUBSCREEN_WIDTH - 60, height=SUBSCREEN_HEIGHT)

        ## DRAW GLOBALS

        #draw menu
        self.canvas2 = Canvas(
            self.frame2,
            bg = Color.WHITE,
            height = SUBSCREEN_HEIGHT,
            width = WINDOW_WIDTH-SUBSCREEN_WIDTH - 60,
            bd = 0,
            highlightthickness = 0,
            relief = tkinter.RIDGE
        )

        self.canvas2.place(x = 0, y = 0)

        buttonImage = PhotoImage(file=getFilePath("button.png"))
        homeButton = Button(
            self.frame2,
            text = "Welcome",
            image=buttonImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleButton("home"), 
            relief=tkinter.FLAT,
            bg=Color.WHITE,
            activebackground=Color.WHITE,
            compound=tkinter.CENTER)
        
        homeButton.pack(side=tkinter.TOP)
        homeButton.place(x=0, y=0, relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        consoleButton = Button(
            self.frame2,
            text = "Compile",
            image=buttonImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleButton("console"), 
            relief=tkinter.FLAT,
            bg=Color.WHITE,
            activebackground=Color.WHITE,
            compound=tkinter.CENTER)
        
        consoleButton.pack(side=tkinter.TOP)
        consoleButton.place(x=0, y=0, relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        
        ##DRAW CONTENT
        #self.currentWindow = Home(self).draw()
        self.handleButton(buttonName="home")
        
        #CONTINUE UI thread
        self.window.mainloop()

    def drawSideBar(self):

        self.canvas3 = Canvas(
            self.sidebarNavigator,
            bg = Color.WHITE,
            height = TITLE_SIZE*2,
            width = WINDOW_WIDTH-40,
            bd = 0,
            highlightthickness = 0,
            relief = tkinter.RIDGE
        )
        self.canvas3.place(x = 0, y = 0)

        self.canvas3.create_text(
            alignRight(WINDOW_WIDTH-40,len(self.section),SUBTITLE_SIZE),
            SUBTITLE_SIZE/2,
            anchor=tkinter.NW,
            text=self.section,
            fill=Color.BLACK,
            font=("Montserrat Bold", SUBTITLE_SIZE))

        
        self.canvas3.create_text(             
            TITLE_SIZE/2, 
            TITLE_SIZE/4,
            anchor=tkinter.NW,
            text="ESP32-CAM Utility",
            fill=Color.BLACK,
            font=("Montserrat Bold", TITLE_SIZE)
        )