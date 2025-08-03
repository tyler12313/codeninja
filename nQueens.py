def create_board(size):
    board = []
    for i in range(size):
        row = [0] * size
        board.append(row)

    return board

def print_board(board):
    symbols = {0:' ⬜',1:' ♜',2:' ♗',3:' 👑'}
    for row in board:
        print(''.join(symbols[x] for x in row))
    print()

def solve_rooks_simple(board,col):
    
    size = len(board)

    if col >= size:
        print("FOund a solution!")
        print_board(board)
        return True

    print(f"Working on column{col}")

    for row in range(size):
        print(f" Trying to place rook at row{row}, col{col}")
        
        if is_rook_safe(board, row, col):
            board[row][col] = 1
            print(f" Placed rook at ({row},{col})")
            print_board(board)

            if solve_rooks_simple(board, col +1):
                return True
            
            board[row][col] = 0
            print(f" Removed rook from ({row},{col}) - didnt work")
            print_board(board)
        else:
            print(f" Can't place at ({row},{col}), not safe")

    print(f"No solution found for column {col}")
    return False

def is_rook_safe(board,row,col):

    size = len(board)
    for c in range(size):
        if board[row][c] == 3:
            return False
    return True



def solve_bishops_simple(board,col):
    
    size = len(board)

    if col >= size:
        print("FOund a solution!")
        print_board(board)
        return True

    print(f"Working on column{col}")

    for row in range(size):
        print(f" Trying to place bishop at row{row}, col{col}")
        
        if is_bishop_safe(board, row, col):
            board[row][col] = 3
            print(f" Placed bishop at ({row},{col})")
            print_board(board)

            if solve_bishops_simple(board, col +1):
                return True
            
            board[row][col] = 0
            print(f" Removed bishop from ({row},{col}) - didnt work")
            print_board(board)
        else:
            print(f" Can't place at ({row},{col}), not safe")

    print(f"No solution found for column {col}")
    return False

def is_bishop_safe(board,row,col):

    size = len(board)

    r,c = row-1, col+1
    while r >= 0 and c < size:
        if board[r][c] == 3:
            return False
        r -= 1
        c += 1

    r,c = row-1, col-1
    while r >= 0 and c >= 0:
        if board[r][c] == 3:
            return False
        r -= 1
        c -= 1

    r,c = row+1, col+1
    while r < size and c < size:
        if board[r][c] == 3:
            return False
        r += 1
        c += 1

    r,c = row+1, col-1
    while r < size and c >= 0:
        if board[r][c] == 3:
            return False
        r += 1
        c -= 1

    return True

    return True

def solve_queens_simple(board,row,col):
    
    size = len(board)

    if col >= size:
        print("FOund a solution!")
        print_board(board)
        return True

    print(f"Working on column{col}")

    for row in range(size):
        print(f" Trying to place queen at row{row}, col{col}")
        
        if is_queen_safe(board, row, col):
            board[row][col] = 3
            print(f" Placed queen at ({row},{col})")
            print_board(board)

            if solve_queens_simple(board, 0, col+1):
                return True
            
            board[row][col] = 0
            print(f" Removed queen from ({row},{col}) - didnt work")
            print_board(board)
        else:
            print(f" Can't place at ({row},{col}), not safe")

    print(f"No solution found for column {col}")
    return False

def is_queen_safe(board,row,col):

    if is_rook_safe(board,row,col) and is_bishop_safe(board,row,col):
        return True
    
    return False

board = create_board(17)
print_board

solve_queens_simple(board,0,0)
