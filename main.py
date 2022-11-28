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


def checkBlock(app, event, block: Block):
    if mouseOnRectangle(event.x, event.y, block.coords):
        editting = False
        for textBox in block.textBoxes:
            if (textBox is not None) and mouseOnRectangle(event.x, event.y, textBox.coords):
                textBox.setText(app)
                editting = True
                return True
        for childBlock in block.children:
            if checkBlock(app, event, childBlock):
                return True
            # if mouseOnRectangle(event.x, event.y, childBlock.coords):
            #     childBlock.pickedUp = True
            #     return
        if not editting:
            block.pickedUp = True
            app.offset = (block.x - event.x, block.y - event.y)
        return True
    return False


def mousePressed(app, event):
    x = 250
    y = 100
    for block in reversed(app.blocks):
        if checkBlock(app, event, block):
            return
    for button in app.buttons:
        if mouseOnRectangle(event.x, event.y, button.coords):
            for otherBlock in app.blocks:
                if block.x == x and block.y == y:
                    x += 10
                    y += 10
            button.onClick(app, x, y)

    if event.x < 150:
        return

    # when run button pressed
    # run interpreter passing in the blocks list


def mouseDragged(app, event):
    for block in app.blocks:
        if block.pickedUp:
            if block.parent is not None:
                block.breakLink()
            elif block.valueParent is not None:
                block.unLinkValueBlock()
            block.x = event.x + app.offset[0]
            block.y = event.y + app.offset[1]


def dropBlock(app, event, block: Block, otherBlock: Block):
    if isinstance(otherBlock, ForLoopBlock) and otherBlock.textBoxes[1]:
        if mouseOnRectangle(event.x, event.y, otherBlock.textBoxes[1].coords):
            otherBlock.linkValueBlock(block, 1)
            return
        if mouseOnRectangle(event.x, event.y, otherBlock.children[1]):
            otherBlock.linkBlock(block)
    # makes otherBlock the parent of block
    # variable call blocks and operation block cannot be stand alone
    # they must be within other blocks
    if not (isinstance(block, VariableCallBlock) or isinstance(block, OperationBlock)):
        otherBlock.linkBlock(block)
    # linking block to values of variable blocks
    # the only blocks that can be made a value block are Variable calls and operations
    elif (isinstance(otherBlock, VariableBlock)):
        # check child of the variable first
        for child in otherBlock.children:
            dropBlock(app, event, block, child)
        if len(otherBlock.textBoxes) > 1 and otherBlock.textBoxes[1] and mouseOnRectangle(event.x, event.y, otherBlock.textBoxes[1].coords):
            otherBlock.linkValueBlock(block, 1)
            return
    # linking blocks to sides of Operation block equation
    elif isinstance(otherBlock, OperationBlock):
        # Using recursion to make sure you always check the child blocks first
        for child in otherBlock.children:
            dropBlock(app, event, block, child)
        index = 0
        for textbox in otherBlock.textBoxes:
            if textbox and mouseOnRectangle(event.x, event.y, textbox.coords):
                otherBlock.linkValueBlock(block, index)
                return
            index += 1
    elif isinstance(otherBlock, PrintBlock):
        if not isinstance(otherBlock.children[0], TextBox):
            dropBlock(app, event, block, otherBlock.children[1])
        if mouseOnRectangle(event.x, event.y, otherBlock.textBoxes[0].coords):
            print("linking")
            otherBlock.linkValueBlock(block, 0)
            return
    elif isinstance(otherBlock, ForLoopBlock):
        if mouseOnRectangle(event.x, event.y, otherBlock.textBoxes[0].coords):
            otherBlock.linkValueBlock(block, 0)


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
        print("-----------------------")


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
        if block.parent:
            continue
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
