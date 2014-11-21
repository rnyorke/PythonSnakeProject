import random
from Tkinter import *
#this function makes button register as an event
def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)
# defines the pressing of certain keys to move the snake, quit the game, restart, and debug    
def keyPressed(event):
    canvas = event.widget.canvas
    canvas.data["ignoreNextTimerEvent"] = True
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data["inDebugMode"] = not canvas.data["inDebugMode"]
    if (canvas.data["isGameOver"] == False):
        if (event.keysym == "Up"):
            moveSnake(canvas,-1,0)
        elif (event.keysym == "Down"):
            moveSnake(canvas, 1, 0)
        elif (event.keysym == "Left"):
            moveSnake(canvas, 0, -1)
        elif (event.keysym == "Right"):
            moveSnake(canvas, 0, 1)
    redrawAll(canvas)
 # this function moves the snake through the positions of rows and columns and ends the game if it runs into itself, runs outside the borders, and makes the snake seem to move   
def moveSnake(canvas, drow, dcol):
    canvas.data["snakeDrow"] = drow
    canvas.data["snakeDcol"] = dcol
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = canvas.data["headRow"]
    headCol = canvas.data["headCol"]
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    if ((newHeadRow < 0) or (newHeadRow >= rows) or
        (newHeadCol < 0) or (newHeadCol >= cols)):
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] > 0):
        gameOver(canvas)
    elif (snakeBoard[newHeadRow][newHeadCol] < 0):
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        placeFood(canvas)
    else:
        snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
        canvas.data["headRow"] = newHeadRow
        canvas.data["headCol"] = newHeadCol
        removeTail(canvas)
# this function basically removes the tail so that the snake appears to move
def removeTail(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1
# this function ends the game
def gameOver(canvas):
    canvas.data["isGameOver"] = True             
# this function has the snake move with a timer so that the snake is controlled by turns rather than movng forward whichever way                
def timerFired(canvas):
    if (canvas.data["isGameOver"] == False):
        drow = canvas.data["snakeDrow"]
        dcol = canvas.data["snakeDcol"]
        moveSnake(canvas,drow,dcol)
        redrawAll(canvas)
    delay = 150
    canvas.after(delay, timerFired, canvas)
# draws the animation each time to redraw everything to look nice and tells the player game over once its over
def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    if (canvas.data["isGameOver"] == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]/2
        canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))
# this function sets up for the snakeBoard     
def drawSnakeBoard(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)
#this function has all the necessities to create the snake cell each time 
def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        canvas.create_oval(left, top, right, bottom, fill="blue")
    elif (snakeBoard[row][col] < 0):
        canvas.create_oval(left, top, right, bottom, fill="green")
    if (canvas.data["inDebugMode"] == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=str(snakeBoard[row][col]),font=("Helvatica", 14, "bold"))
# this makes the background beautiful :P                   
def loadSnakeBoard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    snakeBoard = [ ]
    for row in range(rows): snakeBoard += [[0] * cols]
    snakeBoard[rows/2][cols/2] = 1 
    canvas.data["snakeBoard"] = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)
# this function places 'food' for the snake to eat randomly on the screen
def placeFood(canvas): 
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1 
# this function is used to locate where the snake head is 
def findSnakeHead(canvas):
    snakeBoard = canvas.data["snakeBoard"]
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
# this obviously prints the instructions... 
def printInstructions():
    print "Snake!"
    print "Use the Arrow Keys to move the snake!"
    print "Eat food to grow!"
    print "Stay on the board..."
    print "And don't crash into yourself :)"
    print "Press 'r' to Restart"
    print "Press 'd' for debug mode."
# this makes the animation and everything start
def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1
    canvas.data["ignoreNextTimerEvent"] = False
    redrawAll(canvas)
# contains valuble stuffs and starts the game :P  
def run(rows, cols):
    root = Tk()
    margin = 5
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width = 0, height = 0)
    root.canvas = canvas.canvas = canvas
    canvas.data = { }
    canvas.data["margin"] = margin
    canvas.data["cellSize"] = cellSize
    canvas.data["canvasWidth"] = canvasWidth
    canvas.data["canvasHeight"] = canvasHeight
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    init(canvas)
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    root.mainloop()
# this basically sets the dimensions and of course starts the game
run(16,24)