from Blocks import *
from interpreter import Interpreter


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

    def onClick(self, app, spawnX, spawnY) -> None:
        match self.block:
            case 0:
                name = app.getUserInput("Function Name?")
                if name is None:
                    return
                app.blocks.append(FunctionBlock(spawnX, spawnY, name))
            case 1:
                app.blocks.append(ReturnBlock(spawnX, spawnY, "112"))
            case 2:
                name = app.getUserInput("Variable Name?")
                if name is None:
                    return
                app.blocks.append(VariableBlock(spawnX, spawnY, name))
            case 3:
                app.blocks.append(ConditionalBlock(spawnX, spawnY, "", ""))
            case 4:
                # block = PrintBlock(spawnX, spawnY)
                # app.blocks.append(block)
                app.blocks.append(ForLoopBlock(spawnX, spawnY, 0))

            case 5:
                app.blocks.append(PrintBlock(spawnX, spawnY))
            case 6:
                app.blocks.append(AddBlock(spawnX, spawnY))
            case 7:
                app.blocks.append(SubtractBlock(spawnX, spawnY))
            case 8:
                app.blocks.append(MultiplyBlock(spawnX, spawnY))
            case 9:
                app.blocks.append(DivideBlock(spawnX, spawnY))
            case 10:
                name = app.getUserInput("What Variable Are you Calling?")
                if name is None:
                    return
                # can only call a variable if it has been initialized
                for block in app.blocks:
                    if isinstance(block, VariableBlock) and name == block.children[0].getText():
                        app.blocks.append(
                            VariableCallBlock(spawnX, spawnY, block))
                        break
            case 11:
                name = app.getUserInput("What Function are you calling?")
                print("looking for block")
                if name is None:
                    return
                for block in app.blocks:
                    if isinstance(block, FunctionBlock) and name == block.nameInput.getText():
                        print("found block")
                        app.blocks.append(
                            FunctionCallBlock(spawnX, spawnY, block))
                        break
            case 12:
                interpreter = Interpreter(app.blocks)
                try:
                    exec(open('./output.py').read())
                except Exception as e:
                    print(e)
            case 13:
                app.blocks = [OnRun(300, 100)]
