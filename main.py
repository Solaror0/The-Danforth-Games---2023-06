import pygame
import sys
import screenfunctions as screenf
import config
pygame.init()
import objects as obj

#Header: Jun Nur and Farill's python game, "The Danforth Games"
#Name: Jun Nur Mustaqeem, Farill Arad
#Date: 2023-06-01
#Project Name: Culminating Project
#Project des: We've been assigned to create a Python olympic game. 
# It has to have 30 questions minimum, and the questions should be 
# related to the course content we learned throughout the semester for ICS3U.
#  We decided to have three difficulties, 
# Easy being 36 questions, Medium being 45 questions, Hard being 54 questions. 
# It is a three player game, and each sections' questions (Digital Information, Decis  ion Structures, Repetition Structures) 
# are divided evenly between the three players to answer.

#last edit date: 2023-06-14
#ethics: Jun Nur & Farill did indeed code this





# ##Read comments in config.py, main.py, then obj.py and screenfunctions.py (will inevitably need to alternate) for best understanding

config.screenSetup() ##runs a function that defines screen size, colour, and variables to use universally



screenf.startScreen() ##goes through the start screen, difficulty menu, and name input screesn respectively
screenf.difficultyMenu()

for config.PlayerTurnIterator in range(3):
    screenf.nameInput()


config.masterBoolean = True
config.text = ""


for config.zoneIterator in range(3):
     ##questionRun depends on the mode selected but during easy its 4, meaning it goes through the 3 players 4 times then changes the set
     ##of questions
    
    screenf.digitalInformationScreen()
    screenf.figureOutDictionary() ##sets dictionary based on the zone iterator(which changes every x questions based on difficulty)
    for j in range(config.questionRun):
        for config.PlayerTurnIterator in range(3):
            screenf.digitalInformationQuestions()
            print(config.playerPoints)
    screenf.pointShowScreen() ##shows the screen of points every zone

screenf.winnerShowScreen() ##finds winner and displays
screenf.winnerShowScreenTwo()
obj.leaderboardWrite()
pygame.quit()   

 ##update leaderboard