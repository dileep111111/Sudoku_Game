import random

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(str(num) if num != 0 else '.', end=" ")
        print()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_board():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(17):  # Fill 17 random cells to start
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    return board

def main():
    while True:
        board = generate_board()
        print("Welcome to Sudoku!")
        print_board(board)
        while True:
            command = input("Enter your move (row col num) or 'quit'/'giveup' or 'solution': ")
            if command.lower() in ['quit', 'giveup']:
                print("Thanks for playing!")
                return
            elif command.lower() == 'solution':
                solve(board)
                print("Here's the solution:")
                print_board(board)
                break
            else:
                try:
                    row, col, num = map(int, command.split())
                    row -= 1
                    col -= 1 
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        print_board(board)
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter in the format 'row col num'.")
        
        while True:
            next_command = input("Do you want to continue playing? (yes/no): ")
            if next_command.lower() == 'no':
                print("Thanks for playing!")
                return
            elif next_command.lower() == 'yes':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()