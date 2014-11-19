# Section 1 

from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def timerFired(canvas):
    redrawAll(canvas)
    delay = 250 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)

def drawSnakeBoard(canvas):
    # you write this!
    # hint: for every row,col position on the board, call
    # drawSnakeCell, a helper method you will also write, like so
    #    drawSnakeCell(canvas, snakeBoard, row, col)
    return

def drawSnakeCell(canvas, snakeBoard, row, col):
    # you write this!
    # hint: place a margin 5-pixels-wide around the board.
    # make each cell 30x30
    # draw a white square and then, if the snake is in the
    # cell, draw a blue circle.
    margin = 5
    cellSize = 30
    return

def loadSnakeBoard(canvas):
    # you write this!
    snakeBoard = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 4, 5, 6, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 3, 0, 7, 0, 0, 0 ],
                   [ 0, 0, 0, 1, 2, 0, 8, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 9, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
                ]
    canvas.data["snakeBoard"] = snakeBoard
    # allocate the new snakeBoard 2d list as described
    # in the notes, and store it in the canvas's data
    # dictionary
    return

def printInstructions():
    # you write this!
    # print the instructions
    return

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=310, height=310)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()