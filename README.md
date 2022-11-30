# Scratch-112

This is a drag and drop imperative programming language developed in Python and using the cmu_112_graphics library for the GUI. You can run the program by running the main.py file in the terminal.

- [How to use] (#how-to-use)
- [documentation] (#block-usage)
  - [Function] (#function-block)
  - [Variable Assignment] (#variable-assignment)

## Disclaimer

Please run this project in Python 3.10 or later.

## how to use

To spawn a block, press one of the buttons on the left-hand side of the screen. The block will appear in the top-left area of the block space.
There are two types of blocks, separated in the button space by the red line.
The blocks that are above the line are blocks that can be linked to one another and will correspond to one line of Python code These are called External Blocks.
The list of external blocks is:

- Function
- Variable Assignment
- For Loop
- Conditional
- Print
- Return

The blocks that are below the line are internal blocks, and they are placed on the textboxes of external blocks to create expressions. They do not correspond to a line off code but will appear on the same line as the external block they are inside.
The list of internal blocks is:

- Add
- Subtract
- Divide
- Multiply
- Variable Call

## Block Useage

### Function Block

Clicking on the yellow function button spawns this block. You will receive a prompt on screen to name your function. Once you type a name, the block will spawn. This block is used to create a function which can be called later.
Any external block can be linked to this block by dragging the other block on top of this block. This will make the block you dragged the first line in the new function you created.

### Variable Assignment

The Variable Assignment block is an external call. This block can be spawned by clicking the red "Variable" button. You will be prompted to assign your variable a name. This is an external block and can be linked to another block by dragging it on top of the other block. Other external blocks can also be linked to this block by dragging that block over your variable block.
Variable blocks have a default value of 112 in the textbox on the Right side of the block. To modify this value you can click on the textbox and manually input a value or you can place a Variable Call block or any mathematical operation block by dragging that other block on top of the textbox.
