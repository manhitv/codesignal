'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
*Example:
For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.
There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.
For a = [2, 2], the output should be firstDuplicate(a) = 2;
For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.
'''
def firstDuplicate(a):
    
    i = 0
    while i < len(a):
        if a[i] > len(a):
            return -1
        if a[abs(a[i])-1] < 0:
            return abs(a[i])
        else:
            a[abs(a[i])-1] = a[abs(a[i])-1] * -1
        i+=1
    return -1

'''
Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
*Example:
For s = "abacabad", the output should be firstNotRepeatingCharacter(s) = 'c'.
There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
For s = "abacabaabacaba", the output should be firstNotRepeatingCharacter(s) = '_'.
There are no characters in this string that do not repeat.
'''
def firstNotRepeatingCharacter(s):
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return s[i]
    else:
        return "_"

'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.
Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
*Example:
For
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be sudoku2(grid) = true;
For
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be sudoku2(grid) = false.
The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
'''
def sudoku2(grid):

    def check_list(a):
        if len(a) != 0:
            if sorted(a) != sorted(list(set(a))) or max(a) > 9 or min(a) < 1:
                return False
    
    for i in range(9):
        # horizontal check
        l1 = [int(m) for m in grid[i] if m.isdigit()]
        c = []
        for j in range(9):
            if grid[j][i].isdigit():
                c.append(int(grid[j][i]))
        # vertical check
        if check_list(l1) == 0 or check_list(c) == 0:
            return False
        # 3x3 check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b = []
            for m in range(i, i+3):
                for n in range(j, j+3):
                    if grid[m][n].isdigit():
                        b.append(int(grid[m][n]))
            if check_list(b) == 0:
                return False
    return True
