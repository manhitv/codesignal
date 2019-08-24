'''
Given a string, return its encoding defined as follows:
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
*Example:
For s = "aabbbc", the output should be lineEncoding(s) = "2a3bc".
'''
def lineEncoding(s):
    grub = [ m.group(0) for m in re.finditer(r"(\w)\1*", s )]
    numb = 0
    out  = []
    for i in grub:
        numb += 1
        if len(i) > 1:
            out.append(grub[numb-1].replace(grub[numb-1], str(len(i))+i[0]))
        else:
            out.append(i)
    return ''.join(out)

'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
*Example:
For st = "abcdc", the output should be buildPalindrome(st) = "abcdcba".
'''
def buildPalindrome(st):
    if st == st[::-1]:
        return st
    l = len(st)
    if l <= 2:
        return st + st[0]
    for i in range(l):
        if st[i:][::-1] in st:
            return st + st[:i][::-1]

'''
Implement a function that determines if a given positive integer is a prime or not.
*Example:
For n = 47, the output should be isPrime(n) = true;
For n = 4, the output should be isPrime(n) = false.
'''
def isPrime(n):
    m = int(n**0.5)
    for i in range(2, m+1):
        if n%i == 0:
            return False
    return True

'''
Given a number and a range, find the largest integer within the given range that's divisible by the given number.
*Example:
For left = 1, right = 10, and divisor = 3, the output should be maxDivisor(left, right, divisor) = 9.
The largest integer divisible by 3 in range [1, 10] is 9.
'''
def maxDivisor(left, right, divisor):
    s = right - right%divisor
    return s if s in range(left, right+1) else -1

'''
In this problem, the product of the elements of an arbitrary array x is expressed as p(x).
You are given an array of integers a. Any array that you can obtain from a by removing some elements (possibly none, but not all) is denoted as s. Among all such arrays s, what is the maximum possible value of p(s)? Since the answer could potentially be very large, return the value of p(a) / p(s) instead.
*Example:
For a = [1, 2, -2, -3, 3, 5], the output should be maximumSubsetProduct(a) = 1.
Consider s = a (no elements were removed from the original array): p(s) = 1 · 2 · (-2) · (-3) · 3 · 5 = 180. There is no other s that has elements with a product larger than that. In this case, p(a) = p(s), therefore p(a) / p(s) = 1.
For a = [10, -10], the output should be maximumSubsetProduct(a) = -10.
p(a) = -100. For s = [10], p(s) = 10. p(s) cannot be any larger. Thus, the answer is p(a) / p(s) = -100 / 10 = -10.
'''
def maximumSubsetProduct(a):

    ps = 1
    count = 0
    b, c = [], []
    for ele in a:
        if ele == 0:
            return 0
        if 0< ele < 1:
            b.append(ele)
        if ele < 0:
            c.append(ele)
    for ele in b:
        ps *= ele
    if len(a) == 1:
        return 1
    if len(c)%2 == 0:
        return ps
    else:
        return ps*max(c)

'''
Given an integer index n, find the nth Fibonacci number.
Note: Write a solution with O(n) complexity and O(1) additional memory.
*Example:
For n = 2, the output should be fibonacciNumber(n) = 1.
F2 = F0 + F1 = 0 + 1 = 1
'''
def fibonacciNumber(n):
    a = [0 for i in range(n+1)]
    a[0:2] = [0, 1]
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
        
    return a[n]

'''
The factorial of n is defined as the product of all natural numbers up to and including n - 1 * 2 * 3 * ... * n. The quasifactorial of n is different in that after each multiplication the result is decreased by one. So the quasifactorial of n is (...((1 * 2 - 1) * 3 - 1) * ... * n - 1). The quasifactorial of 1 is 1.
Given a positive integer n, calculate its quasifactorial.
*Example:
For n = 4, the output should be quasifactorial(n) = 7.
'''
def quasifactorial(n):
    return quasifactorial(n-1)*n - 1 if n>2 else 1

'''
Given a set of complex values, find their product.
*Example:
For real = [1, 2] and imag = [1, 3], the output should be arrayComplexElementsProduct(real, imag) = [-1, 5].
The task is to calculate product of 1 + 1 * i and 2 + 3 * i, so the answer is (1 + 1i) * (2 + 3i) = -1 + 5i.
'''
def arrayComplexElementsProduct(real, imag):
    a = [0 for i in range(len(real)-1)]
    b = [0 for i in range(len(real)-1)]
    a[0] = real[0]*real[1] - imag[0]*imag[1]
    b[0] = real[0]*imag[1] + real[1]*imag[0]
    for i in range(1, len(real)-1):
        a[i] = a[i-1]*real[i+1] - b[i-1]*imag[i+1]
        b[i] = a[i-1]*imag[i+1] + real[i+1]*b[i-1] 
    return [a[-1], b[-1]]

'''
Write an algorithm that constructs an array of non unique prime factors of a number n.
*Example:
For n = 100, the output should be primeFactors(n) = [2, 2, 5, 5].
'''
def primeFactors(n):

    a = []
    i = 1
    while True:
        i += 1
        if n%i == 0:
            n = n//i
            a.append(i)
            i = 1
        if n==1:
            break
    return a

'''
Given an array of integers, find the number of inversions it contains.
*Example:
For inputArray = [1, 3, 2, 0], the output should be countInversionsNaive(inputArray) = 4.
'''
def countInversionsNaive(i):

    c = 0
    for k in range(len(i)-1):
        for j in range(k+1, len(i)):
            if i[k] > i[j]:
                c += 1
    return c

'''
Check if all digits of the given integer are even.
*Example:
For n = 248622, the output should be evenDigitsOnly(n) = true;
For n = 642386, the output should be evenDigitsOnly(n) = false.
'''
def evenDigitsOnly(n):
    return not any(int(x)%2 for x in str(n))

'''
Given an array of integers, find the product of its elements.
*Example:
For inputArray = [1, 3, 2, 10], the output should be arrayElementsProduct(inputArray) = 60.
'''
def arrayElementsProduct(i):
    import math
    if 0 in i:
        return 0
    return math.e**sum(math.log(x) for x in i)

'''
The longest diagonals of a square matrix are defined as follows:
the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to swap its longest diagonals by exchanging their elements at the corresponding positions.
*Example:
For
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
the output should be
swapDiagonals(matrix) = [[3, 2, 1],
                         [4, 5, 6],
                         [9, 8, 7]]
