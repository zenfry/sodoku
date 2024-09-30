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


# Example Sudoku puzzle (0 represents empty cells)
puzzle = [
    [0, 0, 0, 0, 3, 0, 0, 2, 0],
    [0, 6, 0, 0, 0, 1, 0, 0, 3],
    [0, 0, 2, 0, 0, 0, 0, 4, 5],
    [2, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 9],
    [3, 0, 0, 0, 0, 0, 4, 0, 0],
    [5, 0, 0, 1, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0, 0, 0, 0, 0]
]

# Create a Sudoku instance and solve the puzzle
sudoku = Sudoku(puzzle)

if sudoku.solve():
    print("Solved Sudoku:")
    sudoku.print_board()
else:
    print("No solution exists!")
