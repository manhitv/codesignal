'''
Given an array of 2k integers (for some integer k), perform the following operations until the array contains only one element:
On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product.
After the algorithm has finished, there will be a single element left in the array. Return that element.
*Example:
For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be arrayConversion(inputArray) = 186.
We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.
'''
def arrayConversion(a):
    s, i = a[:], 1
    if len(s) == 1:
        return s[0]
    while True:
        if i%2:
            s = [s[i] + s[i+1] for i in range(0, len(s) - 1, 2)]
        else:
            s = [s[i]*s[i+1] for i in range(0, len(s) - 1, 2)]
        if len(s) == 1:
            break
        i += 1
    return s[0]
        
'''
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.
*Example:
For items = [3, 5, 2, 4, 5], the output should be arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
'''
def arrayPreviousLess(items):
    a = items[:]
    a[0] = -1
    for i in range(1, len(items)):
        for j in range(i-1, -1, -1):
            if items[i] > items[j]:
                a[i] = items[j]
                break
        else:
            a[i] = -1
    return a

'''
Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:
type indicates if it's a left or a right shoe;
size is the size of the shoe.
Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.
*Example:
For
shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
the output should be pairOfShoes(shoes) = true;
For
shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [1, 23]]
the output should be pairOfShoes(shoes) = false.
'''
def pairOfShoes(shoes):
    l1, l2 = [], []
    for i, j in shoes:
        if i == 0:
            l1.append(j)
        else:
            l2.append(j)
    return sorted(l1) == sorted(l2)