'''
def swapDiagonals(m):
    for i in range(len(m)):
        m[i][i], m[i][len(m)-1 -i] = m[i][len(m)-1 -i], m[i][i]
    return m

'''        
Implement a function that can subtract two reduced fractions and produce a new one.
*Example:
For a = [7, 10] and b = [3, 10], the output should be fractionSubtraction(a, b) = [2, 5].
7/10 - 3/10 = 4/10 = 2/5, so the answer is [2, 5].
'''
def fractionSubtraction(a, b):

    c = a[0]*b[1] - b[0]*a[1]
    d = a[1]*b[1]
    index = []
    for i in range(2, c+1):
        if c%i == 0 and d%i == 0:
            index.append(i)
    if len(index) == 0:
        return [c, d]
    return [c/max(index), d/max(index)]

'''
Given an integer n, find the number of trailing zeros in the decimal representation of n! (the exclamation mark means factorial).
*Example:
For n = 10, the output should be factorialTrailingZeros(n) = 2.
10! = 3628800, it has 2 trailing zeros.
'''
def factorialTrailingZeros(n):
    t, c = 1, 0
    for i in range(2, n+1):
        t *= i
    for j in range(len(str(t))-1, -1, -1):
        if str(t)[j]== '0':
            c += 1
        else:
            break
    return c

'''
Concatenate given strings using a specific separator.
*Example:
For strings = ["Code", "Fight", "On", "!"] and separator = "/", the output should be myConcat(strings, separator) = "Code/Fight/On/!/".
'''
def myConcat(strings, separator):

    return separator.join(strings)+separator

'''
Check whether the given string is a subsequence of the plaintext alphabet.
*Example:
For s = "effg", the output should be alphabetSubsequence(s) = false;
For s = "cdce", the output should be alphabetSubsequence(s) = false;
For s = "ace", the output should be alphabetSubsequence(s) = true;
For s = "bxz", the output should be alphabetSubsequence(s) = true.
'''
def alphabetSubsequence(s):

    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            return False
    return True
 
'''           
Check whether the given string is a substring of the plaintext alphabet.
*Example:
For s = "efghi", the output should be alphabetSubstring(s) = true;
For s = "bde", the output should be alphabetSubstring(s) = false.
'''
def alphabetSubstring(s):
    return (s in string.ascii_lowercase)

'''
Implement a function that can divide two fractions and produce a reduced fraction.
*Example:
For a = [2, 3] and b = [5, 6], the output should be fractionDivision(a, b) = [4, 5].
'''
def fractionDivision(a, b):
    import math
    c = math.gcd(a[0]*b[1], a[1]*b[0])
    return [a[0]*b[1]/c, a[1]*b[0]/c]

'''
Define a multiplication table of size n by m as follows: such table consists of n rows and m columns. Cell on the intersection of the ith row and the jth column (i, j > 0) contains the value of i * j.
Given integers n and m, find the number of different values that are found in the table.
*Example:
For n = 3 and m = 2, the output should be differentValuesInMultiplicationTable2(n, m) = 5.
'''
def differentValuesInMultiplicationTable2(n, m):
    a = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i*j not in a:
                a.append(i*j)
    return len(a)

'''
You are given a set of points on the Cartesian plane. Consider the distance between two points as the maximum difference of their coordinates. For example, the distance between points (1, 2) and (4, 6) is equal to max(|4 - 1|, |6 - 2|) = 4.
Given a set of points, find the pair with the largest distance and return the value of their distance.
*Example:
For a = [7, 6, 6, 8, 1, 2, 8, 6], the output should be largestDistance(a) = 7.
'''
def largestDistance(a):
    b = a[::2]
    c, d = [], []
    for i in range(len(a)):
        if i%2:
            c.append(a[i])
    for i in range(1, len(b)):
        for j in range(i):
            d.append(abs(b[i] - b[j]))
    for i in range(1, len(c)):
        for j in range(i):
            d.append(abs(c[i] - c[j]))
    return max(d)

'''
Given the number of points on the line and the number of colors you have, find the number of the ways to color each point into one of the given colors in such manner that each two adjacent points will be different color.
*Example:
For points = 3 and colors = 2, the output should be countLineColorings(points, colors) = 2.
'''
def countLineColorings(points, colors):
    s = 1
    for i in range(points):
        if i < colors:
            s *= colors-i
    return s

'''
It is believed that primeval humans, as far as counting their cattle was concerned, distinguished only among "one", "two", and "many". Given the number of sheep an imaginary primeval man is looking at, return a string he would use to describe that quantity.
*Example:
For n = 20, the output should be oneTwoMany(n) = "many".
'''
def oneTwoMany(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    else:
        return 'many'

'''
n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.
*Example:
For n = 3 and m = 10, the output should be candies(n, m) = 9.
Each child will eat 3 pieces. So the answer is 9.
'''
def candies(n, m):
    return m - m%n

'''
A string is said to be a correct sentence if it starts with the capital letter and ends with a full stop (.).
Given a string, check whether it represents a correct sentence.
*Example:
For inputString = "This is a correct sentence.", the output should be isCorrectSentence(inputString) = true;
For inputString = "this is an incorrect sentence.", the output should be isCorrectSentence(inputString) = false;
For inputString = "This is another incorrect sentence", the output should be isCorrectSentence(inputString) = false.
'''
def isCorrectSentence(inputString):
    a= inputString[0]
    b= inputString[-1]
    return a == a.upper() and b == '.'

'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
*Example:
For inputArray = [1, 1, 1], the output should be arrayChange(inputArray) = 3.
'''
def arrayChange(inputArray):
    a = 0
    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            a += -inputArray[i+1] + inputArray[i] + 1
            inputArray[i+1] = inputArray[i] + 1
    return a

