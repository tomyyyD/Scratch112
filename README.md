# Scratch-112

This is a drag and drop imperative programming language developed in Python and using the cmu_112_graphics library for the GUI. You can run the program by running the main.py file in the terminal.

- [How to use](#how-to-use)
- [Documentation](#block-usage)
  - [External Blocks](#external-blocks)
    - [Functions](#function-block)
    - [Variable Assignment](#variable-assignment)
    - [For Loops](#for-loops)
    - [Conditionals](#conditionals)
  - [Internal Blocks](#internal-blocks)
    - [Variable Call Block](#variable-call-block)

## Disclaimer

Please run this project in Python 3.10 or later.

## How To Use

To spawn a block, press one of the buttons on the left-hand side of the screen. The block will appear in the top-left area of the block space.
There are two types of blocks, separated in the button space by the red line.
The blocks that are above the line are blocks that can be linked to one another and will correspond to one line of Python code These are called External Blocks.
The list of external blocks is:

- Function
- Variable Assignment
- Loop
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

# Block Usage

## External Blocks

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
- Another external block can be linked to this block by dragging the block over the **upper part of the block** that contains the "Loop {x} times" text. This block can also be linked to other external blocks.
- A For Loop block consists of two main parts.
  - A textbox at the top of the block is the Loop Input that accepts **numerical input only** and can be clicked on to modify the value. This corresponds the the number of times this loop will run.
  - A textbox at the bottom of the block. This textbox is where you can drag and drop other external blocks to have them run inside the loop. External block inside of a loop act the same as they would outside of a loop.

### Conditionals

- This block is an external block spawned by pressing the pink conditional button
- Similar to the For Loop block, and external block can be linked to this block by dragging it on to the **upper part of the block** where the conditional statement is. This block can also be linked to other external blocks.
- This block consists of 4 main parts.
  - A textbox at the top left called the Left Hand Side. This accepts internal blocks as input or Numerical values
  - A textbox at the top right called the Right Hand Side. This accepts internal blocks as input or numerical values
  - A textbox at the top middle called the Comparison. This accepts only "==" meaning equal, ">" meaning greater than, "<" meaning less than, ">=" meaning greater than or equal to, "<=" meaning less than or equal to. This compares the left hand side with the right hand side using the comparison.
  - A textbox at the bottom of the block. This block is where you can drag and drop ther external blocks to have them run inside the block if the comparison is true. Blocks inside a comparison act the same as they would outside of a comparison.

### Print

- This block is an external block spawned by pressing the orange Print button.
- This block has one main part. The textbox on the right side of the block. This textbox will accept numerical input or alphabetical input if that alphabetical input is wrapped in single quotes. This textbox can also accept any internal blocks.

### Return

- This block is an external block and can be linked to other blocks, but no block can link to it as no blocks are able to run in the current scope after a return is called in programming languages.
- This block is spawned by pressing the light blue Return button.
- This block operates very similarly to the print block and has one textbox which accept numerical, alphabetical, or internal block input.

## Internal Blocks

### Variable Call Block

- This block lets you call the value of a variable.
- This is an internal block, meaning it can be used in math operation blocks, Loop Input, and variable values. It cannot link as the next block in the chain nor can it be linked to.
- **You are only able to make variable call blocks for variables you have already assigned at least once**

### Math Operations

- These blocks let you perform math operations on other variables or on fixed values.
- They have two components
  - The textbox on the left, called the left hand side. accepts numerical values, alphabetical values as long as they are wrapped in single quotes, and other internal blocks as input.
  - The textbox on the right follows the same rules.
- This block will perform the mathematical operation it has to the values you give it.
  - given numerical values or variables with numerical values it will perform math
  - given strings, add will concatenate strings
  - given one string and one number, multiply will concatenate that string to itself that number of times, add will append that number to the end of the string.
    - The string value **Must** come before the numerical value, if not an error will occur.
  - If you attempt to subtract or divide a number and a string, an error will occur.
