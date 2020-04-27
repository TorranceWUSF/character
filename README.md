# character
A python package that can be used to create a simple D&D character

The two main classes of the package are character and rolldice 

Character can be used to create and manage the stats of a dungeons and dragons character 

The fist function "create()" takes in no arguments and brings up a series of prompts for the user to enter information about the character 
to be created. 

The update() function takes in two arugments: value and change. Value being the the stat to be updated and change being the desired update

For example: update("strength", 14) changes the value of strength on a character to 14

View is the last function of the character class 

view() displays the stats of the character created 


The second class rolldice allows a user to roll dice of any side. The generic sides given by the class are a 
four, six, eight, ten, twelve, and twenty side die

rolld4()
rolld6()
rolld8()
rolld10()
rolld12()
rolld20()

The arugment for each of these functions are the amount of times a user wants to roll the die. 

For example, rolld6(4) would roll 4 6-sided die

rolldX() works similar to the previous functions, however it takes in two functions. The first argument is the amount of sides a 
user wants to roll and the second being how many dice the user would like to roll 

rolldX(14,2) would roll 2 14-sided die

A file titled example.txt is included in the respository. This file contains stats for a sample character that can be created

