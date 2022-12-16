import tkinter
from tkinter import Canvas, Text
from gui.gui import *


import subprocess
from threading import Thread
from queue import Queue, Empty

class Script():

    def __init__(self,parent):
        self.parent = parent


    def draw(self):

        canvas = Canvas(
            self.parent.window,
            bg = Color.WHITE,
            width = SUBSCREEN_WIDTH,
            height = SUBSCREEN_HEIGHT,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 230, y = 72)
        line = 0

        self.logbox = Text(canvas, width=96, height=27)
        self.logbox.pack()

        threading.Thread(target=self.captureOutput, daemon=True).start()

        return canvas
    
    def captureOutput(self):
        p = subprocess.Popen(["sh",getFilePath("arch-compile.sh"),"--deploy"], stdout=subprocess.PIPE)
        while p.poll() is None: # process is still running
            line = p.stdout.readline()
            while line:
                self.logbox.insert("end", line)
                line = p.stdout.readline()
                self.logbox.see("end")
        self.logbox.insert("end", "--- done ---\n")



    