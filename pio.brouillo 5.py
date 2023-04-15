import tkinter as tk 
import random 

widow=tk.Tk()
widow.title('game')

# Set up the game board
board = [[0 for x in range(4)] for y in range(4)]

# Add a new tile to the board
def add_tile():
    # Find all the empty spots on the board
    empty_spots = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_spots.append((i, j))

    # Choose a random empty spot
    if empty_spots:
        x, y = random.choice(empty_spots)
        # Put a 2 in the spot
        board[x][y] = 2

# Start the game
def game():
    # Add the first two tiles
    add_tile()
    add_tile()

    # Display the initial board
    display_board()

    while check_game_over() == False:
        # Get the user's move
        move = input("Enter your move (left, right, up, down): ")
        # Process the move
        if move == "left":
            shift_left()
        elif move == "right":
            shift_right()
        elif move == "up":
            shift_up()
        elif move == "down":
            shift_down()

        # Add a new tile
        add_tile()

        # Display the updated board
        display_board()

    # Game over
    print("Game over!")

# Display the game board
def display_board():
    for i in range(4):
        for j in range(4):
            print(board[i][j], end="\t")
        print()

# Shift everything to the left
def shift_left():
    for i in range(4):
        for j in range(3):
            # If the current spot is not empty
            if board[i][j] != 0:
                # Check if the next spot is empty
                if board[i][j+1] == 0:
                    # Move the tile to the next spot
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
                # Check if the next spot has the same value
                elif board[i][j] == board[i][j+1]:
                    # Merge the two tiles
                    board[i][j+1] = 2
                    board[i][j] = 0

# Shift everything to the right
def shift_right():
    for i in range(4):
        for j in range(3, 0, -1):
            # If the current spot is not empty
            if board[i][j] != 0:
                # Check if the next spot is empty
                if board[i][j-1] == 0:
                    # Move the tile to the next spot
                    board[i][j-1] = board[i][j]
                    board[i][j] = 0
                # Check if the next spot has the same value
                elif board[i][j] == board[i][j-1]:
                    # Merge the two tiles
                    board[i][j-1]= 2
                    board[i][j] = 0

# Shift everything up
def shift_up():
    for i in range(3):
        for j in range(4):
            # If the current spot is not empty
            if board[i][j] != 0:
                # Check if the next spot is empty
                if board[i+1][j] == 0:
                    # Move the tile to the next spot
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                # Check if the next spot has the same value
                elif board[i][j] == board[i+1][j]:
                    # Merge the two tiles
                    board[i+1][j] *= 2
                    board[i][j] = 0
                                  
# Shift everything down
def shift_down():
    for i in range(3, 0, -1):
        for j in range(4):
            # If the current spot is not empty
            if board[i][j] != 0:
                # Check if the next spot is empty
                if board[i-1][j] == 0:
                    # Move the tile to the next spot
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                # Check if the next spot has the same value
                elif board[i][j] == board[i-1][j]:
                    # Merge the two tiles
                    board[i-1][j] *= 2
                    board[i][j] = 0

# Check if the game is over
def check_game_over():
    # Check if any spots are empty
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False

    # Check if any tiles can be merged horizontally
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return False

    # Check if any tiles can be merged vertically
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j]:
                return False

    # Game is over
    return True

widow.mainloop()