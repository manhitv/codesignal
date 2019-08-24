'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
*Example:
For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''
def arrayReplace(inputArray, elemToReplace, substitutionElem):

    index = []
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            index.append(i)
    for i in index:
        inputArray[i] = substitutionElem
    return inputArray

'''
Check if all digits of the given integer are even.
*Example:
For n = 248622, the output should be evenDigitsOnly(n) = true;
For n = 642386, the output should be evenDigitsOnly(n) = false.
'''
def evenDigitsOnly(n):

    return all(int(i)%2 ==0 for i in str(n))

'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
Check if the given string is a correct variable name.
*Example:
For name = "var_1__Int", the output should be variableName(name) = true;
For name = "qq-q", the output should be variableName(name) = false;
For name = "2w2", the output should be variableName(name) = false.
'''
def variableName(name):
    if name[0].isdigit():
        return False
    for i in name:
        if i not in string.ascii_letters and not i.isdigit() and i != '_':
            return False
    return True

'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).
*Example:
For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
'''
def alphabeticShift(s):
    d = dict(list(enumerate(string.ascii_lowercase)))
    l = []
    for i in s:
        if i == 'z':
            l.append('a')
        for j in d.keys():
            if i == d[j] and j < 25:
                l.append(d[j+1])
    return ''.join(l)

'''    
Given two cells on the standard chess board, determine whether they have the same color or not.
*Example:
For cell1 = "A1" and cell2 = "C3", the output should be chessBoardCellColor(cell1, cell2) = true.
For cell1 = "A1" and cell2 = "H3", the output should be chessBoardCellColor(cell1, cell2) = false.
'''
def chessBoardCellColor(cell1, cell2):
    d = dict(list(enumerate(string.ascii_uppercase)))
    d1, d2 = 0, 0
    for key, value in d.items():
        if value == cell1[0]:
            d1 = key + int(cell1[1])
        if value == cell2[0]:
            d2 = key + int(cell2[1])
    return d1%2 == d2%2
