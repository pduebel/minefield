import os
import sys
from random import randint

playing = True

while playing == True:
  # create a 10 x 11 board
  board = []

  for i in range(10):
    board.append(['-'] * 11)

  # create mine coordinates
  mine_rows = [randint(0, len(board) - 1) for i in range(31)]
  mine_cols = [randint(0, len(board) - 1) for i in range(31)]

  # set hero starting position
  hero_row = len(board) - 1
  hero_col = len(board[0]) // 2
  board[hero_row][hero_col] = "O"

  # display board & instructions
  for i in range(len(board)):
    print ("".join(board[i]))

  print ("")  
  print ("Choose W,A,S or D + enter to move")

  def is_it_dead(hero_row, hero_col, mine_rows, mine_cols):
    '''Helper function to check if hero has landed on mine.'''
    for i in range(30):
      if hero_row == mine_rows[i] and hero_col == mine_cols[i]:
        return True

  # keep playing while player has remaining lives
  lives = 6
  while lives > 0:

    # use user input to update hero position
    board[hero_row][hero_col] = "-"
    move = input("")
    if move == "w":
      hero_row -= 1
    elif move == "a":
      hero_col -= 1
    elif move == "s":
      hero_row += 1
    elif move == "d":
      hero_col += 1
  
    # check if hero has landed on mine
    if is_it_dead(hero_row, hero_col, mine_rows, mine_cols) == True:
      board[hero_row][hero_col] = "X"
      lives -= 1
      print ("Mine! You have %d lives remaining"   %(lives))
      hero_row = len(board) - 1
      hero_col = len(board[0]) // 2
      board[hero_row][hero_col] = "O"
  
    # if hero reaches end of board player wins
    if hero_row == 0:
      print ("You Win!")
      lives -= 6
    else:
      board[hero_row][hero_col] = "O"
    
    if lives == 0:
      print ("Game Over!")
  
    # reprint board with updated positions
    for e in range(len(board)):
      print ("".join(board[e]))
  
  # check if player wants to play again
  answered = False
  while answered == False:
    reset = input("Play again? (y/n):")
    if reset.lower() in ("no", "n"):
      answered = True
      playing = False
    elif reset.lower() in ("yes", "y"):
      answered = True
    else:
      print("Accepted inputs include 'yes', 'y', 'no', or 'n'")