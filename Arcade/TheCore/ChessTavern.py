'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.
The bishop has no restrictions in distance for each move, but is limited to diagonal movement. 
*Example:
For bishop = "a1" and pawn = "c3", the output should be bishopAndPawn(bishop, pawn) = true.
For bishop = "h1" and pawn = "h3", the output should be bishopAndPawn(bishop, pawn) = false.
'''
def bishopAndPawn(bishop, pawn):

    d = dict((enumerate(string.ascii_lowercase)))
    d1, d2 = 0, 0
    for key, value in d.items():
        if value == bishop[0]:
            d1 = key
        if value == pawn[0]:
            d2 = key
    return abs(d1 - d2) == abs(int(bishop[1]) - int(pawn[1]))

'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
*Example:
For cell = "a1", the output should be chessKnightMoves(cell) = 2.
For cell = "c2", the output should be chessKnightMoves(cell) = 6.
'''
def chessKnightMoves(cell):

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
