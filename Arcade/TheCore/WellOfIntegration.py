'''
A boy is walking a long way from school to his home. To make the walk more fun he decides to add up all the numbers of the houses that he passes by during his walk. Unfortunately, not all of the houses have numbers written on them, and on top of that the boy is regularly taking turns to change streets, so the numbers don't appear to him in any particular order.
At some point during the walk the boy encounters a house with number 0 written on it, which surprises him so much that he stops adding numbers to his total right after seeing that house.
For the given sequence of houses determine the sum that the boy will get. It is guaranteed that there will always be at least one 0 house on the path.
*Example:
For inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2], the output should be houseNumbersSum(inputArray) = 11.
The answer was obtained as 5 + 1 + 2 + 3 = 11.
'''
def houseNumbersSum(a):
    if a[0] == 0:
        return 0
    i = a.index(0)
    return sum(a[:i])

'''
Given an array of strings, return another array containing all of its longest strings.
*Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''
def allLongestStrings(inputArray):
    max_l = max([len(i) for i in inputArray])
    return [j for j in inputArray if len(j) == max_l]

'''
There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house sorted in ascending order. It's guaranteed that each person has 2 legs and each cat has 4 legs.
*Example:
For legs = 6, the output should be houseOfCats(legs) = [1, 3].
There could be either 1 cat and 1 person (4 + 2 = 6) or 3 people (2 * 3 = 6).
For legs = 2, the output should be houseOfCats(legs) = [1].
There can be only 1 person.
'''
def houseOfCats(legs):
    if legs%2:
        return 0
    m = legs//2
    return [i for i in range(m+1) if (legs-2*i)%4 == 0]

'''
Check whether the given string is a subsequence of the plaintext alphabet.
*Example:
For s = "effg", the output should be alphabetSubsequence(s) = false;
For s = "cdce", the output should be alphabetSubsequence(s) = false;
For s = "ace", the output should be alphabetSubsequence(s) = true;
For s = "bxz", the output should be alphabetSubsequence(s) = true.
'''
def alphabetSubsequence(s):
    return list(s)==sorted(list(set(s)))

'''
You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.
The coin values available in Bananaland are stored in a sorted array coins. coins[0] = 1, and for each i (0 < i < coins.length) coins[i] is divisible by coins[i - 1]. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's price.
*Example:
For coins = [1, 2, 10] and price = 28, the output should be minimalNumberOfCoins(coins, price) = 6.
You have to use 10 twice, and 2 four times.
'''
def minimalNumberOfCoins(coins, price):
    a = 0
    for i in range(len(coins)-1, -1, -1):
        a += price//coins[i]
        price = price - price//coins[i]*coins[i]
    return a

'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
*Example:
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''
def addBorder(picture):
    a = len(picture[0])
    return ['*'*(a+2)] + ['*' + i + '*' for i in picture] + ['*'*(a+2)]

'''
N candles are placed in a row, some of them are initially lit. For each candle from the 1st to the Nth the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?
*Example:
For a = [1, 1, 1, 1, 1], the output should be switchLights(a) = [0, 1, 0, 1, 0].
Check out the image below for better understanding:
For a = [0, 0], the output should be switchLights(a) = [0, 0].
The candles are not initially lit, so their states are not altered by the algorithm.
'''
def switchLights(a):
    for i in range(len(a)):
        if a[i]%2:
            a[i] += 1
            a[:i] = [j+1 for j in a[:i]]
    return [i%2 for i in a]

'''
Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer than maxLength, he simply skipped it and read on.
Help the teacher figure out how many words the boy has read by calculating the number of words in the text he has read, no longer than maxLength.
Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.
*Example:
For maxLength = 4 and text = "The Fox asked the stork, 'How is the soup?'",
the output should be timedReading(maxLength, text) = 7.
The boy has read the following words: "The", "Fox", "the", "How", "is", "the", "soup".
'''
def timedReading(maxLength, text):
    import re 
    s = re.split('[^a-zA-Z]',text)
    return len([x for x in s if 1 <= len(x) <= maxLength])
        
'''
Elections are in progress!
Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.
The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.
*Example:
For votes = [2, 3, 5, 2] and k = 3, the output should be electionsWinners(votes, k) = 2.
The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
The last candidate can't win no matter what (for the same reason as the first candidate).
Thus, only 2 candidates can win (the second and the third), which is the answer.
'''
def electionsWinners(votes, k):
    m = max(votes)
    if k == 0 and votes.count(m) == 1:
        return 1
    return len([i for i in votes if i+k > m])

'''
Given a positive integer number and a certain length, we need to modify the given number to have a specified length. We are allowed to do that either by cutting out leading digits (if the number needs to be shortened) or by adding 0s in front of the original number.
*Example:
For number = 1234 and width = 2, the output should be integerToStringOfFixedWidth(number, width) = "34";
For number = 1234 and width = 4, the output should be integerToStringOfFixedWidth(number, width) = "1234";
For number = 1234 and width = 5, the output should be integerToStringOfFixedWidth(number, width) = "01234".
'''
def integerToStringOfFixedWidth(number, width):
    l = len(str(number))
    if width > l:
        return (width - l)*'0' + str(number)
    else:
        return str(number)[l-width:]

'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.
*Example:
For a = [1, 2, 3] and b = [1, 2, 3], the output should be areSimilar(a, b) = true.
The arrays are equal, no need to swap any elements.
For a = [1, 2, 3] and b = [2, 1, 3], the output should be areSimilar(a, b) = true.
We can obtain b from a by swapping 2 and 1 in b.
For a = [1, 2, 2] and b = [2, 1, 1], the output should be areSimilar(a, b) = false.
Any swap of any two elements either in a or in b won't make a and b equal.
'''
def areSimilar(a, b):
    d = [{i, j} for i, j in zip(a, b) if i!=j]
    return len(d) == 0 or len(d) == 2 and d[0] == d[1]

'''
Consider two following representations of a non-negative integer:
A simple decimal integer, constructed of a non-empty sequence of digits from 0 to 9;
An integer with at least one digit in a base from 2 to 16 (inclusive), enclosed between # characters, and preceded by the base, which can only be a number between 2 and 16 in the first representation. For digits from 10 to 15 characters a, b, ..., f and A, B, ..., F are used.
Additionally, both representations may contain underscore (_) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.
Your task is to determine whether the given string is a valid integer representation.
Note: this is how integer numbers are represented in the programming language Ada.
*Example:
For line = "123_456_789", the output should be adaNumber(line) = true;
For line = "16#123abc#", the output should be adaNumber(line) = true;
For line = "10#123abc#", the output should be adaNumber(line) = false;
For line = "10#10#123ABC#", the output should be adaNumber(line) = false;
For line = "10#0#", the output should be adaNumber(line) = true;
For line = "10##", the output should be adaNumber(line) = false.
'''
def adaNumber(line):
    
    # Remove _
    line = line.replace('_','')
    if '#' not in line:
        return line.isdigit()
    else:
        if line.count('#') != 2:
            return False
    
    line = line.split('#')
    
    if not line[0].isdigit() or line[1] == '':
        return False
    elif int(line[0]) not in range(2, 17):
        return False

    if int(line[0]) in range(2, 11):
        for i in line[1]:
            if not i.isdigit():
                return False
            elif not 0 <= int(i) <= int(line[0]) - 1:
                return False
    
    if int(line[0]) in range(11, 17):
        for i in line[1]:
            if not ('0' <= i <= '9' or 'a' <= i <= chr(int(line[0])-11+ord('a')) or 'A' <= i <= chr(int(line[0])-11+ord('A'))):
                return False
    
    return True
