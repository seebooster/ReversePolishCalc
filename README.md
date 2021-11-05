# ReversePolishCalc

Hello! 

In this repo you will find the program 'Calc.py' which is a reverse polish notation calculator. This utilizes a stack data structure to fluidly carry out
basic algebraic operations (adding, subtracting, dividing, multiplying) to a dynamically changing list of inputed numbers.

Commands should be passed in the following format: "num1 num2 operator." For example, if you pass "3 2 -", 3-2 will be calculated, and 1 will be the output. 

After a calculation has been executed, the solution will be appended to the end of the data stack, and can be used in the next operation. For example, if, after the previous input 
(3 2 -), "5 *" is entered, 1*5 will be calculated, and 5 will be the output. Inputs can also be entered sequentially. Finally, multiple operations can be entered in a single input.
For example, "3 2 - 5 * 6 -" will carry out the following operation: ((3-2)*5) - 6 (outputting -1).

The calculator utilizes the following commands:

"quit" will exit the program
"clear" will clear the data saved in the stack
"stack" will show the data currently saved in the stack

