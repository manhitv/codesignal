'''
Given array of integers, remove each kth element from it.
*Example:
For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
'''
def extractEachKth(inputArray, k):
    if k == 1:
        return []
    b = inputArray[:k-1]
    m = len(inputArray)//k
    if m == 0:
        return inputArray
    for i in range(1, m):
        for j in range(k*i, k*(i+1)-1):
                b.append(inputArray[j])
    for ele in inputArray[k*m:]:
        b.append(ele)
    return b

'''
Find the leftmost digit that occurs in a given string.
*Example:
For inputString = "var_1__Int", the output should be firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be firstDigit(inputString) = '2';
For inputString = "0ss", the output should be firstDigit(inputString) = '0'.
'''
def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i

'''
Given a string, find the number of different characters in it.
*Example:
For s = "cabca", the output should be differentSymbolsNaive(s) = 3.
There are 3 different characters a, b and c.
'''
def differentSymbolsNaive(s):
    s = set(list(s))
    return len(s)

'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.
*Example:
For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:
2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
'''
def arrayMaxConsecutiveSum(inputArray, k):

    a = sum(inputArray[:k])
    b = a
    for i in range(k, len(inputArray)):
        b = b - inputArray[i - k] + inputArray[i]
        if b > a:
            a = b
    return a