'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
*Example:
For n = 10 and firstNumber = 2, the output should be circleOfNumbers(n, firstNumber) = 7.
'''
def circleOfNumbers(n, firstNumber):
    if firstNumber >= n//2:
        return firstNumber - n//2
    else:
        return firstNumber + n//2

'''
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
*Example:
For n = 240, the output should be lateRide(n) = 4.
Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
For n = 808, the output should be lateRide(n) = 14.
808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
'''
def lateRide(n):
    s = n%60
    m = (n-s)//60
    return sum(int(i) for i in str(m)) + sum(int(j) for j in str(s))

'''
Given an integer, find the number of the ways to change exactly one digit in it in order to obtain a bigger integer.
*Example:
For value = 10, the output should be countWaysToChangeDigit(value) = 17.
'''
def countWaysToChangeDigit(value):
    s = [9-int(i) for i in str(value)]
    for i in s:
        return sum(s)
        
'''
You just bought a public transit card that allows you to ride the Metro for a certain number of days.
Here is how it works: upon first receiving the card, the system allocates you a 31-day pass, which equals the number of days in January. The second time you pay for the card, your pass is extended by 28 days, i.e. the number of days in February (note that leap years are not considered), and so on. The 13th time you extend the pass, you get 31 days again.
You just ran out of days on the card, and unfortunately you've forgotten how many times your pass has been extended so far. However, you do remember the number of days you were able to ride the Metro during this most recent month. Figure out the number of days by which your pass will now be extended, and return all the options as an array sorted in increasing order.
*Example:
For lastNumberOfDays = 30, the output should be metroCard(lastNumberOfDays) = [31].
There are 30 days in April, June, September and November, so the next months to consider are May, July, October or December. All of them have exactly 31 days, which means that you will definitely get a 31-days pass the next time you extend your card.
'''
def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 30 or lastNumberOfDays == 28:
        return [31]
    else:
        return [28, 30, 31]

'''
Determine if the given string contains at least one English letter.
*Example:
For input = "a_ _2", the output should be latinLettersSearchRegExp(input) = true;
For input = "W2", the output should be latinLettersSearchRegExp(input) = true;
For input = "_1111 ", the output should be latinLettersSearchRegExp(input) = false.
'''
def latinLettersSearchRegExp(input):
    for i in input:
        if i in string.ascii_lowercase or i in string.ascii_uppercase:
            return True
    return False

'''
Let's define a specific geometric shape on an infinite grid:
A shape with an order of 1 is just a single cell.
A shape with an order of 2 can be visualized as a shape with an order of 1 with a new cell added to each edge of the original shape, as in the diagram below.
Following that same pattern, a shape with an order of n can be visualized as a shape with an order of n - 1 with a new cell added to each edge of each cell in the original shape.
You have two such shapes. Each shape is represented as an array containing three integers: the first element indicates the order of the shape, while the second and third elements indicate the coordinates of the shape's center on the grid. Calculate the number of cells in the area where the shape1 and shape2 intersect - in other words, the cells that the two shapes have in common.
*Example:
For shape1 = [3, 0, -1] and shape2 = [5, 3, 0], the output should be areaOfIntersection(shape1, shape2) = 8.
In this example, the cells that belong only to the first shape are blue, the cells that belong only to the second shape are yellow, and the 8 cells that belong to both of them are green.
'''
def areaOfIntersection(s1, s2):
    set11 = range(s1[1] + s1[2] - s1[0] + 1, s1[1] + s1[2] + s1[0])
    set12 = range(s1[1] - s1[2] - s1[0] + 1, s1[1] - s1[2] + s1[0])
    set21 = range(s2[1] + s2[2] - s2[0] + 1, s2[1] + s2[2] + s2[0])
    set22 = range(s2[1] - s2[2] - s2[0] + 1, s2[1] - s2[2] + s2[0])
    c = 0
    for i in range(s1[1] - s1[0] + 1, s1[1] + s1[0]):
        for j in range(s1[2] - s1[0] + 1, s1[2] + s1[0]):
            if i+j in set11 and i+j in set21 and i-j in set12 and i-j in set22:
                c+=1
    return c

'''
Write a function that returns the sum of two numbers.
*Example:
For param1 = 1 and param2 = 2, the output should be add(param1, param2) = 3.
'''
def add(param1, param2):
    return param1 + param2

'''
Call two integers a and b similar if divisor divides both a and b or if it doesn't divide either.
Given integers a, b and divisor, check if a and b are similar.
*Example:
For a = 10, b = 12, and divisor = 2, the output should be areSimilarNumbers(a, b, divisor) = true;
For a = 10, b = 12, and divisor = 3, the output should be areSimilarNumbers(a, b, divisor) = false.
'''
def areSimilarNumbers(a, b, divisor):
    if a%divisor != 0 and b%divisor != 0:
        return True
    if a%divisor == 0 and b%divisor == 0:
        return True
    return False

'''
You are given a string. Remove its first and last characters until the string is empty or the first and the last characters are not equal. Output the resulting string.
*Example:
For inputString = "abacaba", the output should be reduceString(inputString) = "".
Explanation: "bacab" -> "aca" -> "c" -> "".
For inputString = "12133221", the output should be reduceString(inputString) = "1332".
'''
def reduceString(s):
    while True:
        if len(s) < 1 or s[0] != s[-1]:
            return s
        s = s[1:-1]

'''
Count the number of different edges in a given undirected graph with no loops and multiple edges.
*Example:
For
matrix = [[false, true, true],
          [true, false, false],
          [true, false, false]]
