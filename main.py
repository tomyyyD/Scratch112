from cmu_112_graphics import *
from guiClasses.Button import Button


def appStarted(app):
    app.blocks = []
    app.buttons = []
    createGui(app)


def createGui(app):
    buttonList = [("Function", "yellow"), ("Return", "lightblue"),
                  ("Variable", "red"), ("Operation", "green"),
                  ("Conditional", "pink"), ("For Loop", "violet"),
                  ("Print", "orange")]
    startX = 45
    index = 0
    for button in buttonList:
        button = Button(button[0], button[1], 10, startX +
                        40 * index, 140, startX + 30 + 40 * index, index)
        app.buttons.append(button)
        index += 1


def mouseOnBlock(block, x, y):
    # basic rectangle collision detection to see if the mouse is in the block
    if block.x - block.width//2 < x < block.x + block.width//2 and block.y - 20 < y < block.y + 20:
        return True
    return False


def mouseOnRectangle(mx, my, rectangle):
    if rectangle[0][0] < mx < rectangle[1][0] and rectangle[0][1] < my < rectangle[1][1]:
        return True
    return False


def onCreateArrow(block, mx, my):
    pass


def mousePressed(app, event):
    for block in reversed(app.blocks):
        # moving blocks with cursor
        if mouseOnBlock(block, event.x, event.y):
            editting = False
            # linking blocks together
            if onCreateArrow(block, event.x, event.y):
                pass
            for textBox in block.textBoxes:
                if mouseOnRectangle(event.x, event.y, textBox.coords):
                    print("hitting textbox")
                    textBox.setText(app)
                    editting = True
                    break
            if not editting:
                block.pickedUp = True
                # break so we only move one block at a time
            break

    for button in app.buttons:
        if mouseOnRectangle(event.x, event.y, button.coords):
            button.onClick(app)

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
