import os
import random

quit = False
catsGame = False
activePlay = '-'
newGame = ['-','-','-','-','-','-','-','-','-']

def opponent(play):
  if(play == "X"):
    return "O"
  elif(play == 'O'):
    return 'X'
  else:
    return play

def display_board(board):
  import os
  dummy = os.system("cls")
  for x in range(0,3):
    print(x, ":", board[x], end='  |  ')
  print()
  for x in range(3,6):
    print(x, ":", board[x], end='  |  ')
  print()
  for x in range(6,9):
    print(x, ":", board[x], end='  |  ')
  print()
  pass
  
def reset(board):
  global activePlay
  if(random.randint(0,1) == 0):
    activePlay = 'O'
  else:
    activePlay = 'X'
  for x in board:
    x = '-'
  pass
  
def changeturn(act):
  global quit
  global activePlay
  if(quit == False):
    if (act == 'X'):
      activePlay = 'O'
    elif (act == 'O'):
      activePlay = 'X'
      
def getCell(player):
  choice = 'n'
  while(choice.isdigit() == False or choice == ''):
    choice = input("Player " + player + ", pick a cell (0-8): ")
    if(choice == ''):
      choice = 'n'
    elif(choice[0] == '9'):
      choice = 'n'
  return int(choice[0])
  
  
def checkLoc(board, tgt, play):
  if(board[tgt] == '-' and 0 <= tgt <= 8):
    board[tgt] = play
    changeturn(play)
    global quit
    quit = checkwin(play, board)
  pass

def checkwin(play, board):
  winner = ''
#horizontal
  if(lineup(0,1,2,board)):
    winner = board[0]
    return True
  elif(lineup(3,4,5,board)):
    winner = board[0]
    return True
  elif(lineup(6,7,8,board)):
    winner = board[0]
    return True
#diagonal
  elif(lineup(0,4,8,board)):
    winner = board[0]
    return True
  elif(lineup(2,4,6,board)):
    winner = board[0]
    return True
#vertical
  elif(lineup(0,3,6,board)):
    winner = board[0]
    return True
  elif(lineup(1,4,7,board)):
    winner = board[0]
    return True
  elif(lineup(2,5,8,board)):
    winner = board[0]
    return True
  elif(board.count('-') == 0):
    global catsGame
    catsGame = True
    return True
#default
  else:
    return False
  
def lineup(one, two, three, board):
  if(board[one] == board[two] and board[two] == board[three] and board[one] != '-'):
     return True
  else:
     return False
   
def gameloop(board):
  #display board
  #input row and col
  #check valid location
  #update location
  #check win
  #change player turn
  
  global activePlay
  global quit
  while(quit == False):
    display_board(newGame)
    checkLoc(newGame, getCell(activePlay), activePlay)
  display_board(newGame)

  pass

reset(newGame)
gameloop(newGame)
if(catsGame):
  print("Both players lose!")
else:
  print("Player", opponent(activePlay), "wins!")