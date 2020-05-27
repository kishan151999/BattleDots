
HOW TO START THE PROGRAM:

	To run this code in linux, type the following command line in the terminal once you are in the directory of location where main.py is located: python3 main.py

	The script will then ask the user to enter how many players are going to play the game. The user then should enter how many players they want, this should be a integer value.

	The game will begin to play itself after the amount of players is entered. 

	The game information will then be logged into the logfile that is created.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

HOW TO COUNTINUE THE PROGRAM OR ADD A NEW PLAYER:
	
	Once a winner has been decided the script will ask the user if they want to play again, if the user decides they want to play again
	
	they should enter one of the following: 'y' , 'yes'. If the user decides they do not want to play again they should enter 

	one of the following: 'n' , 'no'.  


	If user wants to keep playing then they will also be asked if they want to add an additional player.

	If the user wants to add an additional player then they should type one of the following: 'y' , 'yes' when asked if they want to add an additional player. 

	If the user does not want to add an additional player then they should type one of the following: 'no' , 'n'.

	If the user chooses to add an additional player then the user chooses the two people the new player is beside. Both first and second players to be beside should be integers. 

	The user can play the game as many times as they want and can add an additional player each time a new game is started. 
		
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

INTERPRETATION OF RESULTS / LOGFILE INFORMATION:

	The logfile will include the current round, and which player is attacking the other player.

	It will also include the position on the 10 x 10 grid the attack was made, and also if the attack missed or hit the enemy.
	
	It will also display the current grid of each player. Each players grid will be marked with '.' if that position was not attacked, a 'o' if that position was attacked but

	was not the location of the ship, and a 'x' if the position was attacked and it was the ships location. 

	Under each players grid it will also display if the respective player is currently dead or alive. 
	
	When the game finishes the logfile will also include the winner of the game and a thank you message.


	If the user plays a new round the game will restart and all the grids will reset. The logfile will not reset and will have the information from the previous game and current game.

	If the user plays a new round with an additional player then the new round will have an additional grid and the additional player will be between the specified players.


	In case logfile is not displayed properly please zoom out to see all the grids correctly. 





	
