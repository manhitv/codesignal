'''
A string is said to be beautiful if each letter of the alphabet appears at most as many times as than the previous letter; ie: b occurs no more times than a; c occurs no more times than b; etc.
Given a string, check whether it is beautiful.
*Example:
For inputString = "bbbaacdafe", the output should be isBeautifulString(inputString) = true;
This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.
For inputString = "aabbb", the output should be isBeautifulString(inputString) = false;
Since there are more bs than as, this string is not beautiful.
For inputString = "bbc", the output should be isBeautifulString(inputString) = false.
Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
'''
from collections import Counter

def isBeautifulString(s):
    a = Counter(s)
    b = []
    for i in string.ascii_lowercase:
        b.append(a[i])
    return b == sorted(b, reverse=True)

'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").
The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.
Given a valid email address, find its domain part.
*Example:
For address = "prettyandsimple@example.com", the output should be findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be findEmailDomain(address) = "codesignal.com".
'''
def findEmailDomain(address):
    l = address.split('@')
    return l[-1]

'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
*Example:
For st = "abcdc", the output should be buildPalindrome(st) = "abcdcba".
'''
def buildPalindrome(st):
    for i in range(len(st)):
        if st[i:][::-1] in st[i:]:
            return st + st[:i][::-1]

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
    l, c = [], 0
    a = max(votes)
    if k == 0:
        votes.remove(a)
        if a not in votes:
            return 1
        else:
            return 0
    for i in votes:
        if i+k > a:
            c += 1
    return c

'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.
The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).
Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
*Example:
For inputString = "00-1B-63-84-45-E6", the output should be isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be isMAC48Address(inputString) = false.
'''
def isMAC48Address(inputString):

    b = ['A', 'B', 'C', 'D', 'E', 'F']
    if inputString[-1] == '-':
        return False
    for i in range(len(inputString)):
        x = inputString[i]
        if i%3 == 2 and x != '-':
            return False
        if i%3 != 2 and not x.isdigit() and x not in b:
            return False
    return True
