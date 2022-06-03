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


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:

            print("- - - - - - - - - - - -")
            # seperating in the blocks of 3x3
            # i, j != 0 to avoid the situation of the line in the start
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]), end=" ")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def valid(bo, num, pos):
    # checking rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # checking cols
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    # checking boxes
    X_box = pos[1] // 3
    Y_box = pos[0] // 3
    for i in range(Y_box*3, Y_box*3 + 3):
        for j in range(X_box*3, X_box*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


print_board(board)
print("___________________________________")
solve(board)
print_board(board)
