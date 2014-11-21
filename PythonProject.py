import random
from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)
    
def keyPressed(event):
    canvas = event.widget.canvas
    #movement
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
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
    
def moveSnake(canvas, drow, dcol):
    # moving the snake by integer on llist board
    canvas.data["snakeDrow"] = drow # store direction for next timer event
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


   
def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0
    snakeBoard = canvas.data["snakeBoard"]
    #setting up the rowas and columns of the board
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    # making the snake appear as moving by making the tail turn into 0 (nonexistent) when it moves, making the next number the tail
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1
                
def gameOver(canvas):
    canvas.data["isGameOver"] = True             
                
def timerFired(canvas):
    if (canvas.data["isGameOver"] == False):
        drow = canvas.data["snakeDrow"]
        dcol = canvas.data["snakeDcol"]
        moveSnake(canvas,drow,dcol)
        redrawAll(canvas)
    delay = 250 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

    # whether or not game is over, call next timerFired
    # (or we'll never call timerFired again!)
def redrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)

def drawSnakeBoard(canvas):
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas, snakeBoard, row, col)

def drawSnakeCell(canvas, snakeBoard, row, col):
    margin = 5
    cellSize = 30
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (snakeBoard[row][col] > 0):
        canvas.create_oval(left, top, right, bottom, fill="blue")
    elif (snakeBoard[row][col] < 0):
        canvas.create_oval(left, top, right, bottom, fill="green")

def loadSnakeBoard(canvas):
    # 2d Integer List Board
    snakeBoard = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
                ]
    canvas.data["snakeBoard"] = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)
    
def placeFood(canvas): 
    # place food (-1) in a random location on the snakeBoard, but
    # keep picking random locations until we find one that is not
    # part of the snake!
    snakeBoard = canvas.data["snakeBoard"]
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0):
            break
    snakeBoard[row][col] = -1 
    
      
def findSnakeHead(canvas):
    #variables dealing with how to find the snake head through finding highest integer and storing as head's row and column
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
    
    
def printInstructions():
    #print the instructions
    print "Snake!"
    print "Use the Arrow Keys to move the snake!"
    print "Eat food to grow!"
    print "Stay on the board..."
    print "And don't crash into yourself :)"
    print "Press "R" to Restart"
    return

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data["isGameOver"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1
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