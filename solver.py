
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def solve(bo):
    """recursive function that solves the board using backtracking"""

    find = find_empty()  

    # if no empty boxes left --> returns True i.e board is solved  
    if not find:
        return True
    else:
        row, col = find


    for i in range(1,10): 
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo): #recursion
                return True
            
            bo[row][col] = 0 #reseting to zero if no solution

    return False

def is_valid(bo, num, pos):
    """to check whether our move is valid or not"""
    # pos --> (i,j) from find_empty ; bo --> board (2D list)

    #check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i: #<--
            return False
        
    #check box
    box_r = pos[0] // 3
    box_c = pos[1] // 3

    for i in range(box_r*3, box_r*3 + 3):
        for j in range(box_c*3, box_c*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
            
    return True

def find_empty(bo):
    """finds the empty spaces (zeros in our board)"""

    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return(i,j)
            
    return None #<--


def print_board(bo):
    """prints sudoku board with appropriate spaces"""

    for i in range(9):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")

            if j!=8:
                print(str(bo[i][j]) + " ", end="")

            else:
                print(bo[i][j], end="\n")

print_board(board)