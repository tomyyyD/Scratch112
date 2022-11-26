from Blocks import *


class Interpreter:
    def __init__(self, blocksList):
        self.file = open("output.py", 'w')
        self.functionBlocks = []
        for block in blocksList:
            if isinstance(block, FunctionBlock):
                self.functionBlocks.append(block)
        for functionBlock in self.functionBlocks:
            self.file.write(self.buildString(functionBlock, 0, functionBlock))
        # print(self.buildString(functionBlock, 0, functionBlock))
        self.generateMainFunc()

    def buildString(self, block, depth, lastDepthChange):
        string = ''
        if block is None:
            return ""
        if depth == -1:
            return string
        nextblock = block.next
        if isinstance(block, FunctionBlock):
            string += f"def {block.nameInput.getText()}():\n"
            depth += 1
        elif isinstance(block, VariableBlock):
            if isinstance(block.children[1], OperationBlock):
                string += (
                    "\t" * depth) + f"{block.children[0].getText()} = {self.buildOperationString(block.children[1])}\n"
            else:
                string += (
                    "\t" * depth) + f"{block.children[0].getText()} = {block.children[1].getText()}\n"
        elif isinstance(block, ReturnBlock):
            string += ("\t" * depth) + \
                f"return {block.textInput.getText()}\n"
        elif isinstance(block, PrintBlock):
            if isinstance(block.children[0], OperationBlock):
                string += (
                    "\t" * depth) + f"print({self.buildOperationString(self.children[0])})\n"
            else:
                string += (
                    "\t" * depth) + f"print({block.children[0].getText()})\n"
        elif isinstance(block, ForLoopBlock):
            string += ("\t" * depth) + \
                f"for i in range({block.loops.getText()}):\n"
            depth += 1
            lastDepthChange = block
            nextblock = block.value
        if block.next is None:
            depth -= 1
            if depth == 0:
                return string
            block = lastDepthChange
            nextblock = block.next

        string += self.buildString(nextblock, depth, lastDepthChange)

        return string

    def outputToFile(self, block, depth):
        if block is None:
            return
        string = ''
        if isinstance(block, FunctionBlock):
            string = f"def {block.nameInput.getText()}():\n"
            self.file.write(string)
            self.outputToFile(block.next, depth + 1)
            return
        elif isinstance(block, VariableBlock):
            if isinstance(block.children[1], OperationBlock):
                string = (
                    "\t" * depth) + f"{block.children[0].getText()} = {self.buildOperationString(block.children[1])}\n"
            else:
                string = (
                    "\t" * depth) + f"{block.children[0].getText()} = {block.children[1].getText()}\n"
            # self.file.write(string)
            # self.outputToFile(block.next)
        elif isinstance(block, ReturnBlock):
            string = f"\treturn {block.textInput.getText()}\n"
            # self.file.write(string)
        elif isinstance(block, PrintBlock):
            if isinstance(block.children[0], OperationBlock):
                string = (
                    "\t" * depth) + f"print({self.buildOperationString(self.children[0])})"
            else:
                string = (
                    "\t" * depth) + f"print({block.children[0].getText()})"
        elif isinstance(block, ForLoopBlock):
            string = ("\t" * depth) + f"for i in range({block.loops})\n"
            self.outputToFile(block.next, depth + 1)
            return
        self.file.write(string)
        self.outputToFile(block.next, depth)

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
