def display_board(board):

	print('\n' * 100)
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')

# This function is used to print the actual tic tac toe playing board. Each position for a potential X or O
# is represented by the list board followed by the index position in []


def player_input():

	marker = ''

	while marker != "X" and marker != "O":
		marker = input("Player 1 would you like X or O? ").upper()

		if marker == 'X':
			return ('X', 'O')
		else:
			return ('O', 'X')

# This function is used at the beginning to determine which mark each player wants to be


def place_marker(board, marker, position):

	board[position] = marker

# This function associates the marker (either an X or an O) with a position on the tic tac toe board.


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the top
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# This function lists all the possibilities for a victory (3 in a row either up and down, left to right, or diagnol)


import random

def choose_first():

	num = random.randint(1, 2)
	if num == 1:
		return "Player 1 will go first"
	else:
		return "Player 2 will go first"

# This function is used to randomly decide which player goes first


def space_check(board, position):

	return (board[position] == ' ')

# This function returns True if the board position number you enter is empty


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# This function returns True if all the slots are full, otherwise it returns False


def player_choice(board):

	position = 0

	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		position = int(input("Enter your next position (1-9): "))

	return position

# This function asks the user for their next slot if they didn't enter a correct number or the slot is already full


def replay():

	replay = input("Would you like to play agin? (Yes/No) ").title()

	if replay == "Yes":
		return True
	else:
		return False

# This last function asks the user if they want to play again or not, returning True if they do. 





# This is where the game is running 

print('Welcome to Tic Tac Toe!')

while True:

	# First we make a list with empty slots, showing all the availabilities for a marker to be placed
	the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

	# In our player_input() function, we return a tuple of ('X', 'O') or vice versa, so this associates player1 with the first item, and player2 with the second
	player1_marker, player2_marker = player_input()

	# Making a variable called turn equal to our function choose first, which will randomly decide who goes first. 
	turn = choose_first()
	print(turn)

	# This is used to start the actual game after it has been decided who goes first
	play_game = input("Ready to play? ")
	if play_game[0].lower() == 'y':
		game_on = True
	else:
		game_on = False


	# Tic Tac Toe running here

	while game_on:

		# This is referencing our previously made variable turn, if it equaled Player1 then player1 is going first. 
		if turn == "Player 1 will go first":

			# We're going to display the board each time
			display_board(the_board)

			# We make a variable called position equal to the players choice on the board
			position = player_choice(the_board)

			# We then use our place_marker function to place the players selected marker on their position
			place_marker(the_board, player1_marker, position)

			# We use this to decide if the player has won or tied
			if win_check(the_board, player1_marker):
				display_board(the_board)
				print("Player 1 has won!")
				game_on = False

			else:
				if full_board_check(the_board):
					display_board()
					print("Tie game!")
					game_on = False
				else:
					turn = "Player 2 will go first"




		else:

			if turn == "Player 2 will go first":

				display_board(the_board)

				position = player_choice(the_board)

				place_marker(the_board, player2_marker, position)

				if win_check(the_board, player2_marker):
					display_board(the_board)
					print("Player 2 has won!")
					game_on = False

				else:
					if full_board_check(the_board):
						display_board()
						print("Tie game!")
						game_on = False
					else:
						turn = "Player 1 will go first"



	if not replay():
		break