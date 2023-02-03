import time

def runBoard(boardFile, myDict):
   # variables
   totalMoves = 0

   # load board from file
   myBoard = loadBoard(boardFile)

   # read in the dictionary to the myDict list
   myDict = readDictionary(myDict)

   # print out the board
   printBoard(myBoard)

   # print out starting string and cleverness
   print("\nAnd we're off!")
   print("Running with cleverness ON\n")

   # start the clock
   start = time.perf_counter()

   # Start from every possible location =======================================
   for y_iterator in range(len(myBoard)):
      for x_iterator in range(len(myBoard)):
         path = []
         currPosition = y_iterator, x_iterator
         legal_list = legalMoves(possibleMoves(currPosition, myBoard), path)
         # print("LEGAL LIST: ")
         # print(legal_list)
         for position in legal_list:
            currWord, isWord = examineState(myBoard, position, path, myDict)
            if isWord:
               "temp"

   # ==========================================================================
   # stop the clock
   stop = time.perf_counter()

   # print all done string
   print("All done")

   # calculate the time taken to execute
   timeTaken = stop - start

   # print the total moves and time taken
   print(f"Searched total of {totalMoves} moves in {timeTaken:0.8f} seconds")

   # print out the words found:
   # 2 letter
   # 3 letter
   # 4 letter
   # 5 letter

   # print total words found
      # length of found word list

   # sorted alphabetically

def readDictionary(filename):
   my_list_of_words = [word.strip() for word in open("twl06.txt")]
   return my_list_of_words

def legalMoves(moves, path):
   legal_list = [move for move in moves if move not in path]
   return legal_list

def examineState(myBoard, position, path, myDict):
   concatWord = ""
   isWord = False

   # add current position tile to the path
   path.append(position)
   # print("CURRENT PATH: ")
   # print(path)

   # compute the word now formed by the updated path
   for letterCoord in path:
      x, y = letterCoord
      wkgLetter = myBoard[x][y]
      concatWord += wkgLetter
   
   # if word is exactly in dictionary
   
   # if substring

   # returns tuple of (<current word generated>, <yes/no>)
   return concatWord, isWord

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

runBoard("board4.txt", "twl06.txt")
# runBoard("board3.txt", "twl06.txt")
# runBoard("board4.txt", "twl06.txt")