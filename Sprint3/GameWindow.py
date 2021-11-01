from GameLogic import *
import time

#Inherits from GameLogic.
class GameWindow(GameLogic):
    """
    Class that creates window and displays the state of the game in the GUI.

    Inherits all of the variables and methods from GameLogic. Creates the window and frames that
    will contain UI widgets, then creates labels, buttons, and entry boxes and places them in 
    the frames. The playing grid takes up the middle space, options for each player rest on the 
    sides of the grid, and the bottom holds the buttons for controlling the game and entry boxes
    for inputting x and y values.

    Important Attributes:
        xEntry and yEntry: entry boxes that receive coordinates from the user.
        redSButton and redOButton: buttons that control whether Red will enter an S or an O.
        blueSButton and blueObutton: buttons that do the same thing for Blue.
        addCharButton: adds a letter to GameLogic.letterArray and labelGrid IF inputs from xEntry
        and yEntry are a valid, unoccupied space.
        newGameButton: restarts game by resetting all values to original states.
        labelGrid: a 8x8 grid of labels that display the current status of GameLogic.letterGrid.

        gridLetter(self): method connected to addCharButton. Finds appropriate letter and coordinates,
        then places letter in GameLogic.letterArray and labelGrid OR displays error message in
        announceLabel. Also checks if game is over.
        newGameCommand(self): method connected to newGameButton. Resets GameLogic variables with 
        GameLogic.newGameSetup and resets necessary widgets.
    """

    def __init__(self):
        #Initializes GameLogic variables and methods within GameWindow.
        GameLogic.__init__(self)

        #Window setup.
        self.window = tk.Tk()
        self.window.title("SOS Game")
        self.window.geometry("600x400")

        #Sets up frames within window.
        self.headerFrame = tk.Frame(self.window)
        self.redFrame = tk.Frame(self.window)
        self.blueFrame = tk.Frame(self.window)
        self.gridFrame = tk.Frame(self.window)
        self.scoreFrame = tk.Frame(self.window)
        self.charEntryFrame = tk.Frame(self.window)

        #Labels that will be edited during the game.
        self.redScoreLabel = tk.Label(self.scoreFrame, width = 3, text = "0")
        self.blueScoreLabel = tk.Label(self.scoreFrame, width = 3, text = "0")
        self.turnLabel = tk.Label(self.scoreFrame, text = "Red's turn")
        self.announceLabel = tk.Label(self.scoreFrame)

        #String variables and radio buttons that control what letter each player will insert.
        self.redSV = tk.StringVar(self.window, "S")
        self.blueSV = tk.StringVar(self.window, "S")
        self.redSButton = tk.Radiobutton(self.redFrame, pady = 3, text = "S", variable = self.redSV, value = "S")
        self.redOButton = tk.Radiobutton(self.redFrame, pady = 3, text = "O", variable = self.redSV, value = "O")
        self.blueSButton = tk.Radiobutton(self.blueFrame, pady = 3, text = "S", variable = self.blueSV, value = "S")
        self.blueOButton = tk.Radiobutton(self.blueFrame, pady = 3, text = "O", variable = self.blueSV, value = "O")

        #Integer variable and radio buttons that will control the next game's ruleset (not implemented).
        self.nextGameType = tk.IntVar(self.window, 0)
        self.simpleButton = tk.Radiobutton(self.charEntryFrame, text = "Simple Game", variable = self.nextGameType, value = 0)
        self.complexButton = tk.Radiobutton(self.charEntryFrame, text = "Complex Game", variable = self.nextGameType, value = 1)

        #String variables and entry boxes that obtain coordinates for entered letter.
        self.currentX = tk.StringVar(self.window)
        self.currentY = tk.StringVar(self.window)
        self.nextGridSizeVar = tk.StringVar(self.window, value = "8")
        self.xEntry = tk.Entry(self.charEntryFrame, width = 10, textvariable = self.currentX)
        self.yEntry = tk.Entry(self.charEntryFrame, width = 10, textvariable = self.currentY)
        self.gridSizeEntry = tk.Entry(self.charEntryFrame, width = 5, textvariable = self.nextGridSizeVar)

        #Checkboxes that control whether a player is controlled by a human or computer (not implemented).
        self.redComputerBox = tk.Checkbutton(self.redFrame, text = "Computer")
        self.blueComputerBox = tk.Checkbutton(self.blueFrame, text = "Computer")

        #Buttons that add S or O to board and starts new game.
        self.addCharButton = tk.Button(self.charEntryFrame, text = "Add character", command = self.gridLetter)
        self.newGameButton = tk.Button(self.charEntryFrame, text = "New Game", command = self.newGameCommand)

        #Label placements.
        tk.Label(self.headerFrame, text = "SOS Game").pack(fill = 'x')
        tk.Label(self.headerFrame, text = "By Stephen Holman").pack(fill = 'x')

        tk.Label(self.redFrame, text = "Red Player", pady = 15).pack()
        self.redSButton.pack()
        self.redOButton.pack()
        self.redComputerBox.pack(pady = 10)

        tk.Label(self.blueFrame, text = "Blue Player", pady = 15).pack()
        self.blueSButton.pack()
        self.blueOButton.pack()
        self.blueComputerBox.pack(pady = 10)

        tk.Label(self.scoreFrame, text = "Red Score: ").pack(side = 'left')
        self.redScoreLabel.pack(side = 'left')
        self.blueScoreLabel.pack(side = 'right')
        tk.Label(self.scoreFrame, text = "Blue Score: ").pack(side = 'right')
        self.announceLabel.pack()
        self.turnLabel.pack()

        tk.Label(self.charEntryFrame, text = "X value:").grid(row = 0, column = 0)
        self.xEntry.grid(row = 0, column = 1)
        tk.Label(self.charEntryFrame, text = "Y value:").grid(row = 0, column = 2)
        self.yEntry.grid(row = 0, column = 3)
        self.addCharButton.grid(row = 1, column = 0, columnspan = 4, pady = 10)
        tk.Label(self.charEntryFrame, text = "Game Type:").grid(row = 2, column = 0)
        self.simpleButton.grid(row = 2, column = 1)
        self.complexButton.grid(row = 2, column = 2)
        self.newGameButton.grid(row = 2, column = 3)
        tk.Label(self.charEntryFrame, text = "New Game Grid Size: (From 5 to 10)").grid(row = 3, column = 0, columnspan = 3)
        self.gridSizeEntry.grid(row = 3, column = 3)

        #Playing grid placements.
        self.labelGrid = []
        for y in range(0, 8):
            tempGrid = []
            for x in range(0, 8):
                tempLabel = tk.Label(self.gridFrame, text = " ", height = 1, width = 1, padx = 5, relief = "ridge")
                tempGrid.append(tempLabel)
                tempLabel.grid(row = y, column = x)
            self.labelGrid.append(tempGrid)

        #Places frames within window.
        self.headerFrame.grid(row = 0, column = 1)
        self.redFrame.grid(row = 1, column = 0)
        self.gridFrame.grid(row = 1, column = 1)
        self.blueFrame.grid(row = 1, column = 2)
        self.scoreFrame.grid(row = 2, column = 1)
        self.charEntryFrame.grid(row = 3, column = 1)

    #Method for adding letter to the grid in the GUI.
    def gridLetter(self):
        try:   
            selectedX = int(self.currentX.get()) - 1
            selectedY = int(self.currentY.get()) - 1
            #Decides which letter to enter based on whose turn it is.
            if (self.currentTurn):
                selectedLetter = self.redSV.get()
            else:
                selectedLetter = self.blueSV.get()
            success = GameLogic.placeLetter(self, int(self.currentX.get()), int(self.currentY.get()), selectedLetter)
            #Only places letter in labelGrid if GameLogic.placeLetter was successful, then checks if game is over.
            if (success):
                self.labelGrid[selectedY][selectedX].config(text = self.letterArray[selectedY][selectedX])
                self.gameOver()
        except (TypeError, ValueError):
            self.currentAnnounce = "Invalid entry"
        finally:
            #Updates announcement and current turn.
            self.announceLabel.config(text = self.currentAnnounce)
            self.turnLabel.config(text = self.getTurnString())

    #Method for restarting game and resetting labels.
    def newGameCommand(self):
        try:
            self.nextGameSize = int(self.nextGridSizeVar.get())  #FIXME: Error thrown when not integer.
            if (self.nextGameSize >= 5 and self.nextGameSize <= 10):
                GameLogic.newGameSetup(self)
                self.redScoreLabel.config(text = "0")
                self.blueScoreLabel.config(text = "0")
                #Resets labelGrid.
                for y in range(0, len(self.labelGrid)):
                    for x in range(0, len(self.labelGrid[0])):
                        self.labelGrid[y][x].grid_forget()
                self.labelGrid = []
                for y in range(0, self.currentGameSize):
                    tempGrid = []
                    for x in range(0, self.currentGameSize):
                        tempLabel = tk.Label(self.gridFrame, text = " ", height = 1, width = 1, padx = 5, relief = "ridge")
                        tempGrid.append(tempLabel)
                        tempLabel.grid(row = y, column = x)
                    self.labelGrid.append(tempGrid)
            else:
                self.currentAnnounce = "Grid size outside acceptable range"
        except (TypeError, ValueError):
            self.currentAnnounce = "Invalid entry for grid size"
        finally:
            self.announceLabel.config(text = self.currentAnnounce)
            self.turnLabel.config(text = self.getTurnString())