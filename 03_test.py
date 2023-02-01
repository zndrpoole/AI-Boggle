def runBoard(boardFile, myDict):
   myBoard = loadBoard("board.txt")
   totalMoves = 0
   time = 0
   path = []

   myDict = readDictionary("twl06.txt")

   printBoard(myBoard)

   print("And we're off!")
   print("Running with cleverness ON")
   #===========================================================================
   for y_iterator in range(len(myBoard)):
      for x_iterator in range(len(myBoard)):
         currPosition = x_iterator, y_iterator
         legal_list = legalMoves(possibleMoves(currPosition, myBoard), path)
         print(legal_list)
         for position in legal_list:
            currWord, isWord = examineState(myBoard, currPosition, path, myDict)
            if isWord:
               "temp"

   #===========================================================================
  


   print("All done")

   print("Searched total of " + totalMoves + " moves in " + time + " seconds")

def readDictionary(filename):
   my_list_of_words = [word.strip() for word in open("twl06.txt")]
   return my_list_of_words

def legalMoves(moves, path):
   legal_list = [move for move in moves if move not in path]
   return legal_list

def examineState(myBoard, position, path, myDict):
   # returns tuple
   for legal_pair in legal_list:
      legal_x, legal_y = legal_pair
      myBoard[legal_y][legal_x]

def loadBoard(boardFile):
   myBoard = [line.split() for line in open("board.txt")]
   return myBoard

def printBoard(myBoard):
   for index in range(len(myBoard)):
      print(" ".join(myBoard[index]))

def possibleMoves(xy_pair, myBoard):
   x, y = xy_pair
   board_size = len(myBoard)
   move_list = []
   for x_offset in [-1, 0, 1]:
      for y_offset in [-1, 0, 1]:
         new_pair = (x + x_offset, y + y_offset)
         is_good = True
         for coord in new_pair:
            if is_good:
               if coord < board_size and coord >=0:
                  pass
               else:
                  is_good = False
         if is_good and new_pair != xy_pair:
            move_list.append(new_pair)
   return move_list

runBoard("board2.txt", "twl06.txt")
# runBoard("board3.txt", "twl06.txt")
# runBoard("board4.txt", "twl06.txt")