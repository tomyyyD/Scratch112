from Blocks import *

class Interpreter:
    def __init__(self, blocksList):
        self.file = open("output.py", 'w')
        self.functionBlocks = []
        for block in blocksList:
            if isinstance(block, FunctionBlock):
                self.functionBlocks.append(block)
        for functionBlock in self.functionBlocks:
            self.outputToFile(functionBlock)
        self.generateMainFunc()

    def outputToFile(self, block):
        if isinstance(block, FunctionBlock):
            string = f"def {block.name}():\n"
            self.file.write(string)
            self.outputToFile(block.next)
        if isinstance(block, VariableBlock):
            if isinstance(block.value, OperationBlock):
                string = f"\t{block.name.getText()} = {self.buildOperationString(block.value)}\n"
            else:
                string = f"\t{block.name.getText()} = {block.value.getText()}\n"
            self.file.write(string)
            self.outputToFile(block.next)
        if isinstance(block, ReturnBlock):
            string = f"\treturn {block.value.name}\n"
            self.file.write(string)

    def buildOperationString(self, block):
        if isinstance(block.lhs, TextBox) and isinstance(block.rhs, TextBox):
            return f"{block.lhs.getText()} {block.operation} {block.rhs.getText()}"
        elif isinstance(block.lhs, TextBox):
            return f"{self.buildVariableString(block.lhs)} {block.operation} {block.rhs.getText()}"
        elif isinstance(block.rhs, TextBox):
            return f"{block.rhs.getText()} {block.operation} {self.buildVariableString(block.rhb)}"
        else:
            return f"{self.buildOperationString(block.lhs)} {block.operation} {self.buildOperationString(block.rhs)}"

    def generateMainFunc(self):
        string = '\n\nif __name__ == "__main__":\n'
        for functionBlock in self.functionBlocks:
            string += f"\t{functionBlock.getName()}()\n"
        self.file.write(string)
        self.file.close()


