class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.pickedUp = False
        self.fill = "green"

    def draw(self, app, canvas):
        canvas.create_rectangle(self.x - 75, self.y - 20, self.x +
                                75, self.y + 20, fill=self.fill, outline="black", width=2)


class FunctionBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.name = name
        self.fill = "yellow"
        self.listChildren = ""

    def setName(self, input):
        self.name = input

    def draw(self, app, canvas):
        super().draw(app, canvas)
        # canvas.create_rectangle(self.x - 75, self.y - 20, self.x +
        #                         75, self.y + 20, fill=self.fill, outline="black", width=2)
        canvas.create_text(self.x - 25, self.y, text=self.name,
                           fill="black", font="Times 20")


class VariableBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.name = name
        self.fill = "red"
        self.value = ""
        self.next = ""

    def setVariable(self, value):
        self.value = value

    def setNext(self, nextBlock):
        self.next = nextBlock

    def draw(self, app, canvas):
        super().draw(app, canvas)
        canvas.create_text(self.x - 25, self.y, text=self.name,
                           fill='black', font="Times 20")


class OperationBlock(Block):
    def __init__(self, x, y, operation) -> None:
        super().__init__(x, y)
        self.operation = operation
        self.fill = "Green"


class PrintBlock(Block):
    def __init__(self, x, y, text) -> None:
        super().__init__(x, y)
        self.text = text
        self.fill = "Orange"


class ReturnBlock(Block):
    def __init__(self, x, y, value) -> None:
        super().__init__(x, y)
        self.value = value
        self.fill = "lightblue"


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
