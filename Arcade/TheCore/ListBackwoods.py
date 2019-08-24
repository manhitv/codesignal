'''
Given a rectangular matrix and an integer column, return an array containing the elements of the columnth column of the given matrix (the leftmost column is the 0th one).
*Example:
For
matrix = [[1, 1, 1, 2], 
          [0, 5, 0, 4], 
          [2, 1, 3, 6]]
and column = 2, the output should be extractMatrixColumn(matrix, column) = [1, 0, 3].
'''
def extractMatrixColumn(matrix, column):
    return [matrix[i][column] for i in range(len(matrix))]

'''
Two two-dimensional arrays are isomorphic if they have the same number of rows and each pair of respective rows contains the same number of elements.
Given two two-dimensional arrays, check if they are isomorphic.
*Example:
For
array1 = [[1, 1, 1],
          [0, 0]]
and
array2 = [[2, 1, 1],
          [2, 1]]
the output should be areIsomorphic(array1, array2) = true;
For
array1 = [[2],
          []]
and
array2 = [[2]]
the output should be areIsomorphic(array1, array2) = false.
'''
def areIsomorphic(array1, array2):
    return len(array1) == len(array2) and [len(i) for i in array1] == [len(j) for j in array2]

'''
The longest diagonals of a square matrix are defined as follows:
the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.
*Example:
For
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
the output should be
reverseOnDiagonals(matrix) = [[9, 2, 7],
                              [4, 5, 6],
                              [3, 8, 1]]
'''
def reverseOnDiagonals(matrix):
    l = len(matrix) 
    for i in range(l//2):
        j = l-i-1
        matrix[i][i], matrix[j][j] = matrix[j][j], matrix[i][i]
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix
        
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
def swapDiagonals(matrix):
    l = len(matrix)
    for i in range(l):
        j = l-i-1
        matrix[i][i], matrix[i][j] = matrix[i][j], matrix[i][i]
    return matrix

'''
Given a rectangular matrix and integers a and b, consider the union of the ath row and the bth (both 0-based) column of the matrix (i.e. all cells that belong either to the ath row or to the bth column, or to both). Return sum of all elements of that union.
*Example:
For
matrix = [[1, 1, 1, 1], 
          [2, 2, 2, 2], 
          [3, 3, 3, 3]]
a = 1, and b = 3, the output should be crossingSum(matrix, a, b) = 12.
Here (2 + 2 + 2 + 2) + (1 + 3) = 12.
'''
def crossingSum(matrix, a, b):
    return sum(matrix[a]) + sum([i[b] for i in matrix]) - matrix[a][b]

'''
You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different characters to represent pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which draws a rectangle that has an upper left corner at (x1, y1) and a lower right corner at (x2, y2). Here the x-axis points from left to right, and the y-axis points from top to bottom.
Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the operation is applied. For the details about how rectangles are painted, see the example.
*Example:
For
canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
and rectangle = [1, 1, 4, 3], the output should be
drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  					['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                  					['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                  					['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                  					['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
Here is the rectangle, colored for illustration:
[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
['a', '*', '-', '-', '*', 'a', 'a', 'a'],
['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
['b', '*', '-', '-', '*', 'b', 'b', 'b'],
['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its corners and all of the other "pixels" remain the same.
'''
def drawRectangle(canvas, r):
    x1, y1, x2, y2 = r
    canvas[y1][x1] = canvas[y1][x2] = '*'
    canvas[y2][x2] = canvas[y2][x1] = '*'
    
    for i in range(y1+1, y2):
        canvas[i][x1] = '|'
        canvas[i][x2] = '|'
    
    for i in range(x1+1, x2):
        canvas[y1][i] = '-'
        canvas[y2][i] = '-'
    return canvas

'''
You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.
The team you favor plays in the following formation:
0 3 0
4 0 2
0 6 0
5 0 1
where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.
Here's how the players change their positions:
Given the current formation of the team and the number of times k it gained the serve, find the initial position of each player in it.
*Example:
For
formation = [["empty",   "Player5", "empty"],
             ["Player4", "empty",   "Player2"],
             ["empty",   "Player3", "empty"],
             ["Player6", "empty",   "Player1"]]
and k = 2, the output should be
volleyballPositions(formation, k) = [
    ["empty",   "Player1", "empty"],
    ["Player2", "empty",   "Player3"],
    ["empty",   "Player4", "empty"],
    ["Player5", "empty",   "Player6"]
]
For
formation = [["empty", "Alice", "empty"],
             ["Bob",   "empty", "Charlie"],
             ["empty", "Dave",  "empty"],
             ["Eve",   "empty", "Frank"]]
and k = 6, the output should be
volleyballPositions(formation, k) = [
    ["empty", "Alice", "empty"],
    ["Bob",   "empty", "Charlie"],
    ["empty", "Dave",  "empty"],
    ["Eve",   "empty", "Frank"]
]
'''
def volleyballPositions(f, k):
    for i in range(k%6):
        f[1][0], f[0][1], f[1][2], f[3][2], f[2][1], f[3][0] = f[0][1], f[1][2], f[3][2], f[2][1], f[3][0], f[1][0]
    return f
