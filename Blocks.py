from guiClasses.TextBox import TextBox


class Block:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.pickedUp = False
        self.fill = "green"
        self.width = 150
        self.height = 20
        self.textBoxes = []
        self.coords = [[self.x - self.width//2, self.y - self.height],
                       [self.x + self.width//2, self.y + self.height]]
        self.next = None
        self.parent = None
        self.valueParent = None
        self.children = []
        self.parentPosition = None

    def updateCoords(self):
        self.coords = [[self.x - self.width//2, self.y - self.height],
                       [self.x + self.width//2, self.y + self.height]]

    def draw(self, app, canvas):
        self.updateCoords()
        canvas.create_rectangle(self.coords[0][0], self.coords[0][1], self.coords[1][0],
                                self.coords[1][1], fill=self.fill, outline="black", width=2)
        if self.next is not None:
            self.next.y = self.y + 40
            self.next.x = self.x - (self.width - self.next.width)//2
            self.next.draw(app, canvas)

    def breakLink(self):
        self.parent.next = None
        self.parent = None

    def linkBlock(self, block):
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


class VariableBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.children = [TextBox(x, y, name, "Variable Name"), TextBox(
            x, y, "112", "Variable Value")]
        self.textBoxes = [self.children[0], self.children[1]]

        # self.value should be able to be an operation block or a textbox
        self.fill = "red"
        # self.children.extend([self.name, self.value])

    def updateWidth(self):
        self.width = self.children[0].width + self.children[1].width + 75

    def draw(self, app, canvas):
        # name is children[0]
        # value is children[1]
        super().draw(app, canvas)
        self.updateWidth()
        canvas.create_text(self.x - self.width//2 +
                           self.children[0].width + 37, self.y, text="=", font="Times 20", fill="black")
        self.children[0].draw(app, canvas, self.x - self.width //
                              2 + self.children[0].width//2 + 25, self.y)
        if isinstance(self.children[1], OperationBlock):
            self.children[1].x = self.x + self.width//2 - \
                self.children[1].width//2 - 25
            self.children[1].y = self.y
            self.children[1].draw(app, canvas)
        else:
            self.children[1].draw(
                app, canvas, self.x + self.width//2 - self.children[1].width//2 - 25, self.y)

# variable calling Block


class VariableCallBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.name = name

        # self.value should be able to be an operation block or a textbox
        self.fill = "red"

        self.width = len(self.fill) * 5 + 50

    def draw(self, app, canvas):
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

        self.value = value
        self.fill = "lightblue"

    def draw(self, app, canvas):
        super().draw(app, canvas)
        canvas.create_text(self.x, self.y, text="return")
        if isinstance(self.value, VariableCallBlock):
            self.value.x = self.x + self.value.width//2
            self.value.y = self.y
            self.value.draw(app, canvas)
        else:
            canvas.create_text(self.x, self.y, text=self.value)


class ConditionalBlock(Block):
    def __init__(self, x, y, leftHandSide, rightHandSide) -> None:
        super().__init__(x, y)
        self.lhs = leftHandSide
        self.rhs = rightHandSide
        self.fill = "pink"


class ForLoopBlock(Block):
    def __init__(self, x, y, range) -> None:
        super().__init__(x, y)
        self.range = range
        self.fill = "violet"
        self.loops = TextBox(x, y, 12, "Loops")
        self.textBoxes = [self.loops]
        self.value = PrintBlock(x, y)
        self.children = [self.loops, self.value]

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.loops.draw(app, canvas, self.x, self.y)
        self.value.x = self.x + self.width - 25
        self.value.y = self.y + 20
        self.value.draw(app, canvas)
