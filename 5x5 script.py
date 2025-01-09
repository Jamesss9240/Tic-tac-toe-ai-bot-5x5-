import random
import math
#array of game
gameBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
 "10", "11", "12", "13", "14", "15", "16", "17",
 "18", "19", "20", "21", "22", "23", "24", "25"]
#variable setup
winner = ""
global turn

score=0
moves=0

depth_allowance=2
turn = input("would you like to play first or Second (1/2)") #choose whether to start or go 2nd
if turn == "1":
    turn = "0"
  
else:
    turn="1"
global markPlayer
global markCPU
markPlayer = input("would you like to play X or O (X/O)") #choose which mark to use
if markPlayer.upper() == "X":
    markPlayer="X"
    markCPU="O"

else:
    markPlayer="O"
    markCPU="X"

def printGameBoard():
    #modify gameboard such that it prints in line
  for i in range(16):
      if gameBoard[i+9]=="X":
          gameBoard[i+9]="X "
         
      elif gameBoard[i+9]=="O":
          gameBoard[i+9]="O "
         
  print(gameBoard[0] + "  | " + gameBoard[1] + "  | " + gameBoard[2] + "  | " + gameBoard[3] + "  | " + gameBoard[4]) #prints gameboard
  print("-----------------------")
  print(gameBoard[5] + "  | " + gameBoard[6] + "  | " + gameBoard[7] + "  | " + gameBoard[8] + "  | " + gameBoard[9])
  print("-----------------------")
  print(gameBoard[10] + " | " + gameBoard[11] + " | " + gameBoard[12] + " | " + gameBoard[13] + " | " + gameBoard[14])
  print("-----------------------")
  print(gameBoard[15] + " | " + gameBoard[16] + " | " + gameBoard[17] + " | " + gameBoard[18] + " | " + gameBoard[19])
  print("-----------------------")
  print(gameBoard[20] + " | " + gameBoard[21] + " | " + gameBoard[22] + " | " + gameBoard[23] + " | " + gameBoard[24])
    #fix gameboard such that it doesnt produce errors
  for i in range(16):
      if gameBoard[i+9]=="X ":
          gameBoard[i+9]="X"
         
      elif gameBoard[i+9]=="O ":
          gameBoard[i+9]="O"
printGameBoard()  


def CheckTie(Board): #checks for tie/all tiles used
  if (Board[0] != "1" and Board[1] != "2" and
      Board[2] != "3" and Board[3] != "4" and
      Board[4] != "5" and Board[5] != "6" and
      Board[6] != "7" and Board[7] != "8" and
      Board[8] != "9" and Board[9] != "10" and 
      Board[10] != "11" and
      Board[11] != "12" and Board[12] != "13" and
      Board[13] != "14" and Board[14] != "15" and
      Board[15] != "16" and Board[16] != "17" and
      Board[17] != "18" and Board[18] != "19" and
      Board[19] != "20" and Board[20] != "21" and
      Board[21] != "22" and Board[22] != "23" and
      Board[23] != "24" and Board[24] != "25"):
    tie = True
  else:
    tie = False
  return tie
def CheckWin(board): #check for wins
    #horizontal
    for i in range(0, 25, 5):
        if board[i] == board[i+1] == board[i+2] == board[i+3] == board[i+4] != " ":
            return True
    #vertical
    for i in range(5):
        if board[i] == board[i+5] == board[i+10] == board[i+15] == board[i+20] != " ":
            return True
    #diagonal
    if board[0] == board[6] == board[12] == board[18] == board[24] != " ":
        return True
    if board[4] == board[8] == board[12] == board[16] == board[20] != " ":
        return True
    else:
      return False
def check_win(player, board): # check which mark has won
  if(board[0] == board[1] == board[2] == board[3] == board[4] == player):
    return True
  elif(board[5] == board[6] == board[7] == board[8] == board[9] == player):
    return True
  elif(board[10] == board[11] == board[12] == board[13] == board[14] == player):
    return True
  elif(board[15] == board[16] == board[17] == board[18] == board[19] == player):
    return True
  elif(board[20] == board[21] == board[22] == board[23] == board[24] == player):
    return True
  elif(board[0] == board[5] == board[10] == board[15] == board[20] == player):
        return True
  elif(board[1] == board[6] == board[11] == board[16] == board[21] == player):
        return True
  elif(board[2] == board[7] == board[12] == board[17] == board[22] == player):
        return True
  elif(board[3] == board[8] == board[13] == board[18] == board[23] == player):
        return True
  elif(board[4] == board[9] == board[14] == board[19] == board[24] == player):
      return True

  # diagonal
  elif(board[0] == board[6] == board[12] == board[18] == board[24] == player or
      board[4] == board[8] == board[12] == board[16] == board[20] == player):
      return True
  else:
      return False










def userMove():
  user_Input = -1
  while user_Input < 1 or user_Input > 25: #verification
    try: #used for if the user attempts to input a letter to prevent a crash
      user_Input = int(input("Enter your move: "))
      if user_Input > 25 or user_Input < 1:
        print("Invalid move, please enter between 1 and 25")
     
      elif gameBoard[user_Input-1] == "X" or gameBoard[user_Input-1] == "O":  
        print("This move has already been used")
        user_Input = -1
    except:
      print("please enter a number")

  gameBoard[user_Input - 1] = markPlayer # place palyers move

  printGameBoard() # print current board position
  if CheckWin(gameBoard)==True: #check if player has won
    input("Player wins! Press enter to exit")
    exit()

