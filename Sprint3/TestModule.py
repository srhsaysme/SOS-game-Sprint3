from GameWindow import *
import pytest

class gameTesting:
    def testStartUp():
        testW = GameWindow()
        assert testW.blueScore == 0
        assert testW.redScore == 0
        assert testW.currentTurn
        assert testW.gameRunning
        assert len(testW.letterArray) == 8
        for y in range(0,8):
            assert len(testW.letterArray[y]) == 8
        for x in range(0,8):
            for y in range(0,8):
                assert testW.letterArray[y][x] == " "
        for x in range(0,8):
            for y in range(0,8):
                assert testW.labelGrid[y][x].cget("text") == " "
        assert testW.currentAnnounce == ""
        testW.window.destroy()
 
    def testPlaceLetter():
        testW = GameWindow()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.blueOButton.invoke()
        testW.addCharButton.invoke()
        assert testW.letterArray[3][3] == "S"
        assert testW.labelGrid[3][3].cget("text") == "S"
        assert testW.currentAnnounce == "Letter successfully placed"
        assert testW.announceLabel.cget("text") == "Letter successfully placed"
        testW.currentX.set(5)
        testW.addCharButton.invoke()
        assert testW.letterArray[3][4] == "O"
        assert testW.labelGrid[3][4].cget("text") == "O"
        assert testW.letterArray[0][0] == " "
        assert testW.labelGrid[0][0].cget("text") == " "
        assert testW.currentAnnounce == "Letter successfully placed"
        assert testW.announceLabel.cget("text") == "Letter successfully placed"
        assert testW.gameRunning == True
        testW.window.destroy()

    def testOccupiedSpace():
        testW = GameWindow()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.blueOButton.invoke()
        testW.addCharButton.invoke()
        testW.addCharButton.invoke()
        assert testW.letterArray[3][3] == "S"
        assert testW.labelGrid[3][3].cget("text") == "S"
        assert testW.currentAnnounce == "Entered position is occupied"
        assert testW.announceLabel.cget("text") == "Entered position is occupied"
        assert testW.currentTurn == False
        assert testW.turnLabel.cget("text") == "Blue's turn"
        testW.window.destroy()

    def testInvalidIntegers():
        testW = GameWindow()
        testW.currentX.set(-9)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid grid position"
        assert testW.currentAnnounce == "Invalid grid position"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.letterArray[y][x] == " "
        for x in range(0,8):
            for y in range(0,8):
                assert testW.labelGrid[y][x].cget("text") == " "
        assert testW.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.gameRunning == True
        testW.currentX.set(2)
        testW.currentY.set(20)
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid grid position"
        assert testW.currentAnnounce == "Invalid grid position"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.letterArray[y][x] == " "
        for x in range(0,8):
            for y in range(0,8):
                assert testW.labelGrid[y][x].cget("text") == " "
        assert testW.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.gameRunning == True
        testW.window.destroy()

    def testInvalidEntries():
        testW = GameWindow()
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid entry"
        assert testW.currentAnnounce == "Invalid entry"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.letterArray[y][x] == " "
        for x in range(0,8):
            for y in range(0,8):
                assert testW.labelGrid[y][x].cget("text") == " "
        assert testW.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.gameRunning == True

    def testTurnSwitch():
        testW = GameWindow()
        testW.currentX.set(1)
        testW.currentY.set(1)
        assert testW.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        while (int(testW.currentY.get()) <= 8):
            testW.addCharButton.invoke()
            if (int(testW.currentY.get()) % 2 == 1):
                assert not testW.currentTurn
                assert testW.turnLabel.cget("text") == "Blue's turn"
            else:
                assert testW.currentTurn
                assert testW.turnLabel.cget("text") == "Red's turn"
            testW.currentY.set(int(testW.currentY.get()) + 1)

    def testLetterSwitch():
        testW = GameWindow()
        testW.redOButton.invoke()
        testW.blueOButton.invoke()
        testW.currentX.set(1)
        testW.currentY.set(1)
        testW.addCharButton.invoke()
        assert testW.letterArray[0][0] == "O"
        assert testW.labelGrid[0][0].cget("text") == "O"
        testW.currentY.set(2)
        testW.addCharButton.invoke()
        assert testW.letterArray[1][0] == "O"
        assert testW.labelGrid[1][0].cget("text") == "O"
        testW.redSButton.invoke()
        testW.blueSButton.invoke()
        testW.currentY.set(3)
        testW.addCharButton.invoke()
        assert testW.letterArray[2][0] == "S"
        assert testW.labelGrid[2][0].cget("text") == "S"
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.letterArray[3][0] == "S"
        assert testW.labelGrid[3][0].cget("text") == "S"

    def testBoardIsFull():
        testW = GameWindow()
        for x in range(1,9):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
                if (x == 8 and y == 8):
                    assert not testW.gameRunning
                else:
                    assert testW.gameRunning

    def testInsertWhenGameOver():
        testW = GameWindow()
        testW.gameRunning = False
        testW.currentX.set(5)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.currentAnnounce == "Game is over"
        assert testW.announceLabel.cget("text") == "Game is over"
        assert not testW.gameRunning
        assert testW.labelGrid[3][4].cget("text") == " "
        assert testW.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"

    def testNewGame():
        testW = GameWindow()
        for x in range(1,9):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
        testW.newGameButton.invoke()
        assert testW.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentAnnounce == ""
        assert testW.announceLabel.cget("text") == ""
        assert testW.blueScore == 0
        assert testW.blueScoreLabel.cget("text") == "0"
        assert testW.redScore == 0
        assert testW.redScoreLabel.cget("text") == "0"
        for x in range(0, len(testW.labelGrid)):
            for y in range(0, len(testW.labelGrid)):
                assert testW.labelGrid[y][x].cget("text") == " "
                assert testW.letterArray[y][x] == " "