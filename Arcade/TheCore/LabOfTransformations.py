'''
Given a character, check if it represents an odd digit, an even digit or not a digit at all.
*Example:
For symbol = '5', the output should be characterParity(symbol) = "odd";
For symbol = '8', the output should be characterParity(symbol) = "even";
For symbol = 'q', the output should be characterParity(symbol) = "not a digit".
'''
def characterParity(symbol):
    if symbol.isdigit():
        if int(symbol)%2:
            return 'odd'
        else:
            return 'even'
    else:
        return 'not a digit'

'''
Define an alphabet reflection as follows: a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ..., z turns into a.
Define a string reflection as the result of applying the alphabet reflection to each of its characters.
Reflect the given string.
*Example:
For inputString = "name", the output should be reflectString(inputString) = "mznv".
'''
def reflectString(inputString):
    s = string.ascii_lowercase
    t = s[::-1]
    out = ''
    for i in inputString:
        for j, k in enumerate(s):
            if i == k:
                out += t[j]
    return out

'''
Your Informatics teacher at school likes coming up with new ways to help you understand the material. When you started studying numeral systems, he introduced his own numeral system, which he's convinced will help clarify things. His numeral system has base 26, and its digits are represented by English capital letters - A for 0, B for 1, and so on.
The teacher assigned you the following numeral system exercise: given a one-digit number, you should find all unordered pairs of one-digit numbers whose values add up to the number.
*Example:
For number = 'G', the output should be newNumeralSystem(number) = ["A + G", "B + F", "C + E", "D + D"].
Translating this into the decimal numeral system we get: number = 6, so it is ["0 + 6", "1 + 5", "2 + 4", "3 + 3"].
'''
def newNumeralSystem(number):
    s = string.ascii_uppercase
    index = s.index(number)
    return [s[i] + ' + ' + s[index - i] for i in range(index//2+1)]

'''
You've intercepted an encrypted message, and you are really curious about its contents. You were able to find out that the message initially contained only lowercase English letters, and was encrypted with the following cipher:
Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25, respectively.
The number corresponding to the ith letter of the encrypted message is then equal to the sum of numbers corresponding to the first i letters of the initial unencrypted message modulo 26.
Now that you know how the message was encrypted, implement the algorithm to decipher it.
*Example:
For message = "taiaiaertkixquxjnfxxdh", the output should be cipher26(message) = "thisisencryptedmessage".
The initial message "thisisencryptedmessage" was encrypted as follows:
letter 0: t -> 19 -> t;
letter 1: th -> (19 + 7) % 26 -> 0 -> a;
letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
etc.
'''
def cipher26(message):
    l1, l2 = list(range(26)), string.ascii_lowercase
    d = dict(zip(l2, l1))
    s = message[0]
    for i in message[1:]:
        a = len(s)
        for j in range(a+1):
            all_s = [d[k] for k in s]
            s_next = d[i] + 26*j - sum(all_s)
            if s_next in range(26):
                s_next_str = l2[s_next]
                break
        s += s_next_str
    return s

'''
When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a note with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.
The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.
*Example:
For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be stolenLunch(note) = "you'll never guess it: 2390".
'''
def stolenLunch(note):

    s = 'abcdefghij'
    out = note[:]
    for i in range(len(note)):
        if note[i].isdigit():
            out = out[:i] + s[int(note[i])] + out[i+1:]
        else:
            if note[i] in s:
                out = out[:i] + str(s.find(note[i])) + out[i+1:]
    return out
    
'''
Given two version strings composed of several non-negative decimal fields separated by periods ("."), both strings contain equal number of numeric fields. Return true if the first version is higher than the second version and false otherwise.
The syntax follows the regular semver ordering rules:
1.0.5 < 1.1.0 < 1.1.5 < 1.1.10 < 1.2.0 < 1.2.2
< 1.2.10 < 1.10.2 < 2.0.0 < 10.0.0
There are no leading zeros in any of the numeric fields, i.e. you do not have to handle inputs like 100.020.003 (it would instead be given as 100.20.3).
*Example:
For ver1 = "1.2.2" and ver2 = "1.2.0", the output should be higherVersion(ver1, ver2) = true;
For ver1 = "1.0.5" and ver2 = "1.1.0", the output should be higherVersion(ver1, ver2) = false.
'''
def higherVersion(ver1, ver2):

    for i, j in zip(ver1.split('.'), ver2.split('.')):
        if int(i) > int(j):
            return True
        elif int(i) < int(j):
            return False
    else:
        return False

'''
Consider the following ciphering algorithm:
For each character replace it with its code.
Concatenate all of the obtained numbers.
Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.
Note: here the character's code means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.
*Example:
For cipher = "10197115121", the output should be decipher(cipher) = "easy".
Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and charCode('y') = 121.
'''
def decipher(cipher):
    s, i = [], 0
    while i + 2 <= len(cipher):
        a = cipher[i:i+2]
        if i+3 <= len(cipher):
            b = cipher[i:i+3]
        if int(a) in range(97, 123):
            s.append(int(a))
            i = i + 2 
        elif int(b) in range(97, 123):
            s.append(int(b))
            i = i + 3
    return ''.join(chr(i) for i in s)
