def solve(board, direction):
    """
    Solves the board as if it were collapsing from left to right
    """

    # Rotate so we're collapsing in the right direction
    if direction == 3:
        board = rotate(board, 3)
    elif direction == 0:
        board = rotate(board, 2)
    elif direction == 1:
        board = rotate(board, 1)

    # Start at top right, going right to left, row by row
    i, j = [0, 3]

    # Continue until we've reached the last row
    while i < 4:
        # Look one poisition to the left of the current number
        p = [i, j - 1]
        curr_num = board[i][j]

        # Compare with numbers to the left
        while p[1] >= 0:
            # Number to compare our current number with
            compare = board[p[0]][p[1]]

            if curr_num == 0:
                if compare != 0:
                    # Collapse the compared number onto the 0
                    board[i][j] = compare
                    board[p[0]][p[1]] = 0


                    # Rather than moving to the next position, update the current number
                    # (it's been collapsed onto where our 0 was)                  
                    curr_num = board[i][j]
                    p = [i, j] # Set our pointer to the current number as it will be moved left after this 
            elif compare == curr_num:
                # Collapse onto our current number
                board[i][j] = 2 * curr_num
                board[p[0]][p[1]] = 0
                break # Move onto the next position
            elif compare != 0:
                # We've reached some non-zero value that differs from our current number
                # so we cannot perform any more collapsing onto position [i][j]
                break

            p = [p[0], p[1] - 1]

        # If we've reached the end of the row, move down
        if j == 0:
            i += 1
            j = 3
        else:
            i += 0
            j += -1

    # We need to rotate our board back to the way it was given
    if direction == 3:
        board = rotate(board, 1)
    elif direction == 0:
        board = rotate(board, 2)
    elif direction == 1:
        board = rotate(board, 3)

    return board


def rotate(board, times):
    """
    Performs some funky rotation using zips and stuff
    https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    """
    for i in range(times):
        board = list(zip(*board[::-1]))

    return [[x for x in row] for row in board] 



def main():
    board = []

    for i in range(4):
        board.append(list(map(int, input().split())))

    direction = int(input())

    board = solve(board, direction)

    for row in board:
        print(" ".join([str(x) for x in row]))
        

if __name__ == "__main__":
    main()

