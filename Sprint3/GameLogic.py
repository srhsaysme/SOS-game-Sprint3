import tkinter as tk

class GameLogic:
    """
    Class full of variables and methods that control the game's status.

    Contains variables like the player's scores, whose turn it is, whether the game is over,
    and the current ruleset.  The methods edit the variables to match the players' inputs,
    start a new game, and later to keep track of player scores.

    Attributes:
        redScore and blueScore: ints that keep track of how many times a player has scored
        currentTurn: bool that is True when it is Red's turn and False when it is Blue's turn.
        currentGameType: int that will keep track of what the current ruleset of the game is.
        redPlayer and bluePlayer: bools that determine whether the players are controlled by
        humans or the computer.
        letterArray: a 8x8 array that keeps track of the letters inputed by the players.

        placeLetter(self, xVal, yVal, letter): places the given letter at coordinates (yVal, xVal)
        within the letterArray.
        changeRedLetter(letter) and changeBlueLetter(letter): changes the selected letter 
        for a player that will be placed in the letterArray with placeLetter method.
        newGameSetup(self): sets up new game by restoring variables to their original state.
        getTurnString(self): returns a string that tells whether it is Red's or Blue's turn based
        on currentTurn.
    """

    #Initiates GameLogic with variables controlling game and an array of strings.
    def __init__(self):
        self.redScore = 0
        self.blueScore = 0
        #When currentTurn is true, it is red's turn; otherwise, it is blue's turn.
        self.currentTurn = True
        self.currentAnnounce = ""
        self.gameRunning = True

        self.currentGameType = 0
        self.currentGameSize = 8
        self.nextGameSize = 8
        #When these variables are true, there is a human player; otherwise, it is a computer.
        self.redPlayer = True
        self.bluePlayer = True

        #Initializes 2D array that contains letters.
        self.letterArray = []
        for y in range(0,8):
            tempArray = []
            for x in range(0,8):
                tempArray.append(" ")
            self.letterArray.append(tempArray)

    #Places letter within letterArray IF the inputs are valid.
    def placeLetter(self, xVal, yVal, letter):
        #If the game is already over, the letter is not placed.
        if (self.gameRunning == False):
            self.currentAnnounce = "Game is over"
            return False
        #If the input values would not fit on the grid, the letter is not placed.
        elif (xVal <= 0 or xVal > 8 or yVal <= 0 or yVal > 8):
            self.currentAnnounce = "Invalid grid position"
            return False
        #If the space in the array is occupied, the letter is not placed.
        elif (self.letterArray[yVal - 1][xVal - 1] != " "):
            self.currentAnnounce = "Entered position is occupied"
            return False
        #If this is a valid position, places the letter in the correct space
        #in the array and returns True.
        else:
            self.letterArray[yVal - 1][xVal - 1] = letter
            self.currentTurn = not self.currentTurn
            self.currentAnnounce = "Letter successfully placed"
            return True
        
    #Two methods that change letter for each player.
    def changeRedLetter(letter):
        redLetter = letter

    def changeBlueLetter(letter):
        blueLetter = letter

    #Method that resets variables and array for new game.
    def newGameSetup(self):
        self.redScore = 0
        self.blueScore = 0
        self.currentTurn = True
        self.currentAnnounce = ""
        self.gameRunning = True
        #Resets all of the values in the array.
        self.letterArray = []
        for y in range(0, self.nextGameSize):
            tempArray = []
            for x in range(0, self.nextGameSize):
                tempArray.append(" ")
            self.letterArray.append(tempArray)
        self.currentGameSize = self.nextGameSize

    #Determines whether game is over because grid is full. TODO: EXPAND TO INCLUDE VICTORY CONDITIONS.
    def gameOver(self):
        gridFull = True
        for x in range(0,8):
            for y in range(0,8):
                if (self.letterArray[y][x] == " "):
                    gridFull = False
        if (gridFull):
            self.gameRunning = False
        else:
            self.gameRunning = True

    #Method that returns string based on which player's turn it is.
    def getTurnString(self):
        if (self.currentTurn):
            return "Red's turn"
        else:
            return "Blue's turn"
