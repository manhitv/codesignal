'''
Caring for a plant can be hard work, but since you tend to it regularly, you have a plant that grows consistently. Each day, its height increases by a fixed amount represented by the integer upSpeed. But due to lack of sunlight, the plant decreases in height every night, by an amount represented by downSpeed.
Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight, your task is to find how many days it'll take for the plant to reach this height.
*Example:
For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
#	Day	Night
1	100	90
2	190	180
3	280	270
4	370	360
5	460	450
6	550	540
7	640	630
8	730	720
9	820	810
10	910	900
The plant first reaches a height of 910 on day 10.
'''
def growingPlant(upSpeed, downSpeed, desiredHeight):

    grow1 = upSpeed - downSpeed
    i = 0
    while True:
        night = grow1*i
        nextday = grow1*i + upSpeed
        if night >= desiredHeight:
            return i
        if nextday >= desiredHeight:
            return i+1
        i += 1

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
Given a string, output its longest prefix which contains only digits.
*Example:
For inputString = "123aa1", the output should be longestDigitsPrefix(inputString) = "123".
'''
def longestDigitsPrefix(inputString):

    i = 0
    while True:
        if not inputString[i].isdigit():
            return inputString[:i]
        i += 1
        if i >= len(inputString):
            break
    return inputString

'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
Given an integer, find its digit degree.
*Example:
For n = 5, the output should be digitDegree(n) = 0;
For n = 100, the output should be digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''
def digitDegree(n):
    
    if n < 10:
        return 0
    n = [int(x) for x in str(n)]
    return 1 + digitDegree(sum(n))

'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
The bishop has no restrictions in distance for each move, but is limited to diagonal movement. 
*Example:
For bishop = "a1" and pawn = "c3", the output should be bishopAndPawn(bishop, pawn) = true.
For bishop = "h1" and pawn = "h3", the output should be bishopAndPawn(bishop, pawn) = false.
'''
def bishopAndPawn(bishop, pawn):
    d = dict((enumerate(string.ascii_lowercase)))
    d1, d2 = 0, 0
    for key, value in d.items():
        if value == bishop[0]:
            d1 = key
        if value == pawn[0]:
            d2 = key
    return abs(d1 - d2) == abs(int(bishop[1]) - int(pawn[1]))
