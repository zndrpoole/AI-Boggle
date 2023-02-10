import time
import sys

def runBoard(boardFile, myDict):
   # variables
   totalMoves = 0
   validWords = []

   # load board from file
   myBoard = loadBoard(boardFile)

   # read in the dictionary to the myDict list
   myDict = readDictionary(myDict)

   # print out the board
   printBoard(myBoard)

   # print out starting string and cleverness
   print("\nAnd we're off!")
   print("Running with cleverness ON")

   # start the clock
   start = time.perf_counter()

   # Start from every possible location =======================================
   for y_iterator in range(len(myBoard)):
      for x_iterator in range(len(myBoard)):
         path = []
         currPosition = y_iterator, x_iterator
         validWords, path, totalMoves = checkAllPaths(myBoard, currPosition, path, myDict, totalMoves, validWords)
         
   # ==========================================================================
   # stop the clock
   stop = time.perf_counter()

   # print all done string
   print("All done")

   # calculate the time taken to execute
   timeTaken = stop - start

   # print the total moves and time taken
   print(f"\nSearched total of {totalMoves} moves in {timeTaken:0.8f} seconds")

   # print words found string
   print('\nWords found:')
   
   # strip duplicates
   validWords = list(set(validWords))

   # get length of words list
   lengthList = [[]]
   for word in validWords:
      if len(word) > len(lengthList):
         difference = len(word) - len(lengthList)
         for iterator in range(difference):
            lengthList.append([])
      lengthList[len(word)-1].append(word)

   # print out the words found:
   for wordList in lengthList:
      if len(wordList) != 0:
         print(str(len(wordList[0])) + ' -letter words:  ' + ', '.join(wordList))

   # print total words found
   print(f'\nFound {len(validWords)} words in total.')

   # print sorted alphabetically
   print('Alpha-sorted list words: ')
   validWords.sort()
   print(', '.join(validWords))

   # output to file
   outputFile = open('board4_words.txt', 'w')
   outputFile.writelines("\n".join(validWords))
   outputFile.close()

def checkAllPaths(myBoard, currPosition, path, myDict, totalMoves, validWords):
   # append current position to path list
   path.append(currPosition)

   # examine the boards' current state
   testWord, isWord, myDict = examineState(myBoard, currPosition, path, myDict)

   # if it's a valid word, append valid words list
   if isWord == "Yes":
      validWords.append(testWord)

   # get legal moves from possible moves
   legal_list = legalMoves(possibleMoves(currPosition, myBoard), path)

   # if legal moves is not empty, recurse
   if len(legal_list) != 0 and len(myDict) != 0:
      for newPosition in legal_list:
         validWords, path, totalMoves = checkAllPaths(myBoard, newPosition, path, myDict, totalMoves, validWords)

   # increment total moves
   totalMoves += 1

   # remove current position from the path
   path.remove(currPosition)

   # return appropriate data
   return validWords, path, totalMoves

def examineState(myBoard, currPosition, path, myDict):
   # seperate x and y coordinates
   yCoord, xCoord = currPosition

   # get test word from newly appended path list
   testWord = ''.join([myBoard[yCoord][xCoord] for yCoord, xCoord in path])

   # truncate dictionary
   myDict = [word for word in myDict if word.startswith(testWord.lower())]

   # test for word in new dictionary
   if testWord.lower() in myDict:
      return (testWord, "Yes", myDict)
   else:
      return (testWord, "No", myDict)

def readDictionary(filename):
   my_list_of_words = [word.strip() for word in open("twl06.txt")]
   return my_list_of_words

def legalMoves(moves, path):
   legal_list = [move for move in moves if move not in path]
   return legal_list

def loadBoard(boardFile):
   myBoard = [line.split() for line in open(boardFile)]
   return myBoard

def printBoard(myBoard):
   for index in range(len(myBoard)):
      print(" ".join(myBoard[index]))

def possibleMoves(xy_pair, myBoard):
   yCoord, xCoord = xy_pair
   board_size = len(myBoard)
   move_list = []
   for y_offset in [-1, 0, 1]:
      for x_offset in [-1, 0, 1]:
         new_pair = (yCoord + y_offset, xCoord + x_offset)
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
  
# get files from command line
boardFile = sys.argv[1]
myDict = sys.argv[2]

# call runBoard with command line files
runBoard(boardFile, myDict)