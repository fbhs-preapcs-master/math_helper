# Advanced Computer Science 			math_helper.py

## Objective
You will write a program that will be useful in your math class this year.  Use the internet to find at least 5 formulas that should be used in your math class this year.
		
## Program Requirements
		
* The formulas must use:
  * addition, subtraction, multiplication, division, integer division, exponentiation (raising to a power), and square roots (at least one of each).
  * the formulas can optionally also use factorial, logarithms, trig functions (sine, cosine, tangent), modulus, or other math functions/operands.
  * Your program should use appropriately named functions, with appropriately named parameters.
  * Docstrings and *doctests* must be included for each function.
  * Your program should present a list of options for the user (which formula to use), then ask for the appropriate inputs for the requested formula.
  * Your program should allow for multiple formulas to be used without restarting the program.

As part of your testing process, you will need to find the correct input/output values from the formulas without your program.  You can calculate these by hand with a calculator, or use another verifiable source (textbook, online tutoring site, etc.)

You will be required to use “doctest” comments for each function (see the example code and ask questions in class!)  You will need at least 5 test cases for each formula (function).  Try to think of edge-cases, that is, the cases that may cause the formula to act inconsistently (large numbers, small numbers/decimals, negative numbers, etc.)

If a formula has a domain besides all real numbers, be sure that your function validates the user's input and displays an appropriate error message if necessary.

Take a look at the doctest_example.py and my use of the “raise” command that causes an exception.  We will discuss “try-except” blocks in class.


## Implementation Process
1. Decide on a formula to include
2. Write a function with the appropriate parameters that returns the "answer"
3. Write at least 5 doctests for your function and make sure it works correctly
4. If you have all 5 functions done, continue to step 5, otherwise, go back to step 1

**Only continue if you have finished all 5 functions and their doctests!**

5. Write a main function that will be executed when the program is run and will serve as the user interface.  It should:
    * introduce the user to the program.
    * provide a list of the available formulas
    * allow the user to select the formula
    * follow up their selection by asking for the appropriate inputs for the chosen formula
    * use the function created in steps 1-4 to get and display the answer
    * allow the user to select another formula or quit


## Submission
You will regularly add/commit/push via Github so I can track your progress and provide assistance.  When problems arise, you can use the "Issues" feature of Github to request help.  I will clone your repository and run your program to check for its completion on or after the due date discussed in class.


