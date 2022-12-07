from Blocks import *


class Interpreter:
    def __init__(self, blocksList):
        self.file = open("output.py", 'w+')
        self.functionBlocks = []
        for block in blocksList:
            if isinstance(block, FunctionBlock):
                self.functionBlocks.append(block)
        self.file.write(f"class Output:\n\tdef __init__(self):\n")
        if self.buildString(blocksList[0], 1) == "":
            self.file.write("\t\tpass\n")
        else:
            self.file.write(self.buildString(blocksList[0], 2))
        for functionBlock in self.functionBlocks:
            self.file.write(self.buildString(functionBlock, 1))
        # print(self.buildString(functionBlock, 0, functionBlock))
        # self.generateMainFunc()
        string = f"output = Output()\n"
        string += f"print('----------------end of file-----------------')"
        self.file.write(string)
        self.file.close()

    # recursively builds a string that represents the blocks in the GUI

    def buildString(self, block, depth):
        string = ''
        if block is None:
            return ''
        if isinstance(block, TextBox):
            return block.getText()
        nextblock = block.next
        if isinstance(block, FunctionBlock):
            string += ('\t' * depth) + \
                f"def {block.nameInput.getText()}(self):\n"
            depth += 1
        elif isinstance(block, VariableBlock):
            string += (
                "\t" * depth) + f"{block.children[0].getText()} = {self.buildOperationString(block.children[1])}\n"
        elif isinstance(block, ReturnBlock):
            string += ("\t" * depth) + \
                f"return {self.buildOperationString(block.children[0])}\n"
        elif isinstance(block, PrintBlock):
            string += (
                "\t" * depth) + f"print({self.buildOperationString(block.children[0])})\n"
        elif isinstance(block, ForLoopBlock):
            string += ("\t" * depth) + \
                f"for i in range({self.buildOperationString(block.children[0])}):\n"
            # depth += 1
            # increase depth for nested blocks
            if isinstance(block.children[1], TextBox):
                string += ("\t" * (depth + 1)) + "pass\n"
            else:
                string += self.buildString(block.children[1],
                                           depth + 1)
        elif isinstance(block, ConditionalBlock):
            string += ("\t" * depth) + \
                f"if {self.buildOperationString(block.children[0])} {block.children[2].getText()} {self.buildOperationString(block.children[1])}:\n"
            if isinstance(block.children[3], TextBox):
                string += ("\t" * (depth + 1)) + "pass\n"
            else:
                string += self.buildString(block.children[3],
                                           depth + 1)

        string += self.buildString(nextblock, depth)

        return string

    def buildOperationString(self, block):
        # Recursion Moment!!
        # builds operation string by going into the children and finding their values and operations
        # print(block)
        if isinstance(block, TextBox):
            return block.getText()
        if isinstance(block, VariableCallBlock):
            return block.getText()
        if isinstance(block, FunctionCallBlock):
            return f"self.{block.getText()}()"
        if not (isinstance(block.children[0], OperationBlock) or isinstance(block.children[1], OperationBlock)):
            return f"({block.children[0].getText()} {block.operation} {block.children[1].getText()})"
        elif not isinstance(block.children[0], OperationBlock):
            # print("build first")
            return f"({block.children[0].getText()} {block.operation} {self.buildOperationString(block.children[1])})"
        elif not isinstance(block.children[1], OperationBlock):
            # print("build second")
            return f"({self.buildOperationString(block.children[0])} {block.operation} {block.children[1].getText()} )"
        else:
            return f"({self.buildOperationString(block.children[0])} {block.operation} {self.buildOperationString(block.children[1])})"

    def generateMainFunc(self):
        string = ''
        # string = '\n\nif __name__ == "__main__":\n'
        # for functionBlock in self.functionBlocks:
        #     string += f"\t{functionBlock.getName()}()\n"
        # self.file.write(string)
        # self.file.close()
        for functionBlock in self.functionBlocks:
            string += f"{functionBlock.getName()}()\n"
        string += f"print('----------------end of file-----------------')"
        self.file.write(string)
        self.file.close()