def evaluate(board):
  score=0
  #check rows and columns for the cpu
  for i in range(5):
      row_marker = 0
      col_marker = 0
      for j in range(5):
          if board[(i*5)+j] == markCPU: #reward exponentially for larger rows/columns, encourging the ai to go for wins
              row_marker += 1
          if board[j*5+i] == markCPU:
              col_marker += 1
      score += row_marker**3
      score += col_marker**3

  #check diagonal 
  diag_marker = 0
  for i in range(5):
      if board[i*6] == markCPU:
          diag_marker += 1
  score += diag_marker**3 #reward exponentially for larger rows/columns, encourging the ai to go for wins

  #check other diagonal
  diag2_marker = 0
  for i in range(5):
      if board[(i+1)*4] == markCPU:
          diag2_marker += 1
  score += diag2_marker**3 #reward exponentially for larger rows/columns, encourging the ai to go for wins

  #player lines
  #check rows and columns for player
  for i in range(5):
      row_marker = 0
      col_marker = 0
      for j in range(5):
          if board[(i*5)+j] == markPlayer:
              row_marker += 1
              try:
                  if board[((i*5)+j)-1] == markCPU or board[((i*5)+j)+1] == markCPU and row_marker>1: #reward ai for blocking
                      score=score+100
              except:
                  score=score        
          if board[j*5+i] == markPlayer:
              col_marker += 1
              try:
                  if board[((i*5)+j)-5] == markCPU or board[((i*5)+j)+5] == markCPU and col_marker>1: #reward ai for blocking
                      score=score+100
              except:
                  score=score
      score -= row_marker**3 #punish exponentially for larger rows/columns, helping the ai stop the player get a large amount of lines setup early game
      score -= col_marker**3

  #check diagonal 1
  diag_marker = 0
  for i in range(5):
      if board[i*6] == markPlayer:
          diag_marker += 1
  score -= diag_marker**3

  #check other diagonal
  diag2_marker = 0
  for i in range(5):
      if board[(i+1)*4] == markPlayer:
          diag2_marker += 1
  score -= diag2_marker**3
  if board[0] == markCPU: #reward ai for going in powerful positions like the 4 corners or centre
    score=score+250
  if board[4] == markCPU:
    score=score+250
  if board[24] == markCPU:
    score=score+250
  if board[20] == markCPU:
    score=score+250
  if board[12] == markCPU:
    score=score+300


  return score #return score to the minimax for checking





def cpuMove():
    bestscore=-10000
    bestmove=0
    for i in range(25): #iterate through every board position
             
            if gameBoard[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]: #check if empty
                gameBoard[i]=markCPU #setup first mark palcement for minimax
                score = minimax(gameBoard, 0, False, -10000, 10000,0) # calls minimax letting it know it is the players turn
                gameBoard[i] = str(i+1) #replace number in array
                if score > bestscore: #check if this placement of mark is stronger than previous placements
                    bestscore = score
                    bestmove = i
                        
    gameBoard[bestmove] = markCPU     #place best move
    printGameBoard()
    if CheckWin(gameBoard)==True: #if cpu wins print and exit
        input("CPU wins! Press enter to exit")
        exit()

def minimax(board, depth, maximising, alpha, beta, high_score): 
  if CheckWin(board) == True: #check for tie/player win/cpu win
    if check_win(markPlayer, board) == True:
      return -700000
    elif check_win(markCPU, board) == True:
      return 700000
  elif CheckTie(board) == True:
    return 0
  
  high_score = max(high_score, evaluate(board)) #update the current highest score based off the position in the evaluate function
  
    # Save the best score from the evaluate function


  if depth>depth_allowance: #if current explorable depth has been reached return back to cpu move with the current high score
    return high_score



  if maximising: #if cpu turn
    bestscore = -100000000
    for i in range(25):
      if board[i] not in ["X", "O"]: #if empty
        board[i] = markCPU #place mark
        score = minimax(board, depth + 1, False, alpha, beta,high_score) #recursively call minimax with the new board position
        bestscore= max(score, bestscore) #update bestscore
        alpha=max(alpha,bestscore) #update alpha
        board[i] = str(i+1) #restore board back to old state
        if beta <= alpha: # alpha beta pruning to improve performance if current position is bad
            break

    return bestscore
  else: #player turn
    bestscore = 100000000
    for i in range(25):
      if board[i] not in ["X", "O"]: #if empty
        board[i] = markPlayer
        score = minimax(board, depth + 1, True,alpha, beta, high_score)  #recursively call minimax with the new board position
        bestscore= min(score, bestscore) # save the minimum bestscore(best player move since the player is 'minimising')
        beta=min(beta,bestscore) #update beta
        board[i] = str(i+1)  #remove mark from board
        if beta <= alpha: #alpha beta pruning to improve performance
            break
    return bestscore






def move(turn): #change moves/check for ties and update explorable depth as game progresses, since less tiles are avaliable the game can be explored further at a smaller time penalty
  global moves
  moves=moves+1
  if moves==1:
      depth_allowance=2
  elif moves<3: #update explorable depth
      depth_allowance=3
  elif moves<4: #update explorable depth
      depth_allowance=7
  elif moves<6: #update explorable depth
      depth_allowance=15
  else: #update explorable depth
      depth_allowance=30
 

  if CheckTie(gameBoard)==True:
    print("Tie!") 
  elif turn == "0":
    print("PLAYERS TURN")
    userMove()
    move("1")
  elif turn == "1":
    print("CPU TURN")
    cpuMove()
    move("0")



move(turn)      






