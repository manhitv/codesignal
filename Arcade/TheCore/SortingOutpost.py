'''
A noob programmer was given two simple tasks: sum and sort the elements of the given array
a = [a1, a2, ..., an]. He started with summing and did it easily, but decided to store the sum he found in some random position of the original array which was a bad idea. Now he needs to cope with the second task, sorting the original array a, and it's giving him trouble since he modified it.
Given the array shuffled, consisting of elements a1, a2, ..., an, a1 + a2 + ... + an in random order, return the sorted array of original elements a1, a2, ..., an.
*Example:
For shuffled = [1, 12, 3, 6, 2], the output should be shuffledArray(shuffled) = [1, 2, 3, 6].
1 + 3 + 6 + 2 = 12, which means that 1, 3, 6 and 2 are original elements of the array.
For shuffled = [1, -3, -5, 7, 2], the output should be shuffledArray(shuffled) = [-5, -3, 2, 7].
'''
def shuffledArray(shuffled):
    shuffled.remove(sum(shuffled) // 2)
    return sorted(shuffled)

'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
*Example:
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''
def sortByHeight(a):
    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l

'''
Given an array of strings, sort them in the order of increasing lengths. If two strings have the same length, their relative order must be the same as in the initial array.
*Example:
For
inputArray = ["abc",
              "",
              "aaa",
              "a",
              "zz"]
the output should be
sortByLength(inputArray) = ["",
                            "a",
                            "zz",
                            "abc",
                            "aaa"]
'''
def sortByLength(inputArray):

    return sorted(inputArray, key = lambda x: len(x))    
