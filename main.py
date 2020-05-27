import sys
import random
import threading
import logging


class Game:
    def __init__(self):

        self.players = 0
        self.currentPlayers = []
        self.length = 10
        self.current = None
        self.attacked = None
        self.start = True

    def showPlayers(self):  # Displays the state of the game
        for number in range(self.length):  # Prints all the Players boards including the states of their boards
            line = ""
            for player in self.currentPlayers:
                line = line + " ".join(player.board[number]) + "          "
            logging.info(line)
        line = ""
        for player in self.currentPlayers:  # Prints which Player is alive and which player is dead underneath their boards
            if player.alive == False:
                string = "Dead "
            else:
                string = "Alive"
            line = line + "Player " + str(player.playerNumber) + " - " + string + "             "
        logging.info(line + "\n")

    def checkGame(self):  # Checks if the players wishe to play again or end the game
        while True:
            answer = input("Play again y(es) / n(o)? ").lower()
            if answer == 'yes' or answer == 'y':  # calls the clear function and runs the game again
                self.clear()
                self.playGame()
            elif answer == 'no' or answer == 'n':  # prints a goodbye msg and stops the program
                logging.info("Thanks for playing!")
                sys.exit(0)

    def clear(self):  # After a round this methods will reset the gamestate to allow the another round to be played
        self.current = None
        self.attacked = None
        counter = 0
        for player in self.currentPlayers:
            player.clear()
            try:
                target = self.currentPlayers[counter + 1]
            except:
                target = self.currentPlayers[0]
            player.nextTarget = target
            counter = counter + 1

    def playGame(self):  # This is the method that runs the entire game
        if self.start == True:
            logging.info('Welcome!')
            self.buildBoards()
            self.start = False
        else:
            self.addPlayer()
        keepPlaying = True
        counter = 1
        while keepPlaying:
            threads = []
            for player in self.currentPlayers:  # Creates individual threads for each player and prints what happens in each round
                if player.alive == True:
                    thread = threading.Thread(target=player.attack)
                    threads.append(thread)
                    thread.start()
                    logging.info("Round: " + str(counter))
                    logging.info(player.message)
                    self.showPlayers()
                    counter = counter + 1
            for thread in threads:  # Joins the threads together
                thread.join()
            for player in self.currentPlayers:  # Checks if a player has won
                if player == player.nextTarget:
                    winner = player
                    keepPlaying = False
                    break
        # print the winner and call the checkGame function to see if the user wants to play again
        logging.info("Winner is Player " + str(winner.playerNumber) + "!")
        self.checkGame()

    def buildBoards(self):  # Creates the players right at the start of a round and sets up the class variables
        self.players = int(input('Choose how many players are going to play: '))
        logging.info("")
        for number in range(1, self.players + 1):  # Puts the players in a list stored in a class
            player = Player(number)
            self.currentPlayers.append(player)
        counter = 0
        for player in self.currentPlayers:  # Sets all the players targets
            try:
                target = self.currentPlayers[counter + 1]
            except:
                target = self.currentPlayers[0]
            player.nextTarget = target
            counter = counter + 1

    def addPlayer(
            self):  # Adds new players in any position between the players if the players choose to add new players
        while self.start == False:
            answer = input("Do you want to add a player y(es) / n(o)? ").lower()
            if answer == 'yes' or answer == 'y':
                self.players = self.players + 1
                newPlayer = Player(self.players)
                first = int(input("Pick first player to be besides: "))
                second = int(input("Pick second player to be besides: "))
                for player in self.currentPlayers:  # finds the exact position of the players in list of all players
                    if player.playerNumber == first:
                        firstPlayer = player
                    elif player.playerNumber == second:
                        secondPlayer = player
                try:  # inserts the players into list and fixes the targets to include the new player
                    if firstPlayer.nextTarget == secondPlayer:
                        index = self.currentPlayers.index(firstPlayer)
                    elif secondPlayer.nextTarget == firstPlayer:
                        index = self.currentPlayers.index(secondPlayer)
                    newPlayer.nextTarget = self.currentPlayers[index].nextTarget
                    self.currentPlayers[index].nextTarget = newPlayer
                    self.currentPlayers.insert(index + 1, newPlayer)
                    return
                except:
                    logging.info("Invalid entry!")  # log invalid entry if user gives a invalid position
            elif answer == 'no' or answer == 'n':
                return


class Player():
    def __init__(self, playerNumber):
        self.length = 10
        self.board = []
        self.ownBoat = None
        self.playerNumber = playerNumber
        self.buildBoard(self.playerNumber)
        self.chooseStart()
        self.alive = True
        self.targets = []
        self.setTargets()
        self.nextTarget = None
        self.message = None

    def chooseStart(
            self):  # Chooses the players own target. The column and row could be replaced with input statements if someone wanted to play
        column = random.randint(0, 9)
        row = random.randint(0, 9)
        self.ownBoat = [row, column]

    def buildBoard(self, playerNumberPlayer):  # Creates a board for the individual player
        for unit in range(self.length):
            self.board.append(["."] * self.length)

    def attack(self):  # This allows a player to attack the next target the player is meant to attack
        while True:
            row = random.randint(0, self.length)
            column = random.randint(0, self.length)
            coord = [row, column]
            if coord in self.nextTarget.targets:  # Makes sure the player chooses a target that hasn't been fired at already
                self.message = "Player " + str(self.playerNumber) + " shot Player " + str(
                    self.nextTarget.playerNumber) + " on position " + str([coord[0] + 1, coord[1] + 1])
                self.nextTarget.targets.remove(coord)
                if self.nextTarget.ownBoat == coord:  # If the coordinates the current player entered hits the boat belonging target player
                    self.message = self.message + "... and Hit!"
                    self.nextTarget.board[coord[0]][coord[1]] = 'x'
                    self.nextTarget.alive = False
                    current = self.nextTarget
                    while current.alive == False:  # Uses a node like implementation to find the next target for the player to be fired at who's alive
                        current = current.nextTarget
                    self.nextTarget = current
                else:
                    self.message = self.message + "... and Missed!"
                    self.nextTarget.board[coord[0]][coord[1]] = 'o'
                break

    def clear(self):  # Clears the individual player's board
        for y in range(self.length):
            for x in range(self.length):
                if self.board[y][x] != '.':
                    self.board[y][x] = '.'
        self.alive = True
        self.chooseStart()
        self.targets = []
        self.setTargets()

    def setTargets(self):  # Creates all the valid coordinates that some other player can choose to attack this player
        for y in range(self.length):
            for x in range(self.length):
                self.targets.append([y, x])


if __name__ == "__main__":
    logging.basicConfig(filename='logfile.log', level=logging.INFO)  # creates a log file with the level set to info

    # create a game object and start the game by calling playGame()
    game = Game()
    game.playGame()
