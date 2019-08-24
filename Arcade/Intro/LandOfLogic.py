'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
*Example:
For text = "Ready, steady, go!", the output should be longestWord(text) = "steady".
'''
def longestWord(text):
    for i in range(len(text)):
        if text[i] not in string.ascii_letters:
            text = text[:i] + ' ' + text[i+1:]
    a = text.split(' ')
    b = [len(i) for i in a]
    return a[b.index(max(b))]

'''
Check if the given string is a correct time representation of the 24-hour clock.
*Example:
For time = "13:58", the output should be validTime(time) = true;
For time = "25:51", the output should be validTime(time) = false;
For time = "02:76", the output should be validTime(time) = false.
'''
def validTime(time):
    hours, minutes = int(time[:2]), int(time[3:])
    return 0 <= hours <= 23 and 0 <= minutes <= 59

'''    
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.
Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.
*Example:
For inputString = "2 apples, 12 oranges", the output should be sumUpNumbers(inputString) = 14.
'''
def sumUpNumbers(s):
    
    for i in range(len(s)):
        if not s[i].isdigit():
            s = s[:i] + " " + s[i+1:]
    a = s.split(' ')
    c = 0
    for j in a:
        if j.isdigit():
            c += int(j) 
    return c

'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
*Example:
For
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be differentSquares(matrix) = 6.
Here are all 6 different 2 × 2 squares:
1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
'''
def differentSquares(matrix):
    squares = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            sq = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j], matrix[i+1][j+1]]]
            if sq not in squares:
                squares.append(sq)
    return len(squares)

'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.
*Example:
For product = 12, the output should be digitsProduct(product) = 26;
For product = 19, the output should be digitsProduct(product) = -1.
'''
def digitsProduct(product):
    l_div = []
    answer = 0
    if product == 0:
        return 10
    if product == 1:
        return 1

    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            l_div.append(divisor)
    if product > 1:
        return -1

    for i in range(len(l_div) - 1, -1, -1):
        answer = answer * 10 + l_div[i]
    return answer
    
'''     
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.
Return an array of names that will be given to the files.
*Example:
For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
'''
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names

'''
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.
Assuming that your hunch is correct, decode the message.
*Example:
For code = "010010000110010101101100011011000110111100100001", the output should be messageFromBinaryCode(code) = "Hello!".
The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.
'''
def messageFromBinaryCode(code):
    code = int(code, 2)
    return code.to_bytes((code.bit_length() + 7)//8, 'big').decode()
    
'''
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.
*Example:
For n = 3, the output should be 
spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
'''
def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m

'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.
This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
*Example:
For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be sudoku(grid) = true;
For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be sudoku(grid) = false.
The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
'''
def sudoku(grid):

    gt = set(range(1, 10))

    for i in range(9):
        # horizontal check
        if set(grid[i]) != gt:
            return False
        a = []
        for j in range(9):
            a.append(grid[j][i])
        # vertical check
        if set(a) != gt:
            return False
        # 3x3 check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b = []
            for m in range(i, i+3):
                for n in range(j, j+3):
                    b.append(grid[m][n])
            if set(b) != gt:
                return False
    return True
