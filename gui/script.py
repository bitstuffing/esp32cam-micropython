import tkinter
from tkinter import Canvas, Text
from gui.gui import *


import subprocess
from threading import Thread
from queue import Queue, Empty

def Script(parent):

    canvas = Canvas(
        parent.window,
        bg = "#FFFFFF",
        width = SUBSCREEN_WIDTH,
        height = SUBSCREEN_HEIGHT,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 230, y = 72)
    line = 0

    logbox = Text(canvas, width=96, height=27)
    logbox.pack()
    
    def captureOutput():
        p = subprocess.Popen(["sh",getFilePath("arch-compile.sh"),"--deploy"], stdout=subprocess.PIPE)
        while p.poll() is None: # process is still running
            logbox.insert("end", p.stdout.readline())
            logbox.see("end")
        logbox.insert("end", "--- done ---\n")

    threading.Thread(target=captureOutput, daemon=True).start()


    