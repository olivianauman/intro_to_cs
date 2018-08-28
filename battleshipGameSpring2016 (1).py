#This is the backbone for the game Battleship!

#helper functions:  Write the python code for the following helper functions
#as they are described.  This backbone script runs without errors.  Make sure
#that as you modify this file, it always continues to run without errors.

#helper function #1
#create a list of lists containing the board
#the each entry in the board list is a list containing the rows of the board
#it should return the 10x10 board that will be used throughout the game.  All
#entries on the board should be 0 initially; we will change the values as we
#put the ships on the board and then play the game
def boardSetup():
    pass

#helper function #2
#write a function that checks to see if a ship of length n will fit starting at
#the (x,y) coordinate and being oriented up, down, left, right
#it should return a boolean: True if it fits, and False if it does not
#the orientations passed to this function should be one of the following:
#'up', 'down', 'left', 'right'
def doesItFit(n, x, y, orientation):
    pass
    

#this function will only be called if the ship fits on the board...it will check to make
#sure that the space is not occupied.  the restrictions for the orientations still apply
#if the spaces that the ship will occupy are free, the function will return True
#otherwise, the function will return False
def isThereRoom(board, n, x, y, orientation):
    pass     


#this function changes 0s to the number XXX to represent placing a ship onto the board
#this should only be done if the ship fits in that position and the
#spaces are not already occupied (see previous helper functions
#it should return the board after making these changes
def putShipOnBoard(board, n, x, y, orientation, XXX):
    pass
     

#this function will create the board and then place all of the ships onto the board
#there will be 5 ships: one of length 2, one of length 3, two of length 4
#and one of length 5
#for each ship, it should generate random x and y coordinates for the ship, 
#generate a random orientation, check to see if the ship fits, check to see if the
#spaces are occupied, and if it passes those tests, the ship should be placed on the board
#it should do this for all five ships.
#it should return the board after placing all of the ships on the board
#it should make use of the helper functions created up to this point
def placeShipsOnBoard():
    pass

#this function checks to see if a particular (x,y) point hits a battleship on the board
#it should return True if the (x,y) point hits a ship, and False if it does not
def amIAShip(board, x, y):
    pass


#this function records a hit on a battleship:
#it should return the board that has been changed to reflect this hit
def hitTheShip(board, x, y):
    pass

#determine if a particular ship that was hit has been sunk; return True if the ship has sunk
#and False if it has not
def amISunk(board, XXX):
    pass

#determine if there are any more ships on the board that have not been sunk
#if all of the ships have been sunk, return True, and if there is at least one
#ship that has not been sunk, return False
def gameOver(board):
    pass

#this function will be used to play a simple version of the game
#it should start by placing the ships on the board (using one of the
#helper functions created above
#it should then prompt the user to enter the x and y coordinates of a point
#on the board.  If the (x,y) coordinate hits a ship, it should tell the user
#that a ship has been hit.  If the ship has been sunk, it should give that information
#to the user.  If all of the ships have been hit, it should indicate that the game
#is over.  If the (x,y) coordinate misses, it should tell the user that they missed
#and continue to prompt the user for more coordinates.
def playGame():
    pass