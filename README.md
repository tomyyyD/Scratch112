# Scratch-112

This is a drag and drop imperative programming language developed in Python and using the cmu_112_graphics library for the GUI. You can run the program by running the main.py file in the terminal.

- [How to use](#how-to-use)
- [Documentation](#block-usage)
  - [Functions](#function-block)
  - [Variable Assignment](#variable-assignment)

## Disclaimer

Please run this project in Python 3.10 or later.

## How To Use

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

In order to remove a block from your block space, drag it over to the left so that the blocks center point is on the left side of the line. The block will then be removed.

## Block Usage

### Function Block

- Clicking on the yellow function button spawns this block. You will receive a prompt on screen to name your function. Once you type a name, the block will spawn. This block is used to create a function which can be called later.
- Any external block can be linked to this block by dragging the other block on top of this block. This will make the block you dragged the first line in the new function you created.

### Variable Assignment

- The Variable Assignment block is an external block. This block can be spawned by clicking the red "Variable" button.
- You will be prompted to assign your variable a name. After that, the block will spawn.
- This is an external block and can be linked to another block by dragging it on top of the other block. Other external blocks can also be linked to this block by dragging that block over your variable block.
- There are two components to a variable block. The textbox on the right hand side and the textbox on the left hand side.
  - The textbox on the left hand side is where you can modify the variable name and this should only recieve **alphabetical characters as input**.
  - The textbox on the right hand side is where you can modify the varible's value. This can recieve numerical input as well as alphabetical input if wrapped in single quotes. furthermore internal blocks can be placed in this textbox to modify the variable value.
- Once a variable is created with a variable assignment block, you will then be able to call that variable with a [Variable Call Block](#variable-call-block)

### For Loops

- This block is an external block spawned by pressing the purple for loop button.
- An external block. Another external block can be linked to this block by dragging the block over the **upper part of the block** that contains the "Loop {x} times" text. This block can also be linked to other external blocks.
- A For Loop block consists of two main parts.
  - A textbox at the top of the block is the Loop Input that accepts **numerical input only** and can be clicked on to modify the value. This corresponds the the number of times this loop will run.
  - A textbox at the bottom of the block. This textbox is where you can drag and drop other external blocks to have them run inside the loop. External block inside of a loop act the same as they would outside of a loop.

### Variable Call Block

- This block lets you call the value of a variable.
- This is an internal block, meaning it can be used in math operation blocks, Loop Input, and variable values. It cannot link as the next block in the chain nor can it be linked to.
- **You are only able to make variable call blocks for variables you have already assigned at least once**
