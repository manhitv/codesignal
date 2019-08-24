'''
Given an array of strings, return another array containing all of its longest strings.
*Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''
def allLongestStrings(inputArray):
    a = [len(strs) for strs in inputArray]
    b = []
    for ele in inputArray:
        if len(ele) == max(a):
            b.append(ele)
    return b
            
'''        
Given two strings, find the number of common characters between them.
*Example:
For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
'''
def commonCharacterCount(s1, s2):
    count = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(count)

'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
*Example:
For n = 1230, the output should be isLucky(n) = true;
For n = 239017, the output should be isLucky(n) = false.
'''
def isLucky(n):
    s = str(n)
    l = len(s)//2
    sum1, sum2 = 0, 0
    for i in range(l):
        sum1 += int(s[i])
    for j in range(l, len(s)):
        sum2 += int(s[j])
    if sum1 == sum2:
        return True
    else:
        return False

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
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.
*Example:
For inputString = "(bar)", the output should be reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''
def reverseInParentheses(inputString):
    s = inputString
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
