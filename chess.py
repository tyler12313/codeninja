import math
def create_board(size):
    board = []
    for i in range(size):
        row = [0] * size
        board.append(row)

    return board
               

def print_board(board):

    symbols = {
        0: '⬜',
        1: '♖',
        2: '♗',
        3: '👑'
    }

    for row in board:
        for square in row:
            print(symbols[square], end=' ')
        print()

def is_rook_safe(board,row,col):
    size = len(board)

    for c in range(size):
        if board[row][c] == 1 and c != col:
            return False
    
    for r in range(size):
        if board[r][col] == 1 and r != row:
            return False
        
    return True

def place_rook(board, row, col):
    if is_rook_safe(board,row,col):
        board[row][col] = 1
        print(f"\nPlaced rook at position ({row},{col})")
        return True
    print(f"\nCannot place rook at ({row},{col}) - it would be under attack!")
    return False

def is_bishop_safe(board,row,col):
    size = len(board)
    r,c = row-1, col+1
    while r >= 0 and c < size:
        if board[r][c] == 2:
            return False
        r -= 1
        c += 1

    r,c = row-1, col-1
    while r >= 0 and c >= 0:
        if board[r][c] == 2:
            return False
        r -= 1
        c -= 1

    r,c = row+1, col+1
    while r < size and c < size:
        if board[r][c] == 2:
            return False
        r += 1
        c += 1

    r,c = row+1, col-1
    while r < size and c >= 0:
        if board[r][c] == 2:
            return False
        r += 1
        c -= 1

    return True

def place_bishop(board,row,col):
    if is_bishop_safe(board,row,col):
        board[row][col] = 2
        print(f"\nPlaced bishop at position ({row},{col})")
        return True
    print(f"\nCannot place bishop at ({row},{col})- it would be under attack!")
    return False

board = create_board(4)
print_board(board)
print("empty 4x4 board")
place_bishop(board,0,0)
print_board(board)
place_rook(board,0,1)
print_board(board)

for i in range(size):
    size = len(board)
    solrow = 0
    solcol = 0

    place_rook(board,solrow,solcol)
    solrow += 1
    for i in range(math.sqrt(size)):
        solcol += 1
