#
# Draw board triangle in ascii
#
def DrawBoard(board):
  peg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for n in xrange(1,16):
    peg[n] = '.'
    if n in board:
      peg[n] = "%X" % n
  print "     %s" % peg[1]
  print "    %s %s" % (peg[2],peg[3])
  print "   %s %s %s" % (peg[4],peg[5],peg[6])
  print "  %s %s %s %s" % (peg[7],peg[8],peg[9],peg[10])
  print " %s %s %s %s %s" % (peg[11],peg[12],peg[13],peg[14],peg[15])
#

# remove peg n from board
def RemovePeg(board,n):
  board.remove(n)

# Add peg n on board
def AddPeg(board,n):
  board.append(n)

# return true if peg N is on board else false is empty position
def IsPeg(board,n):
  return n in board

# A dictionary of valid jump moves index by jumping peg
# then a list of moves where move has jumpOver and LandAt positions
JumpMoves = { 1: [ (2,4),(3,6) ],  # 1 can jump over 2 to land on 4, or jumper over 3 to land on 6
              2: [ (4,7),(5,9)  ],
              3: [ (5,8),(6,10) ],
              4: [ (2,1),(5,6),(7,11),(8,13) ],
              5: [ (8,12),(9,14) ],
              6: [ (3,1),(5,4),(9,13),(10,15) ],
              7: [ (4,2),(8,9)  ],
              8: [ (5,3),(9,10) ],
              9: [ (5,2),(8,7)  ],
             10: [ (9,8) ],
             11: [ (12,13) ],
             12: [ (8,5),(13,14) ],
             13: [ (8,4),(9,6),(12,11),(14,15) ],
             14: [ (9,5),(13,12)  ],
             15: [ (10,6),(14,13) ]
            }

Solution = []
#
# Recursively solve the problem
#
def Solve(board):
  #DrawBoard(board)
  if len(board) == 1:
    return board # Solved one peg left
  # try a move for each peg on the board
  for peg in xrange(1,16): # try in numeric order not board order
    if IsPeg(board,peg):
      movelist = JumpMoves[peg]
      for over,land in movelist:
        if IsPeg(board,over) and not IsPeg(board,land):
          saveboard = board[:] # for back tracking
          RemovePeg(board,peg)
          RemovePeg(board,over)
          AddPeg(board,land) # board order changes!

          Solution.append((peg,over,land))

          board = Solve(board)
          if len(board) == 1:
            return board
        ## undo move and back track when stuck!
          board = saveboard[:] # back track
          del Solution[-1] # remove last move
  return board

#
# Remove one peg and start solving
#
def InitSolve(empty):
  board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  RemovePeg(board,empty_start)
  Solve(board)

#
empty_start = 1
InitSolve(empty_start)

board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
RemovePeg(board,empty_start)
for peg,over,land in Solution:
  RemovePeg(board,peg)
  RemovePeg(board,over)
  AddPeg(board,land) # board order changes!
  DrawBoard(board)
  print "Peg %X jumped over %X to land on %X\n" % (peg,over,land)