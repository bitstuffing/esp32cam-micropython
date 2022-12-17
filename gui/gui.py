from PIL import Image
from pathlib import Path
import threading
import tkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


WINDOW_WIDTH = 930
WINDOW_HEIGHT = 506
BACKGROUND_COLOR = "#123456"
TITLE_SIZE = 24
SUBTITLE_SIZE = 18
NORMAL_TEXT_SIZE = 14
SUBSCREEN_WIDTH = 675
SUBSCREEN_HEIGHT = 410


def getFilePath(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def alignRight(totalWidth: int, textSize: int, charSize: int) -> int:
    calculated = totalWidth-(textSize*charSize)
    return calculated

def findXCenter(canvas, item, windowWidth):
    coords = canvas.bbox(item) #TODO, check if better with coords()
    xOffset = (windowWidth / 2) - ((coords[2] - coords[0]) / 2)
    return xOffset

def drawCenteredCanvasText(canvas,text,line,size,totalWidth):
    textCanvasId = canvas.create_text(0,0,
        anchor=tkinter.NW,
        text=text,
        fill=Color.BLACK,
        font=("Montserrat Bold", size)
    )
    moveCanvasToCenter(canvas,textCanvasId,totalWidth,line)
    
def moveCanvasToCenter(canvas,textCanvasId,totalWidth,line):
    xOffset = findXCenter(canvas, textCanvasId, totalWidth)
    canvas.move(textCanvasId, xOffset, line)

class Color():
    BLACK = "#000000"
    WHITE = "#FFFFFF"
    PURPLE = "#C67FFC"