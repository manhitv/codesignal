'''
Determine if the given character is a digit or not.
*Example:
For symbol = '0', the output should be isDigit(symbol) = true;
For symbol = '-', the output should be isDigit(symbol) = false.
'''
def isDigit(symbol):

    return symbol.isdigit()

'''
Given a string, return its encoding defined as follows:
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
*Example:
For s = "aabbbc", the output should be lineEncoding(s) = "2a3bc".
'''
def lineEncoding(s):

    i = 0
    nw = ""
    while i < len(s):
        ct = 1
        v = s[i]
        if i < len(s)-1 and s[i] == s[i + 1]:
            while i < len(s) -1 and s[i] == s[i+1]:
                ct += 1
                i += 1
            nw += str(ct) + v
        else:
            nw += v
        i += 1
    return nw
            
'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. 
*Example:
For cell = "a1", the output should be chessKnight(cell) = 2.
For cell = "c2", the output should be chessKnight(cell) = 6.
'''
def chessKnight(cell):

    m = cell[0]
    n = int(cell[1])
    if m in ['a', 'h']: #first quater
        if n in [1, 8]:
            return 2
        elif n in [2, 7]:
            return 3
        else:
            return 4
    elif m in ['b', 'g']:
        if n in [1, 8]:
            return 3
        elif n in [2, 7]:
            return 4
        else:
            return 6
    elif m in ['c','d','e','f']:
        if n in [1, 8]:
            return 4
        elif n in [2, 7]:
            return 6
        else:
            return 8
    
'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
*Example:
For n = 152, the output should be deleteDigit(n) = 52;
For n = 1001, the output should be deleteDigit(n) = 101.
'''
def deleteDigit(n):
    l, r = [int(i) for i in str(n)], [int(i) for i in str(n)] 
    a = []
    for i in range(len(l)):
        r.remove(l[i])
        a.append(int(''.join([str(j) for j in r])))
        r = [int(i) for i in str(n)]
    return max(a)
