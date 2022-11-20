"""
Please read the README.md
"""

from cmu_112_graphics import *
from guiClasses.Button import Button
from Blocks import *
from interpreter import Interpreter


def appStarted(app):
    app.blocks = []
    app.buttons = []
    createGui(app)
    app.offset = (0, 0)


def createGui(app):
    buttonList = [("Function", "yellow"), ("Return", "lightblue"),
                  ("Variable", "red"), ("Conditional", "pink"),
                  ("For Loop", "violet"), ("Print", "orange"),
                  ("Add", "green"), ("Subtract", "green"),
                  ("Multiply", "green"), ("Divide", "green"),
                  ("Variable Call", "red")]
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


def mousePressed(app, event):
    for block in reversed(app.blocks):
        # moving blocks with cursor
        if mouseOnBlock(block, event.x, event.y):
            editting = False
            for textBox in block.textBoxes:
                if (textBox is not None) and mouseOnRectangle(event.x, event.y, textBox.coords):
                    textBox.setText(app)
                    editting = True
                    return
            for childBlock in block.children:
                if mouseOnRectangle(event.x, event.y, childBlock.coords):
                    childBlock.pickedUp = True
                    return
            if not editting:
                block.pickedUp = True
                app.offset = (block.x - event.x, block.y - event.y)
                # break so we only move one block at a time
            return

    for button in app.buttons:
        if mouseOnRectangle(event.x, event.y, button.coords):
            button.onClick(app)

    if event.x < 150:
        return

    # when run button pressed
    # run interpreter passing in the blocks list


def mouseDragged(app, event):
    for block in app.blocks:
        if block.pickedUp:
            print(block)
            if block.parent is not None:
                block.breakLink()
            elif block.valueParent is not None:
                block.unLinkValueBlock()
            block.x = event.x + app.offset[0]
            block.y = event.y + app.offset[1]


def dropBlock(app, event, block: Block, otherBlock: Block):
    # linking block to values of variable blocks
    # the only blocks that can be made a value block are Variable calls and operations
    if (isinstance(otherBlock, VariableBlock)) and (isinstance(block, OperationBlock) or isinstance(block, VariableCallBlock)):
        # check child of the variable first
        for child in block.children:
            dropBlock(app, event, block, child)
        if len(otherBlock.textBoxes) > 1 and otherBlock.textBoxes[1] and mouseOnRectangle(event.x, event.y, otherBlock.textBoxes[1].coords):
            otherBlock.linkValueBlock(block, 1)
            return
    # linking blocks to sides of Operation block equation
    elif isinstance(otherBlock, OperationBlock) and (isinstance(block, OperationBlock) or isinstance(block, VariableCallBlock)):
        index = 0
        for textbox in otherBlock.textBoxes:
            if textbox and mouseOnRectangle(event.x, event.y, textbox.coords):
                otherBlock.linkValueBlock(block, index)
                print(index)
                return
            index += 1
    # makes otherBlock the parent of block
    # variable call blocks and operation block cannot be stand alone
    # they must be within other blocks
    if not (isinstance(block, VariableCallBlock) or isinstance(block, OperationBlock)):
        otherBlock.linkBlock(block)


def mouseReleased(app, event):
    # Finds the block being moved
    # block is being moved
    for block in app.blocks:
        if block.pickedUp:
            block.pickedUp = False
            if block.x < 150:
                app.blocks.remove(block)
                return
            # links two blocks together
            # other block is the stationary block
            for otherBlock in app.blocks:
                if block != otherBlock and not isinstance(block, FunctionBlock):
                    if mouseOnRectangle(event.x, event.y, otherBlock.coords):
                        # assign variable call block to return statement
                        # return will only return variables
                        if isinstance(otherBlock, ReturnBlock):
                            if isinstance(block, VariableCallBlock):
                                otherBlock.value = block
                                return
                        else:
                            dropBlock(app, event, block, otherBlock)


def keyPressed(app, event):
    if event.key == 'C':
        interpreter = Interpreter(app.blocks)
    if event.key == 'R':
        exec(open('output.py').read())
    if event.key == 'P':
        for block in app.blocks:
            print(block.children)


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
    movingBlock = None
    for block in app.blocks:
        if block.pickedUp:
            movingBlock = block
        block.draw(app, canvas)
    if movingBlock is not None:
        movingBlock.draw(app, canvas)
    # for block in reversed(app.blocks):
    #     canvas.create_rectangle(
    #         block.x - 50, block.y - 20, block.x + 50, block.y + 20, fill=block.fill, outline="black", width=2)


def redrawAll(app, canvas):
    drawBlocks(app, canvas)
    drawGui(app, canvas)


runApp(width=800, height=600)
