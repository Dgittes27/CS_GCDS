"""
┌───────────────────────────────────────────────────────────────────────────┐
│                            Tic Tac Toe                                    │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: David Gittes                                                        │
| Course: CS2                                                               |
| Date: October 31, 2026                                                    |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  Tic Tac Toe game against another player or another computer |
| Bonuses:                                                                  |
|   Option to play again, Keeps track of score, and option to play against  |
|    the computer                                                           |
└───────────────────────────────────────────────────────────────────────────┘
"""
import random

def display_board(board): 
    '''
    Displays the tic-tac-toe board in its present state 
    Args:
      board (list): updated list of rows and columns
    '''
    print(f'''                                         
  1   2   3
1 {board[0][0]} | {board[0][1]} | {board[0][2]}
 __________

2 {board[1][0]} | {board[1][1]} | {board[1][2]}
 __________

3 {board[2][0]} | {board[2][1]} | {board[2][2]}
''') #list of lists with rows and columns


def get_spot(x_or_o, row_or_column):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        test_number (int)
    Return:
        bool: true if test_number is an integer
    '''
    while True:
      try:
          number = int(input(f'{x_or_o}, enter a {row_or_column}: '))-1

          if number not in [0, 1, 2]:
            print(f'Please enter a valid {row_or_column} (1, 2, or 3)')
            continue
          return int(number)
      except ValueError:
              print('Enter an integer')

def get_bot_move(board):
  while True:
    r = random.randint(0,2)   #random choice of one of the rows
    c = random.randint(0,2)   #random choice of one the columns

    if board[r][c] == " ":    #if this space is open
      board[r][c] = 'O'       #fill in with O
      return board

def get_player_move(board, x_or_o):
  '''
  Takes user's desired move through a row and column and returns updated board state
  Args:
    board (list): list of rows and columns 
    x_or_o (str): indicates which player's move it is
  Return:
    board (list): updated list of rows and columns '''
  while True:
    row = get_spot(x_or_o, 'row')
    column = get_spot(x_or_o, 'column')

    if board[row][column] != ' ':
      print('Pleae enter a valid row and column (1, 2, or 3)')
      continue

    board[row][column] = x_or_o
    return board
    
     
def check_winner(board, x_or_o):
  '''
  Checks if there is a winner based on previous move
  Args:
    board (list): list of rows and columns 
    x_or_o (str): indicates which player's move it is
  Returns:
    bool: True if someone has three in a row in either direction of the board
  '''
  winning_possibilities = [                             #all combinantions of spaces that if held by user warrant a win
  [board[0][0], board[0][1], board[0][2]],
  [board[1][0], board[1][1], board[1][2]],
  [board[2][0], board[2][1], board[2][2]],
  [board[0][0], board[1][0], board[2][0]],
  [board[0][1], board[1][1], board[2][1]],
  [board[0][2], board[1][2], board[2][2]],
  [board[0][0], board[1][1], board[2][2]],
  [board[2][0], board[1][1], board[0][2]]]
  
  for win in winning_possibilities:           #if a list of one of the combinations is filled
    if all(w == x_or_o for w in win):
       return True          
  return False

         
def is_draw(board):
  '''
  Checks if there is a draw after player 1's move
  Args:
    board (list): updated list of rows and columns
  Returns:
    bool: True if all spaces are filled and no winner is found
  '''
  if not check_winner(board, "X"):        #if no one has won
    for i in board:                       #for all spaces on the board, if any of the spaces are open, there is not a tie
      if any(s == ' ' for s in i):
        return False
    print('Close Game! The game ends in a tie!')
    return True


def play_game(player_x_score, player_o_score, bot_or_user):
  '''
  Plays a game of tic-tac-toe between two players or a player and a bot
  Args:
    player_x_score (int): score of player 1
    player_o_score (int): score of player 2
    bot_or_user (str): indicates whether a bot or user is player 2
  returns
    player_x_score (int): score of player 1
    player_o_score (int): score of player 2
  '''
  board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  display_board(board)

  while True:
    board = get_player_move(board, "X")
    display_board(board)

    if check_winner(board, "X"):
      print('Player X won the game!')
      player_x_score += 1
      return player_x_score, player_o_score
    if is_draw(board):
      break

    if bot_or_user == 'player':
      board = get_player_move(board, "O")
    else:
      board = get_bot_move(board)

    display_board(board)

    if check_winner(board, "O"):
      print('Player O won the game!')
      player_o_score += 1
      return player_x_score, player_o_score


def main():
  while True:
    opponent = input('Do you want to play against another person or against the CPU? (Enter 1 for another person and 2 for the CPU)')

    if opponent == "1":
      player_x_score = 0
      player_o_score = 0

      while True:
        print(f'player X wins = {player_x_score}')
        print(f'player O wins = {player_o_score}')
        question = input('Would you like to play tic tac toe? (answer with y/n): ').lower()
        
        if question == 'y':
          player_x_score, player_o_score = play_game(player_x_score, player_o_score, 'player')
        elif question == 'n':
          print('Okay! Thanks for playing!')
          exit()
        else:
          print('Please enter y or n')
          continue
    elif opponent == "2":
      player_score = 0
      bot_score = 0
      
      while True:
        print(f'Player wins = {player_score}')
        print(f'Computer wins = {bot_score}')
        question = input('Would you like to play tic tac toe? (answer with y/n): ').lower()
        
        if question == 'y':
          player_score, bot_score = play_game(player_score, bot_score, 'bot')
        elif question == 'n':
          print('Okay! Thanks for playing!')
          exit()
        else:
          print('Please enter y or n')
          continue
    else:
      print('Please enter 1 or 2')
      continue

main()