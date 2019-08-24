'''
Given an integer size, return array of length size filled with 1s.
*Example:
For size = 4, the output should be createArray(size) = [1, 1, 1, 1].
'''
def createArray(size):
    a = []
    for i in range(size):
        a.append(1)
    return a

'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
*Example:
For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    a = []
    for x in inputArray:
        if x==elemToReplace:
            a.append(substitutionElem)
        else:
            a.append(x)
    return a

'''
Reversing an array can be a tough task, especially for a novice programmer. Mary just started coding, so she would like to start with something basic at first. Instead of reversing the array entirely, she wants to swap just its first and last elements.
Given an array arr, swap its first and last elements and return the resulting array.
*Example:
For arr = [1, 2, 3, 4, 5], the output should be firstReverseTry(arr) = [5, 2, 3, 4, 1].
'''
def firstReverseTry(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr

'''
Given two arrays of integers a and b, obtain the array formed by the elements of a followed by the elements of b.
*Example:
For a = [2, 2, 1] and b = [10, 11], the output should be concatenateArrays(a, b) = [2, 2, 1, 10, 11].
'''
def concatenateArrays(a, b):
    for x in b:
        a.append(x)
    return a

'''
Remove a part of a given array between given 0-based indexes l and r (inclusive).
*Example:
For inputArray = [2, 3, 2, 3, 4, 5], l = 2, and r = 4, the output should be removeArrayPart(inputArray, l, r) = [2, 3, 5].
'''
def removeArrayPart(inputArray, l, r):
    a = []
    for i in range(len(inputArray)):
        if i < l or i > r:
            a.append(inputArray[i])
    return a

'''
We define the middle of the array arr as follows:
if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.
*Example:
For arr = [7, 2, 2, 5, 10, 7], the output should be isSmooth(arr) = true.
The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.
For arr = [-5, -5, 10], the output should be isSmooth(arr) = false.
The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.
'''
def isSmooth(arr):
    mid = 0
    if len(arr)%2:
        mid = arr[len(arr)//2]
    else:
        mid = arr[len(arr)//2-1] + arr[len(arr)//2]
    return (arr[0] == arr[-1] and arr[0] == mid)

'''
We define the middle of the array arr as follows:
if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
Given array arr, your task is to find its middle, and, if it consists of two elements, replace those elements with the value of middle. Return the resulting array as the answer.
*Example:
For arr = [7, 2, 2, 5, 10, 7], the output should be replaceMiddle(arr) = [7, 2, 7, 10, 7].
The middle consists of two elements, 2 and 5. These two elements should be replaced with their sum, i.e. 7.
For arr = [-5, -5, 10], the output should be replaceMiddle(arr) = [-5, -5, 10].
The middle is defined as a single element -5, so the initial array with no changes should be returned.
'''
def replaceMiddle(arr):
    if len(arr)%2:
        return arr
    else:
        i = len(arr)//2 - 1
        if i == 0:
            return [sum(arr)]
        a = arr[:i]
        a.append(arr[i]+arr[i+1])
        for ele in arr[i+2:]:
            a.append(ele)
    return a

'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
*Example:
For statues = [6, 2, 3, 8], the output should be makeArrayConsecutive2(statues) = 3.
Ratiorg needs statues of sizes 4, 5 and 7.
'''
def makeArrayConsecutive2(statues):
    a = min(statues)
    b = max(statues)
    c = 0
    if len(statues) <= 1:
        return 0
    for x in statues:
        if x > a and x < b:
            c += 1
    return b - a - c - 1
