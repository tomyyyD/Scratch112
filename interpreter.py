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
            string = f"\t{block.name.text} = {block.value.text}\n"
            self.file.write(string)
            self.outputToFile(block.next)
        if isinstance(block, ReturnBlock):
            string = f"\treturn {block.value.name.text}\n"
            self.file.write(string)

    def generateMainFunc(self):
        string = '\n\nif __name__ == "__main__":\n'
        for functionBlock in self.functionBlocks:
            string += f"\t{functionBlock.getName()}()\n"
        self.file.write(string)
        self.file.close()


