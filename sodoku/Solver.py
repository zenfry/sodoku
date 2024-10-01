class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check the row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check the column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        # Find an empty cell
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    # Try numbers from 1 to 9
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            
                            # Recur to check if this leads to a solution
                            if self.solve():
                                return True
                            
                            # If not, reset the cell and try another number
                            self.board[row][col] = 0
                    
                    return False  # Trigger backtracking if no number fits
        return True  # Puzzle solved!

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))


def get_input_board():
    board = []
    print("Enter the Sudoku board (use 0 for empty cells), one row at a time:")
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            if len(row) == 9 and all(c in '0123456789' for c in row):
                board.append([int(c) for c in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9).")
    return board


# Get the Sudoku puzzle from user input
puzzle = get_input_board()

# Create a Sudoku instance and solve the puzzle
sudoku = Sudoku(puzzle)

if sudoku.solve():
    print("Solved Sudoku:")
    sudoku.print_board()
else:
    print("No solution exists!")
