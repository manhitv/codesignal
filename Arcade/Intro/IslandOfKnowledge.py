'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.
Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.
Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
*Example:
For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
'''
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    return (min(yourLeft, yourRight)==min(friendsLeft, friendsRight) and max(yourLeft, yourRight)==max(friendsLeft, friendsRight))

'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
*Example:
For inputArray = [2, 4, 1, 0], the output should be arrayMaximalAdjacentDifference(inputArray) = 3.
'''
def arrayMaximalAdjacentDifference(a):

    return max(abs(a[i]-a[i+1]) for i in range(len(a)-1))

'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
Given a string, find out if it satisfies the IPv4 address naming rules.
*Example:
For inputString = "172.16.254.1", the output should be isIPv4Address(inputString) = true;
For inputString = "172.316.254.1", the output should be isIPv4Address(inputString) = false.
316 is not in range [0, 255].
For inputString = ".254.255.0", the output should be isIPv4Address(inputString) = false.
There is no first number.
'''
def isIPv4Address(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)You are given an array of integers representing coordinates of obstacles situated on a straight line.

'''
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles.
*Example:
For inputArray = [5, 3, 6, 7, 9], the output should be avoidObstacles(inputArray) = 4.
'''
def avoidObstacles(inputArray):
    
    for i in range(1, max(inputArray)):
        divs = any([x for x in inputArray if not x%i])
        if not divs:
            return i
    
    return max(inputArray) + 1

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
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if 0<=i+k<len(matrix) and 0<=j+l<len(matrix[0]) and (not k)*(not l)!=1:
                        r[i][j] += matrix[i+k][j+l]
    return r
