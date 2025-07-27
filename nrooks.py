def create_board(size):
    board = []
    for i in range(size):
        row = [0] * size
        board.append(row)

    return board

def print_board(board):
    symbols = {0:'⬜',1:'♜'}
    for row in board:
        print(''.join(symbols[x] for x in row))
    print()

def solve_3_rooks_final(board,col):

    print("===col===:", col)
    if col >= 3:
        print("col:", col, end = "")
        print("Found a solution!")
        print_board(board)
        return True 
    
    for row in range(3):
        print("ROW", row);
        if is_safe(board,row,col):
            board[row][col] = 1
            print(f"Placing rook at row {row}, column {col}")
            print_board(board)

        if solve_3_rooks_final(board,col + 1):
            return True
        
        board[row][col] = 0
        print(f"Removing rook from row{row}, column {col}")
        print_board(board)

    return False

def is_safe(board,row,col):

    for c in range(col):
        if board[row][c] == 1:
            return False
    return True

board = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    solve_3_rooks_final(board,i)
