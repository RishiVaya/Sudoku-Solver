# Sudoku solver which uses backtracking algorithm.

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return [row, col]
    return None

def printer(board):
    for row in range(len(board)):
        if row % 3 == 0:
            print("-------------------------------------")

        for col in range(len(board[0])):
            if col % 3 == 0:
                print("| ", end = " ")
            
            print (board[row][col], end = "  ")
        print("|")
    print("-------------------------------------")

def is_valid(board, value, position):

    for i in board[position[0]]:
        if i == value:
                return False

    for i in board:
        if i[position[1]] == value:
                return False

    for i in range((position[0] // 3) * 3, ((position[0] // 3) * 3) + 3 ):
        for x in range((position[1] // 3) * 3, ((position[1] // 3) * 3) + 3 ):
            if board[i][x] == value:
                return False
    
    return True

def backtrack_solver(board):
    new_empty = find_empty(board)
    if new_empty == None:
        return True
    
    for i in range(1, 10):
        if is_valid(board, i, new_empty):
            board[new_empty[0]][new_empty[1]] = i

            if backtrack_solver(board):
                return True

        board[new_empty[0]][new_empty[1]] = 0
    
    return False


puzzle = [[0, 7, 0, 0, 0, 2, 0, 0, 0],
          [0, 9, 0, 3, 7, 0, 0, 0, 0],
          [0, 0, 5, 0, 8, 0, 0, 0, 1],
          [0, 0, 4, 7, 0, 0, 0, 0, 9],
          [0, 0, 0, 0, 9, 6, 0, 0, 0],
          [0, 0, 0, 0, 0, 8, 6, 5, 4],
          [0, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 4, 3],
          [4, 0, 7, 9, 5, 0, 2, 6, 0],
            ]

print("TO SOLVE") 
printer(puzzle)
print(is_valid(puzzle, 7, [0, 0]))
print("SOLVED")
backtrack_solver(puzzle)
printer(puzzle)