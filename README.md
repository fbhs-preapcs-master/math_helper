# Pre-AP Computer Science Exercise 1				math_helper_lastnfi.py

Write a program that will be useful in your math class this year.  Use the internet to find at least 5 formulas that should be used in your math class this year.
		
Program Requirements
		
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

Your program should be named math_helper_lastnamefi.py

# Setting Up Git/Github
This will be your first real experience with using Git and Github, so be patient, learn a lot and **ASK QUESTIONS**!!

You will need to download and install [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.18.0.windows.1/Git-2.18.0-64-bit.exe).

After installing Git, open a command prompt, and change to your PreAPCS folder: *cd PreAPCS*

Towards the top of this page is a green button that says "Clone or Download." Click it, then click the little clipboard icon with the arrow.

Go back to your command prompt and type in: *git clone* then press *ctrl v* to paste the link in.  Press Enter.

Something should happen.  

Now move your current math_helper program into the newly created "math_helper_#####" folder (where ##### is your github username...if you don't have this folder, STOP and ask for help...)

From the command line, type *git add math_helper_lastfi.py* where lastfi is your lastname/first initial (or whatever you named your program).  You can use *TAB* to auto-complete after typing in *git add math* here.  If you get an error, ASK FOR HELP.

Type *git commit -m "initial commit"* and press Enter.

Type *git push* and press Enter.  It should ask you for your Github username and password; type them in.

Refresh this page and notice that YOUR file should now be there.  If it's not...ASK FOR HELP.

# Using Git/Github
Git is "version control system".  Think of it as a way to save every version of your program as you develop it.

As you work and complete various parts of your program, you should go to your command line and type the following:
* *git add math_helper_lastfi.py*
* *git commit -m "**change made**"*

At the END of the period (before you log out), you should type:
* *git push* 

This will upload all of your work from class to Github where I can look at it, and you can access it from elsewhere if needed.  

I am expecting to see regular "commits" and should see your "push" at the end of each class period!

