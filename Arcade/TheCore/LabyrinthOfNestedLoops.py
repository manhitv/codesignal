'''
Determine if the given number is a power of some non-negative integer.
*Example:
For n = 125, the output should be isPower(n) = true;
For n = 72, the output should be isPower(n) = false.
'''
def isPower(n):
    import math
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            for j in range(2, n//i):
                if i**j == n:
                    return True
    return False

'''
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.
*Example:
For n = 9, the output should be isSumOfConsecutive2(n) = 2.
There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.
For n = 8, the output should be isSumOfConsecutive2(n) = 0.
There are no ways to represent n = 8.
'''
def isSumOfConsecutive2(n):
    if n == 1:
        return 0
    i, j, c, s = 1, 1, 0, 0
    while True:
        s += i
        if s == n:
            c += 1
        elif s < n:
            i += 1
            continue
        else: 
            s = 0
            i = j + 1
            j += 1
        if j >= n:
            break
    return c

'''        
Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.
Given the first element a0, find the length of the sequence.
*Example:
For a0 = 16, the output should be squareDigitsSequence(a0) = 9.
Here's how elements of the sequence are constructed:
a0 = 16
a1 = 12 + 62 = 37
a2 = 32 + 72 = 58
a3 = 52 + 82 = 89
a4 = 82 + 92 = 145
a5 = 12 + 42 + 52 = 42
a6 = 42 + 22 = 20
a7 = 22 + 02 = 4
a8 = 42 = 16, which has already occurred before (a0)
Thus, there are 9 elements in the sequence.
For a0 = 103, the output should be squareDigitsSequence(a0) = 4.
The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.
'''
def squareDigitsSequence(a0):
    a = [a0]
    while True:
        a.append(sum([int(x)**2 for x in str(a[-1])]))
        if a[-1] in a[:-1]:
            break
    return len(a)

'''
You work in a company that prints and publishes books. You are responsible for designing the page numbering mechanism in the printer. You know how many digits a printer can print with the leftover ink. Now you want to write a function to determine what the last page of the book is that you can number given the current page and numberOfDigits left. A page is considered numbered if it has the full number printed on it (e.g. if we are working with page 102 but have ink only for two digits then this page will not be considered numbered).
It's guaranteed that you can number the current page, and that you can't number the last one in the book.
*Example:
For current = 1 and numberOfDigits = 5, the output should be pagesNumberingWithInk(current, numberOfDigits) = 5.
The following numbers will be printed: 1, 2, 3, 4, 5.
For current = 21 and numberOfDigits = 5, the output should be pagesNumberingWithInk(current, numberOfDigits) = 22.
The following numbers will be printed: 21, 22.
For current = 8 and numberOfDigits = 4, the output should be pagesNumberingWithInk(current, numberOfDigits) = 10.
The following numbers will be printed: 8, 9, 10.
'''
def pagesNumberingWithInk(current, numberOfDigits):
    
    s = 0
    while True:
        s += len(str(current))
        current += 1
        if s <= numberOfDigits and s+len(str(current)) > numberOfDigits:
            return current-1

'''
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.
How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?
*Example:
For l = 10 and r = 12, the output should be comfortableNumbers(l, r) = 2.
Here are all values of s(x) to consider:
s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).
'''
def sumDigit(x):
    return sum([int(ele) for ele in str(x)])
def comfortableNumbers(l, r):
    c = 0
    for i in range(l, r):
        for j in range(i+1, r+1):
            if j <= sumDigit(i) + i and j - sumDigit(j) <= i:
                c += 1
    return c

'''
We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.
It follows that the weaker the number, the greater overall weakness it has. For the given integer n, you need to answer two questions:
what is the weakness of the weakest numbers in the range [1, n]?
how many numbers in the range [1, n] have this weakness?
Return the answer as an array of two elements, where the first element is the answer to the first question, and the second element is the answer to the second question.
*Example:
For n = 9, the output should be weakNumbers(n) = [2, 2].
Here are the number of divisors and the specific weakness of each number in range [1, 9]:
1: d(1) = 1, weakness(1) = 0;
2: d(2) = 2, weakness(2) = 0;
3: d(3) = 2, weakness(3) = 0;
4: d(4) = 3, weakness(4) = 0;
5: d(5) = 2, weakness(5) = 1;
6: d(6) = 4, weakness(6) = 0;
7: d(7) = 2, weakness(7) = 2;
8: d(8) = 4, weakness(8) = 0;
9: d(9) = 3, weakness(9) = 2.
As you can see, the maximal weakness is 2, and there are 2 numbers with that weakness level.
'''
def weakNumbers(n):
    a, b, e = [], [], []
    for i in range(1, n+1):
        c, d = 0, 0
        for j in range(1, i+1):
            if i%j == 0:
                c += 1
        a.append(c)     #num of divisors
        for k in range(len(a)-1):
            if a[k] > a[-1]:
                d += 1
        b.append(d)     #list of weakness   
    for ele in b:
        if ele == max(b):
            e.append(ele)
    return [max(b), len(e)]        

'''
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.
How many points with integer coordinates are located inside the given rectangle (including on its sides)?
*Example:
For a = 6 and b = 4, the output should be rectangleRotation(a, b) = 23.
The following picture illustrates the example, and the 23 points are marked green.
'''
def rectangleRotation(a, b):
    
    m, c = max(a, b), 0
    for x in range(-m, m):
        for y in range(-m, m):
            if (x-y)**2 <= a**2/2 and (x+y)**2 <= b**2/2:
                c += 1
    return c

