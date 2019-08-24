'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
*Example:
For n = 10 and firstNumber = 2, the output should be circleOfNumbers(n, firstNumber) = 7.
'''
def circleOfNumbers(n, firstNumber):

    return firstNumber+n/2 if n/2 > firstNumber else firstNumber-n/2

'''
You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.
*Example:
For deposit = 100, rate = 20, and threshold = 170, the output should be depositProfit(deposit, rate, threshold) = 3.
Each year the amount of money in your account increases by 20%. So throughout the years, your balance would be:
year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172.8.
Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.
'''
def depositProfit(deposit, rate, threshold):
    d = deposit
    i = 0
    while True:
        i += 1
        d *= 1+rate/100
        if d >= threshold:
            return i

'''
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum: abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)
If there are several possible answers, output the smallest one.
*Example:
For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.
for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.
For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.
for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.
'''
def absoluteValuesSumMinimization(a):

    b = []
    for i in range(len(a)):
        c = []
        for j in range(len(a)):
            c.append(abs(a[i] - a[j]))
        b.append(sum(c))
    return a[b.index(min(b))]

'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.
Note: You're only rearranging the order of the strings, not the order of the letters within the strings!
*Example:
For inputArray = ["aba", "bbb", "bab"], the output should be stringsRearrangement(inputArray) = false.
There are 6 possible arrangements for these strings:
["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.
For inputArray = ["ab", "bb", "aa"], the output should be stringsRearrangement(inputArray) = true.
It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
'''
from itertools import permutations as p

def stringsRearrangement(A):
    for a in p(A):
        res = True
        
        for i in range(len(a) - 1):
            c = list(a[i])
            n = list(a[i+1])
            li = [ j for j in range(len(a[i])) if n[j] != c[j] ]
                
            if len(li) != 1:
                res = False
                break
        if res:
            return True

    return False
