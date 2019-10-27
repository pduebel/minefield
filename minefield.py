from random import randint

#Creating a 10 x 11 board composed of '-'
board = []

for i in range(10):
  board.append(['-'] * 11)

#Creating 30 mines with random coordinates 
mine_rows = []
mine_cols = []

for i in range(31):
  mine_row = randint(0, len(board) - 1)
  mine_rows.append(mine_row)

for i in range(31):
  mine_col = randint(0, len(board[0]) - 1)
  mine_cols.append(mine_col)

#Setting the starting coordinates of the player(hero)
hero_row = len(board) - 1
hero_col = len(board[0]) // 2
board[hero_row][hero_col] = "O"

#Printing the board
for i in range(len(board)):
  print ("".join(board[i]))

#Function to check if the position of the hero is the same as the position of a mine
def is_it_dead(hero_row, hero_col, mine_rows, mine_cols):
  for i in range(30):
    if hero_row == mine_rows[i] and hero_col == mine_cols[i]:
      return True

#Printing instructions
print ("")  
print ("Choose W,A,S or D + enter to move")

#Assigning how many lives the player has
lives = 6

#While the player still has lives remaining they can still play
while lives > 0:

#Getting the player to input w,a,s or d and moving the hero accordingly
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
  
#If the hero lands on a mine one life is lost and the position of the hero is reset. If the hero reaches the top of the board then the player wins. If the player runs out of lives then it is game over.
  if is_it_dead(hero_row, hero_col, mine_rows, mine_cols) == True:
    board[hero_row][hero_col] = "X"
    lives -= 1
    print ("Mine! You have %d lives remaining"   %(lives))
    hero_row = len(board) - 1
    hero_col = len(board[0]) // 2
    board[hero_row][hero_col] = "O"
    
  if hero_row == 0:
    print ("You Win!")
    lives -= 6
  else:
    board[hero_row][hero_col] = "O"
    
  if lives == 0:
    print ("Game Over!")
  
#board is reprinted with updated positions
  for e in range(len(board)):
    print ("".join(board[e]))
