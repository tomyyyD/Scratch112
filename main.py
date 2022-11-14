from cmu_112_graphics import *
from Blocks import Block


def appStarted(app):
    app.blocks = []


def mouseOnBlock(block, x, y):
    # basic rectangle collision detection to see if the mouse is in the block
    if block.x - 50 < x < block.x + 50 and block.y - 20 < y < block.y + 20:
        return True
    return False


def mousePressed(app, event):
    dragging = False
    for block in app.blocks:
        if mouseOnBlock(block, event.x, event.y):
            dragging = True
            block.pickedUp = True

    if not dragging:
        block = Block(event.x, event.y)
        app.blocks.append(block)


def mouseDragged(app, event):
    for block in app.blocks:
        if block.pickedUp:
            block.x = event.x
            block.y = event.y


def mouseReleased(app, event):
    for block in app.blocks:
        if block.pickedUp:
            block.pickedUp = False


def keyPressed(app, event):
    pass


def redrawAll(app, canvas):
    for block in app.blocks:
        canvas.create_rectangle(
            block.x - 50, block.y - 20, block.x + 50, block.y + 20, fill=block.fill)


runApp(width=600, height=400)
