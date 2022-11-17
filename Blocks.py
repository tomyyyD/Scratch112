from guiClasses.TextBox import TextBox


class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.pickedUp = False
        self.fill = "green"
        self.width = 150
        self.textBoxes = []
        self.coords = [[self.x - self.width//2, self.y - 20], [self.x + self.width//2, self.y + 20]]
        self.next = None
        self.parent = None

    def updateCoords(self):
        self.coords = [[self.x - self.width//2, self.y - 20], [self.x + self.width//2, self.y + 20]]

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

class FunctionBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        # self.name = name
        self.fill = "yellow"
        self.nameInput = TextBox(x, y, name, "Function Name")
        self.name = self.nameInput.getText()
        self.width = self.nameInput.width + 100
        self.textBoxes.append(self.nameInput)

    def setName(self, input):
        self.name = input

    def getName(self):
        return self.name

    def draw(self, app, canvas):
        self.width = self.nameInput.width + 100
        super().draw(app, canvas)
        self.nameInput.draw(app, canvas, self.x - 25, self.y)

# variable addignment block
class VariableBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.name = TextBox(x, y, name, "Variable Name")
        self.textBoxes.append(self.name)

        #self.value should be able to be an operation block or a textbox
        self.value = TextBox(x, y, "112", "Variable Value")
        self.textBoxes.append(self.value)
        self.fill = "red"

    def setVariable(self, value):
        self.value = value

    def updateWidth(self):
        self.width = self.name.width + self.value.width + 75

    def draw(self, app, canvas):
        super().draw(app, canvas)
        self.updateWidth()
        self.name.draw(app, canvas, self.x - self.width//2 + self.name.width//2 + 25, self.y)
        self.value.draw(app, canvas, self.x + self.width//2 - self.value.width//2 - 25, self.y)


#variable calling Block
# class VariableCallBlock(block):



class OperationBlock(Block):
    def __init__(self, x, y, operation) -> None:
        super().__init__(x, y)
        self.operation = operation
        self.fill = "Green"

        # self.lhs and self.rhs can be either a variable block or a textBox
        self.lhs = None
        self.rhs = None

    def draw(self, app, canvas):
        super().draw(app, canvas)
        canvas.create_text(self.x, self.y, text=self.operation, fill="black", font="Times 20")

class PrintBlock(Block):
    def __init__(self, x, y, text) -> None:
        super().__init__(x, y)
        self.text = text
        self.fill = "Orange"


class ReturnBlock(Block):
    def __init__(self, x, y, value) -> None:
        super().__init__(x, y)

        #self.value can be a variable block
        self.value = value
        self.fill = "lightblue"

    def draw(self, app, canvas):
        super().draw(app, canvas)
        if isinstance(self.value, VariableBlock):
            self.value.x = self.x + 50
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
