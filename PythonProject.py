#Python 

from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)
    
def keyPressed(event):
    canvas = event.widget.canvas
    #movement
    if (event.keysym == "Up"):
        moveSnake(canvas,-1,0)
    elif (event.keysym == "Down"):
        moveSnake(canvas, 1, 0)
    elif (event.keysym == "Left"):
        moveSnake(canvas, 0, -1)
    elif (event.keysym == "Right"):
        moveSnake(canvas, 0, 1)
    redrawAll(canvas)

def moveSnake(canvas, drow, dcol):
    # moving the snake by integer on llist board
    
    snakeBoard = canvas.data["snakeBoard"]
    #recent head position
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    #variables to help with the next steps... placing the new head of the snake
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    #giving head a new integer to represent it
    snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
    canvas.data["headRow"] = newHeadRow
    canvas.data["headCol"] = newHeadCol
    #calling removeTail to make the snake seem as if moving by adding a head, and subrtacting a tail
    removeTail(canvas)
    
def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    
    #of snakeboard in canvas data
    snakeBoard = canvas.data["snakeBoard"]
    #setting up the rowas and columns of the board
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    # making the snake appear as moving by making the tail turn into 0 (nonexistent) when it moves, making the next number the tail
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1
                
                
                
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
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)

def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = 5
    cellSize = 30
    # you write this!
    # hint: place a margin 5-pixels-wide around the board.
    # make each cell 30x30
    # draw a white square and then, if the snake is in the
    # cell, draw a blue circle.
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        # drawing part of the snake body
        canvas.create_oval(left, top, right, bottom, fill="blue")
    return

def loadSnakeBoard(canvas):
    # 2d Integer List Board
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
    findSnakeHead(canvas)
    return
    
    
def findSnakeHead(canvas):
    #variables dealing with how to find the snake head through finding highest integer and storing as head's row and column
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data["headRow"] = headRow
    canvas.data["headCol"] = headCol
    
    
def printInstructions():
    #print the instructions
    print "Snake!"
    print "Use the Arrow Keys to move the snake!"
    print "Eat food to grow!"
    print "Stay on the board..."
    print "And don't crash into yourself :)"
    return

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    redrawAll(canvas)

def run():
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