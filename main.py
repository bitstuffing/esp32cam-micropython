from gui.app import App
import tkinter
from gui.gui import getFilePath, Color

if __name__=="__main__":

    root = tkinter.Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

    image = tkinter.PhotoImage(file=getFilePath("micropython.png"))

    canvas = tkinter.Canvas(root, height=height*0.8, width=width*0.8, bg=Color.PURPLE)
    canvas.create_image(width*0.8/2, height*0.8/2, image=image)
    canvas.pack()

    root.after(1000, root.destroy)
    root.mainloop()
    
    App().main()