the output should be graphEdges(matrix) = 2.
'''
def graphEdges(matrix):
    l = []
    for i in range(len(matrix)):
        if [matrix[i][0], matrix[i][-1]] not in l:
            l.append([matrix[i][0], matrix[i][-1]])
    if len(l) == 1:
        return 0
    return len(l)

'''
Two players - "black" and "white" are playing a game. The game consists of several rounds. If a player wins in a round, he is to move again during the next round. If a player loses a round, it's the other player who moves on the next round. Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.
*Example:
For lastPlayer = "black" and win = false, the output should be whoseMove(lastPlayer, win) = "white".
'''
def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    else:
        if lastPlayer == 'black':
            return 'white'
        else:
            return 'black'

'''
Given array of integers lengths, create an array of arrays output such that output[i] consists of lengths[i] elements and output[i][j] = j.
*Example:
For lengths = [1, 2, 0, 4], the output should be
create2DArray(lengths) = [[0], 
                          [0, 1], 
                          [], 
                          [0, 1, 2, 3]]
'''
def create2DArray(lengths):
    out = []
    for i in lengths:
        a = []
        if i > 0:
            for j in range(i):
                a.append(j)
        out.append(a)
    return out

'''
Given an array of integers, find the leftmost number that has a decimal representation which doesn't contain any digit more than once. If there is no such number, return -1 instead.
*Example:
For inputArray = [22, 111, 101, 124, 33, 30], the output should be differentDigitsNumberSearch(inputArray) = 124;
For inputArray = [1111, 404], the output should be differentDigitsNumberSearch(inputArray) = -1.
'''
def differentDigitsNumberSearch(inputArray):
    i = 0
    while i < len(inputArray):
        a = str(inputArray[i])
        if all(a[j] not in a[:j] + a[j+1:] for j in range(len(a))):
                return inputArray[i]
        i += 1    
    return -1
  
'''      
Define crossover operation over two equal-length strings A and B as follows:
the result of that operation is a string of the same length as the input strings result[i] is either A[i] or B[i], chosen at random
Given array of strings inputArray and a string result, find for how many pairs of strings from inputArray the result of the crossover operation over them may be equal to result.
Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the same element of the array twice (however, if there are two equal elements in the array, they can form a pair).
*Example:
For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be stringsCrossover(inputArray, result) = 2.
'''
def stringsCrossover(a, result):
    c, i = 0, 0
    while i < len(a) - 1:
        for j in range(i+1, len(a)):
            if all(result[k] in [a[i][k], a[j][k]] for k in range(len(a[i]))):
                c += 1
        i+= 1
    return c

'''
Find the longest string from the given array.
*Example:
For inputArray = ["a", "ab", "c"], the output should be longestString(inputArray) = "ab".
'''
def longestString(inputArray):
    l = [len(i) for i in inputArray]
    return inputArray[l.index(max(l))]

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
def comfortableNumbers(l, r):
    c = 0
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            li = sum([int(x) for x in str(i)])
            lj = sum([int(y) for y in str(j)])
            if i >= j - lj and j <= i + li:
                c += 1
    return c

'''
Check if the given point belongs to the given line.
*Example:
For point = [0, 1] and line = [1, 1, 0], the output should be pointInLine(point, line) = false;
For point = [1, -1] and line = [1, 1, 0], the output should be pointInLine(point, line) = true.
'''
def pointInLine(point, line):
    return point[0]*line[0] + point[1]*line[1] + line[2] == 0

'''
Let's call a string cool if it is formed only by English letters and no two lowercase and no two uppercase letters are in adjacent positions. Given a string, check if it is cool.
*Example:
For inputString = "aQwFdA", the output should be coolString(inputString) = true;
For inputString = "aAA", the output should be coolString(inputString) = false;
For inputString = "q q", the output should be coolString(inputString) = false.
'''
def coolString(s):
    if not s.isalpha():
        return False
    if len(s) == 1:
        return True
    return s[::2].islower() and s[1::2].isupper() if s[0].islower() else s[::2].isupper() and s[1::2].islower() 

'''
Find the sum of squares of all integers from 1 up to and including given N.
*Example:
For n = 5, the output should be sumOfSquares(n) = 55.
'''
def sumOfSquares(n):
    return sum([i**2 for i in range(1, n+1)])

'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
*Example:
For n = 1230, the output should be isLucky(n) = true;
For n = 239017, the output should be isLucky(n) = false.
'''
def isLucky(n):
    n = str(n)
    m = len(n)
    return sum([int(x) for x in n[:m//2]]) == sum([int(x) for x in n[m//2:]])

'''
Given an initial string, switch case of the minimal possible number of letters to make the whole string written in the upper case or in the lower case.
*Example:
For inputString = "Aba", the output should be caseUnification(inputString) = "aba";
For inputString = "ABa", the output should be caseUnification(inputString) = "ABA".
'''
def caseUnification(s):
    c1, c2 = 0, 0
    for i in range(len(s)):
        if s[i] != s.lower()[i]:
            c1 += 1
        if s[i] != s.upper()[i]:
            c2 += 1
    return s.lower() if c1 < c2 else s.upper()

'''
Given a string, check if a palindrome can be obtained from it by at most one swap of some pair of characters.
*Example:
For inputString = "aabaa", the output should be isOneSwapEnough(inputString) = true.
It is already a palindrome.
For inputString = "abab", the output should be isOneSwapEnough(inputString) = true.
For example, one can swap the leftmost 'a' with the leftmost 'b'.
For inputString = "abc", the output should be isOneSwapEnough(inputString) = false.
'''
def isOneSwapEnough(s):
    if s == s[::-1]:
        return True
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            s1 = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            if s1 == s1[::-1]:
                return True
    return False

'''
Find the leftmost digit that occurs in a given string.
*Example:
For inputString = "var_1__Int", the output should be firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be firstDigit(inputString) = '2';
For inputString = "0ss", the output should be firstDigit(inputString) = '0'.
'''
def firstDigit(s):
    for i in s:
        if i.isdigit():
            return i

'''
Given a matrix, find its transpose.
*Example:
For
matrix = [[1, 1, 3], 
          [2, 1, 1]]
the output should be
matrixTransposition(matrix) = [[1, 2],
                               [1, 1],
                               [3, 1]]
'''
def matrixTransposition(matrix):
    l1, l2 = len(matrix), len(matrix[0])
    a = [[0 for i in range(l1)] for j in range(l2)]
    for i in range(l1):
        for j in range(l2):
            a[j][i] = matrix[i][j]
    return a

'''
There are some apples that you want to give out as a present. You are going to distribute them between some gift boxes in such a way that all the boxes will contain an equal number of apples. You can leave out some of the apples, but no more than maxResidue. You also don't want to leave out more apples than necessary; that is, if each box contains x apples, the number of left out apples should be less than x.
Assume that you have an infinite number of gift boxes, and that all of them have the capacity of boxCapacity. In how many ways can you distribute the apples satisfying all of the above conditions?
*Example:
For apples = 7, boxCapacity = 4, and maxResidue = 1, the output should be applesDistribution(apples, boxCapacity, maxResidue) = 3.
There are three ways to distribute the apples:
seven boxes, one apple into each box, no apples left out;
three boxes, two apples into each box, one apple left out;
two boxes, three apples into each box, one apple left out.
'''
def applesDistribution(apples, boxCapacity, maxResidue):
    c = 0
    for i in range(1, boxCapacity+1):
        if apples%i <= maxResidue:
            c += 1
    return c
   
'''                
Given integers a and b, determine whether the following pseudocode results in an infinite loop
while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
*Example:
For a = 2 and b = 6, the output should be isInfiniteProcess(a, b) = false;
For a = 2 and b = 3, the output should be isInfiniteProcess(a, b) = true.
'''
def isInfiniteProcess(a, b):
    return True if a>b else (b-a)%2

'''
Given array of integers, find the number of sorted pairs formed by its (different) elements such that the second element in the pair is divisible by the first one.
*Example:
For sequence = [1, 3, 2], the output should be divisorsPairs(sequence) = 2.
These pairs are: (1, 3), (1, 2).
For sequence = [2, 4, 8], the output should be divisorsPairs(sequence) = 3.
These pairs are: (2, 4), (2, 8), (4, 8).
'''
from itertools import permutations
def divisorsPairs(sequence):
    l = list(permutations(sequence, 2))
    c = 0
    for i in l:
        if i[1]%i[0] == 0:
            c += 1
    return c

'''
For given integers a and b, find the last digit of ab.
*Example:
For a = 2 and b = 5, the output should be lastDigit(a, b) = 2.
Explanation: 25 = 32.
'''
def lastDigit(a, b):
    if b==0:
        return 1
    last_a = [int(i) for i in str(a)][-1]
    b = b%4 if b%4 != 0 else 4
    return [int(i) for i in str(last_a**b)][-1]

'''
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?
Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.
*Example:
For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
You can only carry the first item.
For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be knapsackLight(value1, weight1, value2, weight2, maxW) = 16.
You're strong enough to take both of the items with you.
For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be knapsackLight(value1, weight1, value2, weight2, maxW) = 7.
You can't take both items, but you can take any of them.
'''
def knapsackLight(value1, weight1, value2, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        if min(weight1, weight2) > maxW:
            return 0
        elif weight1 > maxW:
            return value2
        elif weight2 > maxW:
            return value1
        else:
            return max(value1, value2)

'''
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.
*Example:
For n = 6, l = 2, and r = 4, the output should be countSumOfTwoRepresentations2(n, l, r) = 2.
There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
'''
def countSumOfTwoRepresentations2(n, l, r):
    c = 0
    for i in range(l, r+1):
        if n-i >= i and n-i <= r:
            c += 1
    return c

'''
Given the x-coordinate of a point on the parabole with specified coefficients, find the y-coordinate of that point.
*Example:
For a = 1, b = 2, c = 3, and x = -1, the output should be parabole(a, b, c, x) = 2.
Explanation: y = ax2 + bx + c = 1 * (-1)2 + 2 * (-1) + 3 = 2.
'''
parabole = lambda a, b, c, x: a*x*x + b*x + c

'''
Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.
*Example:
For inputString = "AaBaa", the output should be isCaseInsensitivePalindrome(inputString) = true.
"aabaa" is a palindrome as well as "AABAA", "aaBaa", etc.
For inputString = "abac", the output should be isCaseInsensitivePalindrome(inputString) = false.
All the strings which can be obtained via changing case of some group of letters, i.e. "abac", "Abac", "aBAc" and 13 more, are not palindromes.
'''
def isCaseInsensitivePalindrome(s):
    return s.lower() == s.lower()[::-1]

'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
*Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.
'''
def adjacentElementsProduct(a):
    return max([a[i]*a[i+1] for i in range(len(a)-1)])

'''
Consider the following template for an equation:
a ? b ? c ? d
Here each letter stands for an integer value, and ? stands for either an equals sign or a multiplication operator.
You have an array values that contains four integers. Can you fill the template with the integers, two multiplication operators, and one equals sign, such that the resulting equation will be correct?
*Example:
For values = [2, 4, 3, 6], the output should be equationTemplate(values) = true.
Here is how the template can be filled to result in a correct equation: 2 * 6 = 3 * 4.
For values = [2, 3, 30, 5], the output should be equationTemplate(values) = true.
Here is one of the ways to fill the template to get a correct equation: 30 = 2 * 3 * 5.
For values = [2, 3, 5, 5], the output should be equationTemplate(values) = false.
There is no way to fill the template that will result in a correct equation.
'''
def equationTemplate(values):

    # minus 0
    minus = len([i for i in values if i < 0])
    if minus%2:
        return False
    # abs
    values = [abs(i) for i in values]
    max_value, min_value = max(values), min(values)
    value1, value2 = values[:], values[:]
    value1.remove(max_value)
    value2.remove(max_value)
    value2.remove(min_value)
    return max_value == value1[0]*value1[1]*value1[2] or max_value*min_value == value2[0]*value2[1]

'''
Given an integer n, find the value of phi(n), where phi is Euler's totient function.
*Example:
For n = 5, the output should be eulersTotientFunction(n) = 4.
'''
def eulersTotientFunction(n):
    
    from math import gcd
    return len([i for i in range(1, n+1) if gcd(i, n) == 1])

'''
Imagine the following situation for a given integers n and k. There are n people standing in a circle. They are numbered from 1 through n in clockwise direction. The counting out begins at person #1 and continues around the circle in a clockwise direction. In each step, k-1 people are skipped and the next person is removed from the circle. The elimination proceeds around the circle (which is becoming smaller and smaller as people get removed), until only one person remains, who is announced a winner.
The task is to find the place in the initial circle that would guarantee a win.
*Example:
For n = 3 and k = 2, the output should bejosephusProblem(n, k) = 3.
'''
def josephusProblem(n, k):
    return n if k%2 == 0 else 1

'''
Given integers n and k, find the kth divisor (1-based) of n or determine if n has less than k divisors.
*Example:
For n = 63 and k = 4, the output should be kthDivisor(n, k) = 9.
Divisors of number 63 are the following: 1, 3, 7, 9, 21, 63.
For n = 5 and k = 3, the output should be kthDivisor(n, k) = -1.
Number 5 has only two divisors.
'''
def kthDivisor(n, k):

    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c += 1
            if c == k:
                return i
    return -1

'''
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.
*Example:
For items = [3, 5, 2, 4, 5], the output should be arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
'''
def arrayPreviousLess(items):

    l = [-1]
    for i in range(1, len(items)):
        if items[i] > items[i-1]:
            l.append(items[i-1])
        else:
            l.append(-1)
    return l

'''
Check if the given matrix is diagonal.
*Example:
For
matrix = [[1, 0, 0], 
          [0, 5, 0], 
          [0, 0, 3]]
the output should be isDiagonalMatrix(matrix) = true;
For
matrix = [[1, 0, 0], 
          [0, 5, 0], 
          [2, 0, 3]]
the output should be isDiagonalMatrix(matrix) = false.
'''
def isDiagonalMatrix(matrix):

    return all([matrix[i][j] == 0 for i in range(len(matrix)) for j in range(len(matrix[0])) if i != j])

'''
You're given an integer n.
If n is even, divide it by 2.
If n is odd, change it to 3 * n + 1.
Repeat the process until n = 1. Return the number of steps performed by the above algorithm.
*Example:
For n = 5, the output should be hailstoneSequence(n) = 5.
The sequence is 5 -> 16 -> 8 -> 4 -> 2 -> 1, so the number of steps is 5.
'''
def hailstoneSequence(n):

    c = 0
    while True:
        if n == 1:
            return c
        if n%2:
            n = 3*n+1
        else:
            n = n//2
        c += 1

'''    
Given two integers a and b, find the remainder of a when divided by b.
*Example:
For a = 5 and b = 3, the output should be findTheRemainder(a, b) = 2.
'''
findTheRemainder = lambda a, b: a%b

'''
Determine whether a given fraction is proper.
*Example
For a = [7, 2], the output should be properOrImproper(a) = "Improper".
'''
properOrImproper = lambda a: 'Proper' if abs(a[0]) < abs(a[1]) else 'Improper'

'''
Two lines ax + by + c = 0 and a'x + b'y + c' = 0 are parallel if and only if a * b' = b * a'.
Check if the two given lines are parallel.
*Example:
For line1 = [1, -1, 0] and line2 = [1, 1, 0], the output should be parallelLines(line1, line2) = false.
'''
parallelLines = lambda l1, l2: l1[0]*l2[1] == l1[1]*l2[0]

'''
Given an array of integers inputArray and an integer bound, find the smallest array element strictly greater than bound.
*Example:
For inputArray = [1, 3, 5, 4, 2, 6] and bound = 3, the output should be arrayMinimumAboveBound(inputArray, bound) = 4.
'''
def arrayMinimumAboveBound(inputArray, bound):

    for i in sorted(inputArray):
        if i > bound:
            return i
