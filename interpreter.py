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
            string = f"def {block.nameInput.getText()}():\n"
            self.file.write(string)
            self.outputToFile(block.next)
        if isinstance(block, VariableBlock):
            if isinstance(block.children[1], OperationBlock):
                string = f"\t{block.children[0].getText()} = {self.buildOperationString(block.children[1])}\n"
            else:
                string = f"\t{block.children[0].getText()} = {block.children[1].getText()}\n"
            self.file.write(string)
            self.outputToFile(block.next)
        if isinstance(block, ReturnBlock):
            string = f"\treturn {block.value.name}\n"
            self.file.write(string)
        if isinstance(block, PrintBlock):
            string = f"print({block.children.getText()})"

    def buildOperationString(self, block):
        # Recursion Moment!!
        # builds operation string by going into the children and finding their values and operations
        if not (isinstance(block.children[0], OperationBlock) or isinstance(block.children[1], OperationBlock)):
            return f"{block.children[0].getText()} {block.operation} {block.children[1].getText()}"
        elif not isinstance(block.children[0], OperationBlock):
            return f"{self.buildOperationString(block.children[0])} {block.operation} {block.children[1].getText()}"
        elif not isinstance(block.children[1], OperationBlock):
            return f"{block.children[1].getText()} {block.operation} {self.buildOperationString(block.children[0])}"
        else:
            return f"{self.buildOperationString(block.children[0])} {block.operation} {self.buildOperationString(block.children[1])}"

    def generateMainFunc(self):
        string = '\n\nif __name__ == "__main__":\n'
        for functionBlock in self.functionBlocks:
            string += f"\t{functionBlock.getName()}()\n"
        self.file.write(string)
        self.file.close()
