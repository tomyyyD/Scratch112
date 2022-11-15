from cmu_112_graphics import *
from guiClasses import Button


def appStarted(app):
    app.blocks = []
    app.buttons = []
    createGui(app)


def createGui(app):
    functionButton = Button("Function", "yellow", 10, 45, 140, 75, 0)
    app.buttons.append(functionButton)
    returnButton = Button("Return", "lightblue", 10, 85, 140, 115, 1)
    app.buttons.append(returnButton)
    variableButton = Button("Variable", "red", 10, 125, 140, 155, 2)
    app.buttons.append(variableButton)
    operationButton = Button("Operation", "Green", 10, 165, 140, 195, 3)
    app.buttons.append(operationButton)
    conditionalBlock = Button("Conditional", "pink", 10, 205, 140, 235, 4)
    app.buttons.append(conditionalBlock)
    forLoopBlock = Button("For Loop", "violet", 10, 245, 140, 275, 5)
    app.buttons.append(forLoopBlock)
    printBlock = Button("Print", "orange", 10, 285, 140, 315, 6)
    app.buttons.append(printBlock)


def mouseOnBlock(block, x, y):
    # basic rectangle collision detection to see if the mouse is in the block
    if block.x - 50 < x < block.x + 50 and block.y - 20 < y < block.y + 20:
        return True
    return False


def mouseOnRectangle(mx, my, rectangle):
    if rectangle[0][0] < mx < rectangle[1][0] and rectangle[0][1] < my < rectangle[1][1]:
        return True
    return False


def onCreateArrow(block, mx, my):
    pass


def mousePressed(app, event):
    dragging = False
    for block in reversed(app.blocks):
        if mouseOnBlock(block, event.x, event.y):
            if onCreateArrow(block, event.x, event.y):
                pass
            dragging = True
            block.pickedUp = True
            break

    for button in app.buttons:
        if mouseOnRectangle(event.x, event.y, button.coords):
            button.onClick(app, event)

    if event.x < 150:
        return


def mouseDragged(app, event):
    for block in app.blocks:
        if block.pickedUp:
            block.x = event.x
            block.y = event.y


def mouseReleased(app, event):
    for block in app.blocks:
        if block.pickedUp:
            block.pickedUp = False
            if block.x < 150:
                app.blocks.remove(block)


def keyPressed(app, event):
    # if event.key == "w":
    #     stuff = app.getUserInput("function name")
    #     app.blocks[0].setName(stuff)
    pass


def drawGui(app, canvas):
    # draws the blocks tab
    canvas.create_line(150, 0, 150, 600, fill="black", width=5)
    canvas.create_rectangle(0, 0, 150, 600, fill="white",
                            outline="black", width=5)
    canvas.create_text(75, 20, fill="black",
                       text="Blocks", font="Times 30 bold")

    for button in app.buttons:
        button.draw(app, canvas)


def drawBlocks(app, canvas):
    for block in app.blocks:
        block.draw(app, canvas)
    # for block in reversed(app.blocks):
    #     canvas.create_rectangle(
    #         block.x - 50, block.y - 20, block.x + 50, block.y + 20, fill=block.fill, outline="black", width=2)


def redrawAll(app, canvas):
    drawBlocks(app, canvas)
    drawGui(app, canvas)


runApp(width=800, height=600)
