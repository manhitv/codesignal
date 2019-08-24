'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
A spiral matrix is a square matrix of size n × n. It contains all the integers in range from 1 to n * n so that number 1 is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.
Given the size of the matrix n, your task is to create a spiral matrix.
*Example:
For n = 3, the output should be
createSpiralMatrix(n) = [[5, 4, 3],
                         [6, 9, 2],
                         [7, 8, 1]]
'''
def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0 for x in range(n)] for y in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros and has the following configuration:
lst[0] contains one element;
lst[1] contains two elements;
...
lst[n - 2] contains n - 1 elements;
lst[n - 1] contains n elements;
lst[n] contains n - 1 elements;
...
lst[2 * n - 3] contains two elements;
lst[2 * n - 2] contains one element.
Given an integer n, return a shell list.
*Example:
For n = 3, the output should be
constructShell(n) = [[0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 0],
                     [0]]
'''
def constructShell(n):
    return [[0]*min(i,2*n-i) for i in range(1,2*n)]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a power value to each action and each word. To begin somewhere, you defined a power of a word as the sum of powers of its characters, where power of a character is equal to its 1-based index in the plaintext alphabet.
Given a word, calculate its power.
*Example:
For word = "hello", the output should be wordPower(word) = 52.
Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. Thus, the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.
'''
def wordPower(word):
    num = dict([("a", 1), ("b", 2),("c", 3),("d", 4),("e", 5),("f", 6),("g", 7),("h", 8),("i", 9),("j", 10),("k", 11),("l", 12),("m", 13),("n", 14),("o", 15),("p", 16),("q", 17),("r", 18),("s", 19),("t", 20),("u", 21),("v", 22),("w", 23),("x", 24),("y", 25),("z", 26)])
    return sum([num[ch] for ch in word])

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
A pair of numbers is considered to be cool if their product is divisible by their sum. More formally, a pair (i, j) is cool if and only if (i * j) % (i + j) = 0.
Given two lists a and b, find cool pairs with the first number in the pair from a, and the second one from b. Return the number of different sums of elements in such pairs.
*Example:
For a = [4, 5, 6, 7, 8] and b = [8, 9, 10, 11, 12], the output should be coolPairs(a, b) = 2.
There are three cool pairs that can be formed from these arrays: (4, 12), (6, 12) and (8, 8). Their respective sums are 16, 18 and 16, which means that there are just 2 different sums: 16 and 18. Thus, the output should be equal to 2.
'''
def coolPairs(a, b):
    uniqueSums = {x+y for x in a for y in b if x*y%(x+y) == 0}
    return len(uniqueSums)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Looks like your little brother doesn't want to remember the multiplication table! Instead he wants to play videogames all day long. To teach him a lesson you'd like to write a virus that will pop up in the middle of the game and disappear only when the brother correctly solves several math questions.
To begin with, you need to construct a multiplication table. Given an integer n, return the multiplication table of size n × n.
*Example:
For n = 5, the output should be
multiplicationTable(n) = [[1, 2,  3,  4,  5 ], 
                          [2, 4,  6,  8,  10], 
                          [3, 6,  9,  12, 15], 
                          [4, 8,  12, 16, 20], 
                          [5, 10, 15, 20, 25]]
'''
def multiplicationTable(n):
    return [[j*i for i in range(1, n+1)] for j in range(1, n+1)]
