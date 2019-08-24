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

'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
*Example:
For
matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be
minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''
def minesweeper(matrix):

    r = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #m = -matrix[i][j]
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if 0<=i+k<len(matrix) and 0<=j+l<len(matrix[0]) and (not k)*(not l)!=1:
                        r[i][j] += matrix[i+k][j+l]
    return r

'''
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.
Return the blurred image as an integer, with the fractions rounded down.
*Example:
For
image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].
To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.
For
image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be
boxBlur(image) = [[5, 4], 
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.
'''
def boxBlur(image):

    x = len(image[0]) - 2;
    y = len(image) - 2;
    b = [[0 for i in range(x)] for j in range(y)]
    
    for i in range(y):
        for j in range(x):
            b[i][j] = image[i][j] + image[i][j+1] + image[i][j+2] + image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] + image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]
            b[i][j] //= 9
    return b        
