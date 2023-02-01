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
   print(move_list)
   return move_list

myBoard = loadBoard("board.txt")
printBoard(myBoard)
possibleMoves((0,0),myBoard)
possibleMoves((2,2),myBoard)