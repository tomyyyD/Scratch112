from Blocks import *


class Button:
    def __init__(self, text, color, x1, y1, x2, y2, block) -> None:
        self.text = text
        self.color = color
        self.coords = [[x1, y1], [x2, y2]]
        self.block = block

    def draw(self, app, canvas) -> None:
        canvas.create_rectangle(
            self.coords[0], self.coords[1], fill=self.color, outline="black", width=2)
        midX = (self.coords[0][0] + self.coords[1][0])//2
        midY = (self.coords[0][1] + self.coords[1][1])//2
        canvas.create_text(midX, midY, text=self.text,
                           fill="black", font="Times 20")

    def onClick(self, app) -> None:
        match self.block:
            case 0:
                name = app.getUserInput("Function Name?")
                if name is None:
                    return
                app.blocks.append(FunctionBlock(250, 100, name))
            case 1:
                app.blocks.append(ReturnBlock(250, 100, ""))
            case 2:
                name = app.getUserInput("Variable Name?")
                if name is None:
                    return
                app.blocks.append(VariableBlock(250, 100, name))
            case 3:
                app.blocks.append(ConditionalBlock(250, 100, "", ""))
            case 4:
                app.blocks.append(ForLoopBlock(250, 100, 0))
            case 5:
                app.blocks.append(PrintBlock(250, 100, ""))
            case 6:
                app.blocks.append(AddBlock(250, 100))
            case 7:
                app.blocks.append(SubtractBlock(250, 100))
            case 8:
                app.blocks.append(MultiplyBlock(250, 100))
            case 9:
                app.blocks.append(DivideBlock(250, 100))
            case 10:
                name = app.getUserInput("What Variable Are you Calling?")
                if name is None:
                    return 
                app.blocks.append(VariableCallBlock(250, 100, name))
