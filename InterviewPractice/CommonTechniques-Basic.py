'''
Given an array of integers, write a function that determines whether the array contains any duplicates. Your function should return true if any element appears at least twice in the array, and it should return false if every element is distinct.
*Example:
For a = [1, 2, 3, 1], the output should be containsDuplicates(a) = true.
There are two 1s in the given array.
For a = [3, 1], the output should be containsDuplicates(a) = false.
The given array contains no duplicates.
'''
def containsDuplicates(a):
    dic = {}
    for e in a:
        if e in dic:
            return True
        else:
            dic[e] = True
    return False

'''
You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.
*Example:
For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be sumOfTwo(a, b, v) = true.
'''
def sumOfTwo(a,b,v):
    b = set(b)

    return any(v - x in b for x in a)

'''
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.
*Example:
For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be sumInRange(nums, queries) = 10.
The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.
'''
from itertools import accumulate

def sumInRange(nums, queries):
    a, s = [0] + list(accumulate(nums)), 0
    for i, j in queries:
        s += a[j+1] - a[i]
    return s%1000000007

'''
Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.
*Example:
For inputArray = [-2, 2, 5, -11, 6], the output should be arrayMaxConsecutiveSum2(inputArray) = 7.
The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.
'''
def arrayMaxConsecutiveSum2(inputArray):

    if len(inputArray) == 1:
        return inputArray[0]
    
    max_in = 0
    max_here = inputArray[0]
    
    for i in inputArray:
        max_in += i
        if max_in < i:
            max_in = i
        if max_in > max_here:
            max_here = max_in 
                        
    return max_here
