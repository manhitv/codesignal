'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.
Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). Only this part is allowed to be changed.
*Example:
For n = 50, the output should be countBits(n) = 6.
5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.
'''
def countBits(n):
    return n.bit_length()

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.
To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.
*Example:
For n = 15, the output should be modulus(n) = 1;
For n = 23.12, the output should be modulus(n) = -1.
'''
def modulus(n):
    if n == int(n):
        return n % 2
    else:
        return -1

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.
Hint: with Python it's possible to swap several elements in a single line. To solve the task, use this knowledge to fill in both of the blanks (...).
*Example:
For arr = [2, 4, 1, 5], the output should be simpleSort(arr) = [1, 2, 4, 5].
'''
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.
Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!
Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.
*Example:
For n = "1302" and x = 5, the output should be baseConversion(n, x) = "ca".
Here's why:
13025 = 20210 = ca16.
'''
def baseConversion(n, x):
    return hex(int(n,x))[2:]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've just started to study impartial games, and came across an interesting theory. The theory is quite complicated, but it can be narrowed down to the following statements: solutions to all such games can be found with the mex function. Mex is an abbreviation of minimum excludant: for the given set s it finds the minimum non-negative integer that is not present in s.
You don't yet know how to implement such a function efficiently, so would like to create a simplified version. For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.
Hint: for loops also have an else clause which executes when the loop completes normally, i.e. without encountering any breaks
*Example:
For s = [0, 4, 2, 3, 1, 7] and upperBound = 10, the output should be mexFunction(s, upperBound) = 5.
5 is the smallest non-negative integer that is not present in s, and it is smaller than upperBound.
For s = [0, 4, 2, 3, 1, 7] and upperBound = 3, the output should be mexFunction(s, upperBound) = 3.
The minimum excludant for the given set is 5, but it's greater than upperBound, so the output should be 3.
'''
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound    
    return found

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, your task is to chop off its first and its last element until it becomes beautiful. Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.
Hint: one of the features introduced in Python 3 called extended unpacking could help here.
*Example:
For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be listBeautifier(a) = [4, 38, 4].
Here's how the answer is obtained:
[3, 4, 2, 4, 38, 4, 5, 3, 2] => [4, 2, 4, 38, 4, 5, 3] => [2, 4, 38, 4, 5] => [4, 38, 4].
For a = [1, 4, -5], the output should be listBeautifier(a) = [4].
'''
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res
