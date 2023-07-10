import pygame
import sys
import screenfunctions as screenf
import config

running = True ## This is a variable that each screen uses for their respective "while" statements, which are necessary because
                ##pygame needs to keep running and refreshing every surface(an object) for it to run properly
            
masterBoolean = True ##A convenient boolean that can be accessed anywhere 

masterTimer = int ##The variable used to keep track of the timer(will see in the later parts of screenfunctions)
timerDown = pygame.USEREVENT+1 ##An pygame event, in screenfunctions when this is detected the mastertimer gets put down by 1
##An event is like when you send out a broadcast or frequency and something else picks it up and does something

correctAnswer = pygame.USEREVENT+2
incorrectAnswer = pygame.USEREVENT+3 ##pygame events to broadcast correct answers

##events might seem reduntant (if you run an event when something happens, why not just run a function?) but sometimes 
##when running a function, it messes with built-in necessary events(namely, the quit event aka the x button) or it slows the code down 
##so events are safer to check through all at once at some point in the while loop


##Dictionary/Question Answer variables
listOfOptions = [] ##setting up a variable for the options in a question
answer = "" ##answers in the question (check dictionaries for clarification)

text = "" 
inputActive = True ##these two variables are important for the obj.text, the text is how the object knows what to display
        ##it is a config so you can always edit it and therefore change the text without needing to type (like refreshing the text every screen)

        ##inputActive is a boolean that turns False after the enter button is clicked, allowing no further text entry
        ##it is a universal variable so at the same time other processes(namely, checking the text) can know when to run

        ##check obj.text for clarification

difficulty = "easy"  ##difficulty variable, set as default easy just incase 
dictionaryHolder = dict ##universal variable for accessing the dictionary

PlayerTurnIterator = 0 ##In main.py this is used as an iterator value, so the program knows which player loop it is
zoneIterator = 0 ##Same thing but for zones(the three types of questions)

playerPoints = [0,0,0] #  ##player point & name storage

PlayerNames = ["HolderOne","HolderTwo","HolderThree"]


def screenSetup():
    global SCREEN_WIDTH,screen,SCREEN_HEIGHT
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 750
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    screen.fill((0,0,0)) ##sets up screen to be used everywhere

questionRun = 4 ##check main.py, the default amount of questions to run per player, changes based on difficulty

def screenGoAway():
    screen.fill("black")  ##a function used sometimes to reset the screen
