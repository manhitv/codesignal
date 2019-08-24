'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've been working on a numerical analysis when something went horribly wrong: your solution returned completely unexpected results. It looks like you apply a wrong function at some point of calculation. This part of the program was implemented by your colleague who didn't follow the PEP standards, so it's extremely difficult to comprehend.
To understand what function is applied to x instead of the one that should have been applied, you decided to go ahead and compare the result with results of all the functions you could come up with. Given the variable x and a list of functions, return a list of values f(x) for each x in functions.
*Example:
For x = 1 and functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"],
the output should be tryFunctions(x, functions) = [0.84147, 0.5403, 2, 1].
'''
def tryFunctions(x, functions):
    return [eval(i)(x) for i in functions]

