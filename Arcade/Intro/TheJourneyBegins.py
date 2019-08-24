'''
Write a function that returns the sum of two numbers.
*Example:
For param1 = 1 and param2 = 2, the output should be add(param1, param2) = 3.
'''
def add(param1, param2):
    return param1+param2

'''
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
*Example:
For year = 1905, the output should be centuryFromYear(year) = 20;
For year = 1700, the output should be centuryFromYear(year) = 17.
'''
def centuryFromYear(year):
    a = year/100
    b = int(year/100)
    if a>b:
        return b+1
    else: 
        return b

'''
Given the string, check if it is a palindrome.
*Example:
For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
For inputString = "abac", the output should be checkPalindrome(inputString) = false;
For inputString = "a", the output should be checkPalindrome(inputString) = true.
'''
def checkPalindrome(inputString):
    if str(inputString) == str(inputString)[::-1]:
        return True
    else:
        return False
