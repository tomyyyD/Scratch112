class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.pickedUp = False
        self.fill = "green"


class FunctionBlock(Block):
    def __init__(self, x, y, name) -> None:
        super().__init__(x, y)
        self.name = name
        self.fill = "orange"


class OperationBlock(Block):
    def __init__(self, x, y, operation) -> None:
        super().__init__(x, y)
        self.operation = operation
        self.fill = "lightblue"
