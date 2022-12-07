from guiClasses.TextBox import TextBox


class Block:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.pickedUp = False
        self.fill = "green"
        self.font = "times 20"
        self.width = 150
        self.totalHeight = 40
        self.height = 20
        self.textBoxes = []
        self.coords = [[self.x - self.width//2, self.y - 20],
                       [self.x + self.width//2, self.y + self.height]]
        self.placeCoords = [[self.x - self.width//2, self.y - 20],
                            [self.x + self.width//2, self.y + 20]]
        self.next = None
        self.parent = None
        self.valueParent = None
        self.children = []
        self.parentPosition = None

    def updateCoords(self):
        self.totalHeight = 20 + self.height
        self.coords = [[self.x - self.width//2, self.y - 20],
                       [self.x + self.width//2, self.y + self.height]]
        self.placeCoords = [[self.x - self.width//2, self.y - 20],
                            [self.x + self.width//2, self.y + 20]]

    def draw(self, app, canvas):
        self.updateCoords()
        canvas.create_rectangle(self.coords[0][0], self.coords[0][1], self.coords[1][0],
                                self.coords[1][1], fill=self.fill, outline="black", width=2)
        if self.next is not None:
            self.next.y = self.y + 20 + self.height
            self.next.x = self.x - (self.width - self.next.width)//2
            self.next.draw(app, canvas)

    def breakLink(self):
        self.parent.next = None
        self.parent = None

    def linkBlock(self, block):
        if self.next:
            self.next.x += 50
            self.next.y += 50
            self.next.parent = None
        self.next = block
        self.next.parent = self

    def unLinkValueBlock(self):
        self.valueParent.resetTextBox(self.parentPosition)
        self.valueParent = None

    def linkValueBlock(self, block, pos):
        block.valueParent = self
        # self.textBoxes.pop(pos)
        self.children[pos] = block
        self.textBoxes[pos] = None
        block.parentPosition = pos

    def resetTextBox(self, pos):
        self.children[pos] = TextBox(self.x, self.y, "112", "Enter Value")
        self.textBoxes[pos] = self.children[pos]

    def updateWidth(self):
        width = 75
        for child in self.children:
            if isinstance(child, Block) or isinstance(child, TextBox):
                width += child.width
        self.width = width


class OnRun(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.fill = "yellow"
        self.width = 200

    def draw(self, app, canvas):
        super().draw(app, canvas)
        canvas.create_rectangle(self.x - self.width//2 + 10, self.y -
                                self.height, self.x, self.y + self.height, fill="green", width=0)
        canvas.create_text(self.x - self.width//2 + 52, self.y,
                           text="On Run", fill="black", font=self.font)


class FunctionBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        # self.name = name
        self.fill = "yellow"
        self.nameInput = TextBox(x, y, name, "Function Name")
        self.width = self.nameInput.width + 100
        self.textBoxes.append(self.nameInput)
        self.args = []

    def getName(self):
        return self.nameInput.getText()

    def draw(self, app, canvas):
        self.width = self.nameInput.width + 100
        super().draw(app, canvas)
        self.nameInput.draw(app, canvas, self.x - 25, self.y)
        index = 0
        for arg in self.args:
            arg.draw(self.x + self.nameInput.width +
                     index * self.width + 15, self.y)

# variable addignment block


class FunctionCallBlock(Block):
    def __init__(self, x, y, block) -> None:
        super().__init__(x, y)
        self.link = block
        self.name = self.link.textBoxes[0].getText()

        # self.value should be able to be an operation block or a textbox
        self.fill = "yellow"

        self.width = len(self.link.nameInput.getText()) * 5 + 50

    def draw(self, app, canvas):
        self.name = self.link.nameInput.getText()
        super().draw(app, canvas)
        canvas.create_text(self.x, self.y, text=self.name,
                           font="Times 20", fill="black")

    def getText(self):
        return self.name


class VariableBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.children = [TextBox(x, y, name, "Variable Name"), TextBox(
            x, y, "112", "Variable Value")]
        self.textBoxes = [self.children[0], self.children[1]]

        # self.value should be able to be an operation block or a textbox
        self.fill = "red"
        # self.children.extend([self.name, self.value])

    # def updateWidth(self):
    #     self.width = self.children[0].width + self.children[1].width + 75

    def draw(self, app, canvas):
        # name is children[0]
        # value is children[1]
        super().draw(app, canvas)
        self.updateWidth()
        canvas.create_text(self.x - self.width//2 +
                           self.children[0].width + 37, self.y, text="=", font="Times 20", fill="black")
        self.children[0].draw(app, canvas, self.x - self.width //
                              2 + self.children[0].width//2 + 25, self.y)
        if isinstance(self.children[1], Block):
            self.children[1].x = self.x + self.width//2 - \
                self.children[1].width//2 - 25
            self.children[1].y = self.y
            self.children[1].draw(app, canvas)
        else:
            self.children[1].draw(
                app, canvas, self.x + self.width//2 - self.children[1].width//2 - 25, self.y)

# variable calling Block


class VariableCallBlock(Block):
    def __init__(self, x, y, block) -> None:
        super().__init__(x, y)
        self.link = block
        self.name = self.link.children[0].getText()

        # self.value should be able to be an operation block or a textbox
        self.fill = "red"

        self.width = self.link.children[0].width + 50

    def draw(self, app, canvas):
        self.name = self.link.children[0].getText()
        super().draw(app, canvas)
        canvas.create_text(self.x, self.y, text=self.name,
                           font="Times 20", fill="black")

    def getText(self):
        return self.name


class OperationBlock(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.fill = "Green"
        # self.lhs and self.rhs can be either a variable block or a textBox
        self.lhs = TextBox(x, y, '112', "Right Hand Side")
        self.rhs = TextBox(x, y, '112', "Left Hand Side")
        self.textBoxes = [self.lhs, self.rhs]
        self.children = [self.lhs, self.rhs]

    def updateWidth(self):
        self.width = self.children[0].width + self.children[1].width + 75

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        canvas.create_text(self.x - self.width//2 +
                           self.children[0].width + 37, self.y, text=self.operation, font="Times 20", fill="black")
        if isinstance(self.children[0], TextBox):
            self.children[0].draw(
                app, canvas, self.x - self.width//2 + self.children[0].width//2 + 25, self.y)
        else:
            self.children[0].x = self.x - self.width//2 + \
                self.children[0].width//2 + 25
            self.children[0].y = self.y
            self.children[0].draw(app, canvas)
        if isinstance(self.children[1], TextBox):
            self.children[1].draw(
                app, canvas, self.x + self.width//2 - self.children[1].width//2 - 25, self.y)
        else:
            self.children[1].x = self.x + self.width//2 - \
                self.children[1].width//2 - 25
            self.children[1].y = self.y
            self.children[1].draw(app, canvas)


class AddBlock(OperationBlock):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.operation = "+"


class SubtractBlock(OperationBlock):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.operation = "-"


class MultiplyBlock(OperationBlock):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.operation = "*"


class DivideBlock(OperationBlock):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.operation = "/"


class PrintBlock(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.textInput = TextBox(x, y, "112", "Print Value")
        self.textBoxes = [self.textInput]
        self.fill = "Orange"
        self.children = [self.textInput]

    def updateWidth(self):
        self.width = self.children[0].width + 75

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        if isinstance(self.children[0], TextBox):
            self.children[0].draw(app, canvas, self.x, self.y)
        else:
            self.children[0].x = self.x
            self.children[0].y = self.y
            self.children[0].draw(app, canvas)


class ReturnBlock(Block):
    def __init__(self, x, y, value) -> None:
        super().__init__(x, y)
        # self.value can be a variable block
        self.textInput = TextBox(x, y, value, "Print Value")
        self.textBoxes = [self.textInput]
        self.children = [self.textInput]
        self.value = value
        self.fill = "lightblue"

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        canvas.create_text(self.x - self.width//2 + 35, self.y,
                           text="Return", font=self.font, fill="black")
        if isinstance(self.children[0], TextBox):
            self.children[0].draw(app, canvas, self.x +
                                  self.children[0].width//2, self.y)
        else:
            self.children[0].x = self.x + self.width//2 - \
                self.children[0].width//2 - 10
            self.children[0].y = self.y
            self.children[0].draw(app, canvas)


class ConditionalBlock(Block):
    def __init__(self, x, y, leftHandSide, rightHandSide) -> None:
        super().__init__(x, y)
        self.lhs = TextBox(x, y, 112, "Left Hand Side")
        self.rhs = TextBox(x, y, 112, "Right Hand Side")
        self.fill = "pink"
        self.placeholder = TextBox(x, y, "Place blocks", "Blocks")
        self.comparison = TextBox(x, y, "==", "==, <, >, <=, >= only")
        self.textBoxes = [self.lhs, self.rhs,
                          self.comparison, self.placeholder]
        self.children = [self.lhs, self.rhs, self.comparison, self.placeholder]

    def updateWidth(self):
        self.width = self.children[1].width + \
            self.children[0].width + self.children[2].width + 75

    def updateHeight(self):
        value = self.children[3]
        if isinstance(value, TextBox):
            self.height = 60
            return
        sum = 0
        while value:
            sum += value.totalHeight
            value = value.next
        self.height = 20 + sum

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        self.updateHeight()
        if isinstance(self.children[0], TextBox):
            self.children[0].draw(
                app, canvas, self.x - self.width//2 + self.children[0].width//2 + 10, self.y)
        else:
            self.children[0].x = self.x - self.width//2 + \
                self.children[0].width//2 + 10
            self.children[0].y = self.y
            self.children[0].draw(app, canvas)
        if isinstance(self.children[1], TextBox):
            self.children[1].draw(
                app, canvas, self.x + self.width//2 - self.children[1].width//2 - 10, self.y)
        else:
            self.children[1].x = self.x + self.width//2 - \
                self.children[1].width//2 - 10
            self.children[1].y = self.y
            self.children[1].draw(app, canvas)
        self.children[2].draw(app, canvas, self.x -
                              self.width//2 + self.children[0].width + 47, self.y)
        if isinstance(self.children[3], TextBox):
            self.children[3].draw(
                app, canvas, self.x - self.width//2 + self.children[3].width//2 + 10, self.y + 40)
        else:
            self.children[3].x = self.x - \
                self.width//2 + self.children[3].width//2 + 20
            self.children[3].y = self.y + 40
            self.children[3].draw(app, canvas)


class ForLoopBlock(Block):
    def __init__(self, x, y, range) -> None:
        super().__init__(x, y)
        self.range = range
        self.fill = "violet"
        self.loops = TextBox(x, y, 12, "Loops")
        self.placeholder = TextBox(x, y, "Place blocks", "Blocks")
        self.textBoxes = [self.loops, self.placeholder]
        self.children = [self.loops, self.placeholder]

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        self.updateHeight()
        canvas.create_text(self.x - self.width//2 + 30,
                           self.y, text="Loop", fill="black", font=self.font)
        canvas.create_text(self.x + self.width//2 - 30,
                           self.y, text="Times", fill="black", font=self.font)
        if isinstance(self.children[0], TextBox):
            self.children[0].draw(app, canvas, self.x, self.y)
        else:
            self.children[0].x = self.x
            self.children[0].y = self.y
            self.children[0].draw(app, canvas)
        if isinstance(self.children[1], TextBox):
            self.children[1].draw(
                app, canvas, self.x - self.width//2 + self.children[1].width//2 + 20, self.y + 40)
        else:
            self.children[1].x = self.x - \
                self.width//2 + self.children[1].width//2 + 20
            self.children[1].y = self.y + 40
            self.children[1].draw(app, canvas)

    def updateHeight(self):
        value = self.children[1]
        if isinstance(value, TextBox):
            self.height = 60
            return
        sum = 0
        while value:
            sum += value.totalHeight
            value = value.next
        self.height = 20 + sum


class functionCallblock(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
