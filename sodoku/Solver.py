class Sudoku:
    def __init__(self, board):
        if isinstance(board, str):
            self.board = self.from_string(board)
        else:
            self.board = board

    @staticmethod
    def from_string(board_str):
        """Converts a string representation of a board into a list of lists."""
        return [[int(c) for c in board_str[i:i+9]] for i in range(0, 81, 9)]

    def is_valid(self, row, col, num):
        """Check if a number is valid in the current row, column, and 3x3 subgrid."""
        # Check the row and column in one loop to reduce redundant iterations
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # Check the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        """Solve the Sudoku puzzle using backtracking."""
        # Find an empty cell (represented by 0)
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    # Try numbers 1 to 9
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            
                            if self.solve():
                                return True
                            
                            self.board[row][col] = 0  # Backtrack
                    return False
        return True

    def __str__(self):
        """Returns a formatted string representation of the Sudoku board."""
        lines = []
        for i, row in enumerate(self.board):
            line = " ".join(str(num) if num != 0 else "." for num in row)
            lines.append(line)
            if i % 3 == 2 and i != 8:
                lines.append("-" * 21)  # Add grid lines for readability
        return "\n".join(lines)


def prompt_user_input():
    """Prompts the user to input the Sudoku board row by row."""
    board = []
    print("Enter the Sudoku board (use 0 for empty cells), one row at a time:")
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            # Validate row length and content
            if len(row) == 9 and all(c.isdigit() for c in row):
                board.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9).")
    return ''.join(board)


# Get the Sudoku puzzle from user input
puzzle_str = prompt_user_input()

# Create a Sudoku instance and solve the puzzle
sudoku = Sudoku(puzzle_str)

# Solve and display the result
if sudoku.solve():
    print("Solved Sudoku:")
    print(sudoku)
else:
    print("No solution exists!")
