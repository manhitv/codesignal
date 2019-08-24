'''
Given a string, enclose it in round brackets.
*Example:
For inputString = "abacaba", the output should be encloseInBrackets(inputString) = "(abacaba)".
'''
def encloseInBrackets(inputString):
    return '(' + inputString + ')'

'''
Proper nouns always begin with a capital letter, followed by small letters.
Correct a given proper noun so that it fits this statement.
*Example:
For noun = "pARiS", the output should be properNounCorrection(noun) = "Paris";
For noun = "John", the output should be properNounCorrection(noun) = "John".
'''
def properNounCorrection(noun):
    return noun[0].upper() + noun[1:].lower()

'''
Determine whether the given string can be obtained by one concatenation of some string to itself.
*Example:
For inputString = "tandemtandem", the output should be isTandemRepeat(inputString) = true;
For inputString = "qqq", the output should be isTandemRepeat(inputString) = false;
For inputString = "2w2ww", the output should be isTandemRepeat(inputString) = false.
'''
def isTandemRepeat(inputString):
    l = len(inputString)
    for i in range(1, l):
        if inputString[:i] == inputString[i:]:
            return True
    return False

'''
Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.
*Example:
For inputString = "AaBaa", the output should be isCaseInsensitivePalindrome(inputString) = true.
"aabaa" is a palindrome as well as "AABAA", "aaBaa", etc.
For inputString = "abac", the output should be isCaseInsensitivePalindrome(inputString) = false.
All the strings which can be obtained via changing case of some group of letters, i.e. "abac", "Abac", "aBAc" and 13 more, are not palindromes.
'''
def isCaseInsensitivePalindrome(inputString):
    return inputString.lower()==inputString.lower()[::-1]

'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").
The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.
Given a valid email address, find its domain part.
*Example:
For address = "prettyandsimple@example.com", the output should be findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be findEmailDomain(address) = "codesignal.com".
'''
def findEmailDomain(address):
    return address.split('@')[-1]

'''
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.
Given the starting HTML tag, find the appropriate end tag which your editor should propose.
If you are not familiar with HTML, consult with this note.
*Example:
For startTag = "<button type='button' disabled>", the output should be htmlEndTagByStartTag(startTag) = "</button>";
For startTag = "<i>", the output should be htmlEndTagByStartTag(startTag) = "</i>".
'''
def htmlEndTagByStartTag(startTag):
    a = startTag.split(' ')[0]
    if len(a) == len(startTag):
        return '</' + a[1:]
    else:
        return '</' + a[1:] + '>'

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
    for i in range(len(inputString)):
        x = inputString[i]
        if i%3 == 2 and x != '-':
            return False
        if i%3 != 2 and not x.isdigit() and x not in b:
            return False
        if inputString[-1] == '-':
            return False
    return True
