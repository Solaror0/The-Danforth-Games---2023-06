import objects as obj

import pygame
import sys
pygame.init()
import config
import random
import dictionaries as di ##import section wowow

def leaderboardShow():

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 750
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    screen.fill((0,0,0)) ##sets up screen to be used everywhere
    config.running = True

    while config.running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        sys.exit()
        ##BACKGROUND
        background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
        backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
        background.fill((237, 213, 92))
        config.screen.blit(background,backgroundCenter)   

        topThree = obj.leaderboardWrite()
        x = slice(-2)
        scoreOne = topThree[0]
        scoreOne = scoreOne.strip()

        scoreTwo = topThree[1]
        scoreTwo = scoreTwo.strip()

        scoreThree = topThree[2]
        scoreThree = scoreThree.strip()

        textOneSurf, textOneRect = obj.text(80,500,300,scoreOne,"#000000")
        textTwoSurf, textTwoRect = obj.text(80,500,400,scoreTwo,"#000000")                                  
        textThreeSurf, textThreeRect = obj.text(80,500,60,scoreThree,"#000000")
        config.screen.blit(textOneSurf, textOneRect)
        config.screen.blit(textTwoSurf, textTwoRect)
        config.screen.blit(textThreeSurf, textThreeRect)
        nextbuttonSurface, nextbuttonRect = obj.button(config.screen,"Next",250,config.SCREEN_HEIGHT-100,200,100,"#FFFFFF","#666666",obj.nextScreenButton)
        config.screen.blit(nextbuttonSurface, nextbuttonRect)
        pygame.display.flip()
def startScreen():

        while config.running: ##keeps refreshing while this runs, important so all the active objects work(buttons)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit() ##checks through all the events for a quit event, if it is detected it goes blam(quits)

                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50)) #set to be a little smaller than the main screen
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2) ##places center
                ##here math needs to be done because pygame places the top left corner of the surface at your coordinates
                background.fill((237, 213, 92)) ##background = size, backgroundCenter(the second variable) = location

                # Creating the image surface
                image = pygame.image.load('Images\The Danforth Games.png') ##loads an image
                imagesize = (1006,457) ##sets the new size of the image
                image = pygame.transform.scale(image,imagesize) ##uses transform function to set it as so

                ##Button object, check obj.button
                nextbuttonSurface, nextbuttonRect = obj.button(config.screen,"Next",250,config.SCREEN_HEIGHT-200,200,100,"#FFFFFF","#666666",obj.nextScreenButton)   
                leaderBoardSurface,leaderBoardRect = obj.button(config.screen,"Leaderboard",475,config.SCREEN_HEIGHT-200,300,100,"#FFFFFF","#666666",leaderboardShow)

                # putting our image surface on display
                # surface
                config.screen.blit(background,backgroundCenter) 
                config.screen.blit(image,(-3,50))
                config.screen.blit(nextbuttonSurface,nextbuttonRect)
                config.screen.blit(leaderBoardSurface,leaderBoardRect) ##order matters here, like layers in photoshop

                ##these are all just advanced versions of rectangles, with the button rectangles behaving differently based on events
                ##config.screen.blit takes 1. The size of your rectangle(and other information like colour) and 2. its location

                pygame.display.update() ##updates the whole thing, would not display without it 



def difficultyMenu():
        config.running = True
        while config.running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                config.screenGoAway() ##refreshes screen

                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                rect = background.get_rect()

                easyButtonSurface, easyButtonRect = obj.button(config.screen,"Easy",100,200,200,100,"#FFFFFF","#5fe866",obj.easyButton)   
                mediumButtonSurface, mediumButtonRect = obj.button(config.screen,"Medium",100,350,200,100,"#FFFFFF","#f7ff03",obj.mediumButton)
                hardButtonSurface, hardButtonRect = obj.button(config.screen,"Hard",100,500,200,100,"#FFFFFF","#ff2003",obj.hardButton)
                

                easytext,easytextRect = obj.text(30,550,225,"Easy Mode: 30 Questions",'#000000')
                easytextTwo,easytextRectTwo = obj.text(30,500,275,"10 Questions Each","#000000") ##the obj.text function

                mediumtext,mediumtextRect = obj.text(30,575,375,"Medium Mode: 42 Questions",'#000000')
                mediumtextTwo,mediumtextRectTwo = obj.text(30,500,425,"14 Questions Each","#000000")

                hardtext,hardtextRect = obj.text(30,560,525,"Hard Mode: 54 Questions",'#000000')
                hardtextTwo,hardtextRectTwo = obj.text(30,500,575,"18 Questions Each","#000000")

                image = pygame.image.load('Images\Choose Your Difficulty.png')
                imagesize = (1006,457)
                image = pygame.transform.scale(image,imagesize)

                thermometer,x,y,bar,barRect = obj.difficultythermometer(800,50,267,700,100,25) ##displays a thermometer with a moving rectangle(check function)

                config.screen.blit(background,backgroundCenter)
                config.screen.blit(image,(-3,-125))
                config.screen.blit(easyButtonSurface,easyButtonRect)
                config.screen.blit(mediumButtonSurface,mediumButtonRect)
                config.screen.blit(hardButtonSurface,hardButtonRect)
                config.screen.blit(easytext,easytextRect)
                config.screen.blit(easytextTwo,easytextRectTwo)
                config.screen.blit(mediumtext,mediumtextRect)
                config.screen.blit(mediumtextTwo,mediumtextRectTwo)
                config.screen.blit(hardtext,hardtextRect)
                config.screen.blit(hardtextTwo,hardtextRectTwo)
                config.screen.blit(thermometer,(x,y))
                config.screen.blit(bar,barRect)
                pygame.display.update()
                
def nameInput():
        config.running = True
        while config.running:
                # for event in pygame.event.get():
                #         if event.type == pygame.QUIT:
                #                 pygame.quit()
                #                 sys.exit()


                config.screenGoAway()

                textbackground,textbackgroundCenter,text,text_surf,textRect = obj.inputBox(300,450,400,100,80,'#ffffff','Times New Roman','#000000')
                ##check obj.inputBox
                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                rect = background.get_rect()
                
                center = (config.SCREEN_WIDTH-background.get_width())/2

                displayText = "Player"+ str(config.PlayerTurnIterator+1)
                playerText,playerTextRect = obj.text(80,500,250,displayText, '#000000')
                otherText,otherTextRect = obj.text(40,500,350,"What is your name?","#000000")

            
                config.screen.blit(background,backgroundCenter)
                config.screen.blit(playerText,playerTextRect)
                config.screen.blit(otherText,otherTextRect)
                config.screen.blit(textbackground,textbackgroundCenter)
                config.screen.blit(text_surf,textRect) ##blits can be placed anywhere as long as they are in order

                config.PlayerNames[config.PlayerTurnIterator] = text

               
                if not(config.inputActive): ##every loop it checks if the player has stopped typing

                        if len(config.PlayerNames)!= len(set(config.PlayerNames)): ##if true, it checks through different conditions in the order of:
                               randomnumber = str(random.randint(0,9))             ##duplicate names, 0 characters, and over character limit, and displays the appropriate text
                               message = "Cannot have a duplicate name."+" Perhaps: " + text +randomnumber
                               correctionText,correctionTextRect = obj.text(20,500,650,message,'#ff0000')
                               config.screen.blit(correctionText,correctionTextRect)
                               pygame.display.update()
                               pygame.time.delay(3000)
                               config.inputActive = True                                
                        elif len(text)==0:
                               pass #put in text display of being more than 0 characters
                               correctionText,correctionTextRect = obj.text(20,500,650,"Your name must be more than 0 characters, retype in 3 seconds.",'#ff0000')
                               config.screen.blit(correctionText,correctionTextRect)
                               pygame.display.update()
                               pygame.time.delay(3000)
                               config.inputActive = True
                        elif len(text)>7:
                               pass #put in text display of being more than 0 characters
                               correctionText,correctionTextRect = obj.text(20,500,650,"Your name must be less than 7 characters, retype in 3 seconds.",'#ff0000')
                               config.screen.blit(correctionText,correctionTextRect)
                               pygame.display.update()
                               pygame.time.delay(3000)
                               config.inputActive = True
                        else:                              
                                continueButton, continueButtonRect = obj.button(config.screen,"Continue",400,625,200,100,"#FFFFFF","#1ed90d",obj.nextScreenButton,"#16de20")
                                config.screen.blit(continueButton,continueButtonRect)
                                pygame.display.update()

                pygame.display.update()

def digitalInformationScreen():
        
        if config.zoneIterator == 0:
                theImage = "Images\digitalInformation.png"
        if config.zoneIterator == 1:
                theImage = "Images\DecisionStructures.png"
        if config.zoneIterator == 2:
                theImage = "Images\RepetitionStructures.png" ##uses zoneIterator to see which part of the game its on to display the section
        
        config.running = True
        while config.running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                rect = background.get_rect()

                
                image = pygame.image.load(theImage)
                imageSize = (750,562)
                image = pygame.transform.scale(image,imageSize)


                
                text = ["Your competition is loading.","Your competition is loading..","Your competition is loading..."] ## acts like animation frames
                finishedText = "Your competition has loaded."  

                if config.masterBoolean:
                        for i in range(3):
                                for j in range(3):

                                        message = text[j] ##displays a string from the text list
                                        colour = '#000000'

                                        ##displays the text, waits for 500 ms and then
                                        loadingText,loadingTextRect = obj.text(50,500,650,message,colour)     
                                        config.screen.blit(loadingText,loadingTextRect)
                                        pygame.display.update()

                                        pygame.time.delay(500)

                                        loadingText.fill((237, 213, 92)) ##fills it with the same colour as the bg so it "disappears"
                                        config.screen.blit(loadingText,loadingTextRect) ##refreshes it so it registers

                                        config.screen.blit(background,backgroundCenter) ##reupdates the backgruond to refresh screen
                                        config.screen.blit(image,(125,34)) ##reupdates image so it appears otherwise it would be covered
                                        pygame.display.update() ##refresh screen

        

                                if i == 2:
                                        config.masterBoolean = False ##set this back in main  ##stops the loop from running after 9 animation frames

                else:             
                        loadingText,loadingTextRect = obj.text(50,500,650,finishedText,'#13d62a')  ##when masterBoolean is eventually stopped it displays the continue button  
                        continueButton, continueButtonRect = obj.button(config.screen,"Play!",400,525,200,100,"#FFFFFF","#a8ada9",obj.nextScreenButton,"#13d62a")
                        config.screen.blit(background,backgroundCenter)
                        config.screen.blit(image,(125,34))                      

                        config.screen.blit(loadingText,loadingTextRect)
                        config.screen.blit(continueButton,continueButtonRect) ##and then refreshes everything once more
                        pygame.display.update()                         

def figureOutDictionary():     

        if config.difficulty == "easy":
                questionDifficulty = 12 
        elif config.difficulty == "medium":
                questionDifficulty = 15
        elif config.difficulty == "hard":
                questionDifficulty = 18

        if config.zoneIterator == 0:
                config.dictionaryHolder = di.digital_info_questions_hard
        elif config.zoneIterator == 1:
                config.dictionaryHolder = di.decision_structure_questions_hard
        elif config.zoneIterator == 2:
                config.dictionaryHolder = di.repetition_structure_questions_hard 


        convertKeys = list(config.dictionaryHolder.keys())
        values = list(config.dictionaryHolder.values())
        dictionaryConvert = {}

        for i in range(questionDifficulty):
         dictionaryConvert[convertKeys[i]] = values[i]
        config.dictionaryHolder = dictionaryConvert

        ##checks for difficulty and chooses a dictionary based on that 

def digitalInformationQuestions(): ##check the dictionaries.py file so everything here makes sense whoever is reading this 
                                ##im pretending that someone other than ms.lal will actually read this

        ready = True ##A variable used inside the loop and then set to false so that a piece of code only runs once
        config.running = True
        config.dictionaryHolder = config.dictionaryHolder

        key = random.choice(list(config.dictionaryHolder.keys())) 
        ##accesses all the questions, important to do this way because the already-done questions(aka keys) will change

        questionIndex = key ##the question

        questionToDisplay = config.dictionaryHolder[questionIndex]['question'] ##accesses the question part of the key
        
        config.answer = config.dictionaryHolder[questionIndex]['answer'] #accesses the answer part, this needs to be accessed in other places

        trueOrFalse = False
        code = False
        shortAnswer = False ##the different types of questions

        questionFont = 20 ##default size

        print (list((config.dictionaryHolder[questionIndex].keys())))
        if "keywordThreshold" in list(config.dictionaryHolder[questionIndex].keys()): ##checks if theres this key in the question's keys (all of these question types have this key)
                config.masterTimer = 25 ##if so, it sets the timer to 25 and tells the code this for later
                shortAnswer = True
                config.inputActive = True #because this question will need typing, it activates the boolean which allows for it
                
        elif "code" in list(config.dictionaryHolder[questionIndex].keys()): ##checks for code snippet questions
                name = config.dictionaryHolder[questionIndex]['name']
                image = pygame.image.load(name)
                imagesize = (450,200)
                image = pygame.transform.scale(image,imagesize)
                imagePlace = ((150, config.SCREEN_HEIGHT-375))
                code = True
                config.listOfOptions = list(config.dictionaryHolder[questionIndex]['options'].keys()) ##accesses all the options for the mcq 
                random.shuffle(config.listOfOptions) ##randomizes it so all the button texts(seen later won't be in the same place always)
                option1 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[0]] ##sets the options to each str variable
                option2 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[1]] ##these will be displayed on the buttons
                option3 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[2]]
                option4 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[3]] 
                config.masterTimer = 22

        elif ("true" in config.dictionaryHolder[questionIndex]['keywords']) or ("false" in config.dictionaryHolder[questionIndex]['keywords']):
                config.listOfOptions = list(config.dictionaryHolder[questionIndex]['options'].keys())
                random.shuffle(config.listOfOptions)
                option1 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[0]]
                option2 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[1]]
                trueOrFalse = True
                config.masterTimer=12
                ##if true or fale it sets the buttons accordingly

        else:
                config.listOfOptions = list(config.dictionaryHolder[questionIndex]['options'].keys())
                random.shuffle(config.listOfOptions)  

                option1 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[0]]
                option2 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[1]]
                option3 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[2]]
                option4 = config.dictionaryHolder[questionIndex]['options'][config.listOfOptions[3]]
                config.masterTimer=17

                ##and the normal, multiple choice question

        displayNumber = str(config.masterTimer) #alternate variable for masterTimer that'll go into an obj.text function
                                                #cause i didnt wanna place a config. variable as a function input just in case..

        allowedToCheck = False ##Without this, the code sometimes skips past the questions and goes to the correct/incorrect screen between players
        ##I think it is because: The code checks for correct/incorrect answers through events, after the screen switches to the next player
        ##it runs the code really fast before the events are given a chance to update, and then sees the correct answer event 

        ##so, this variable is only set to true at the end of the loop so to allow for the events to refresh, and the if statement checking
        ##for the answer events wont run without this condition set to True

        pygame.time.set_timer(config.timerDown,1000)  ##begins a timer that triggers the timerDown event every 1000ms(1s)

        while config.running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                running = False
                                sys.exit()
                        if event.type == config.timerDown:
                                if config.masterTimer>=0:
                                        config.masterTimer-= 1
                                        displayNumber = str(config.masterTimer) ##timer down when the pygame timer counts 1 second
                                elif config.masterTimer <0:
                                        pygame.event.post(pygame.event.Event(config.incorrectAnswer)) ##if timer is 0 it goes incorrect

                        elif (event.type == config.correctAnswer) and (allowedToCheck): ##if correct
                                
                                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                                background.fill((237, 213, 92))                               
                                config.screen.blit(background,backgroundCenter)
                                correctText, correctTextRect = obj.text(80,500,375,"Correct!",'#a8ada9')
                                config.screen.blit(correctText,correctTextRect) ##it displays a "Correct!"
                                pygame.display.update()
                                config.playerPoints[config.PlayerTurnIterator]+=1 #and adds a point

                                pygame.time.delay(4000) #then it waits
                                config.running = False
                                
                        elif event.type == config.incorrectAnswer and (allowedToCheck):
                                
                                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                                background.fill((237, 213, 92))  
                                config.screen.blit(background,backgroundCenter) #same thing here except there is no point addition and its incorrect
                                incorrectText, incorrectTextRect = obj.text(80,500,375,"Incorrect.",'#f20707')
                                config.screen.blit(incorrectText,incorrectTextRect)
                                pygame.display.update()
                                pygame.time.delay(4000)
                                config.running = False



                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                config.screen.blit(background,backgroundCenter)
                rect = background.get_rect()
              #  pygame.display.update()
              
                timerText,timerTextRect = obj.text(80,910,80,displayNumber,"#FF0000") ##displays the timer after getting timer info
                
                config.screen.blit(timerText,timerTextRect)
                if ready:
                        message = "Get Ready:" + " Player " + config.PlayerNames[config.PlayerTurnIterator] ##This is before they get the question
                        getReady,getReadyRect = obj.text(20,500,375,message,'#000000')
                        config.screen.blit(getReady,getReadyRect)
                        
                        pygame.display.update()

                        pygame.time.delay(2000) #<-- Delay here

                        getReady,getReadyRect = obj.text(20,500,375,message,'#edd55c')
                        config.screen.blit(background,backgroundCenter)
                        pygame.display.update() ##its just a screen telling the user to get ready with a 2000ms delay
                        ready = False
       
       ## ASKING THE QUESTION PART STARTS, ABOVE PART WORKS FINE

                questionText,questionRect = obj.text(questionFont,500,275,questionToDisplay,"#000000")
                config.screen.blit(questionText,questionRect) ##QUESTION DISPLAY

                # if config.masterTimer>0:
                #  timer,timerRect = obj.timerText(910,80,80)
                #  config.screen.blit(timer,timerRect)

                ##BUTTONS | DEPENDING ON THE TYPE OF QUESTION IT DISPLAYS DIFFERENT THINGS
                if shortAnswer:
                        textbackground,textbackgroundCenter,text,text_surf,textRect = obj.inputBox(100,450,800,100,30,'#ffffff','Times New Roman','#000000')

                        config.screen.blit(textbackground,textbackgroundCenter)
                        config.screen.blit(text_surf,textRect)

                        if not(config.inputActive):

                                answerCorrect = obj.textAnswerCheck(text,questionIndex)
                                if answerCorrect:
                                        pygame.event.post(pygame.event.Event(config.correctAnswer))
                                else:
                                        pygame.event.post(pygame.event.Event(config.incorrectAnswer)) ##a text box and the question
                                config.text = "" ##it puts the text through a function, and then depending on the boolean it'll post an event
                elif code:
                        config.screen.blit(image,imagePlace)
                        firstbuttonSurface, firstbuttonRect = obj.button(config.screen,option1,650,config.SCREEN_HEIGHT-375,150,150,"#d13542","#666666",obj.answerButtonOne,fontSize = 19)   
                        secondbuttonSurface,secondbuttonRect = obj.button(config.screen,option2,810,config.SCREEN_HEIGHT-375,150,150,"#286ac8","#666666",obj.answerButtonTwo,fontSize = 19)   
                        thirdbuttonSurface, thirdbuttonRect = obj.button(config.screen,option3,650,config.SCREEN_HEIGHT-215,150,150,"#d29f36","#666666",obj.answerButtonThree,fontSize = 19)   
                        fourthbuttonSurface, fourthbuttonRect = obj.button(config.screen,option4,810,config.SCREEN_HEIGHT-215,150,150,"#498c2b","#666666",obj.answerButtonFour,fontSize = 19)  
                        config.screen.blit(firstbuttonSurface, firstbuttonRect)
                        config.screen.blit(secondbuttonSurface, secondbuttonRect)
                        config.screen.blit(thirdbuttonSurface, thirdbuttonRect)
                        config.screen.blit(fourthbuttonSurface, fourthbuttonRect) ##this is just buttons for code snippet questions

                elif trueOrFalse:   
                        firstbuttonSurface, firstbuttonRect = obj.button(config.screen,option1,195,config.SCREEN_HEIGHT-375,300,300,"#d13542","#666666",obj.answerButtonOne,fontSize = 30)   
                        secondbuttonSurface,secondbuttonRect = obj.button(config.screen,option2,505,config.SCREEN_HEIGHT-375,300,300,"#286ac8","#666666",obj.answerButtonTwo,fontSize = 30)
                        config.screen.blit(firstbuttonSurface, firstbuttonRect)  
                        config.screen.blit(secondbuttonSurface, secondbuttonRect) ##same thing for true and false,only showing two buttons
                else:
                        firstbuttonSurface, firstbuttonRect = obj.button(config.screen,option1,195,config.SCREEN_HEIGHT-375,300,150,"#d13542","#666666",obj.answerButtonOne,fontSize = 19)   
                        config.screen.blit(firstbuttonSurface, firstbuttonRect)

                        secondbuttonSurface,secondbuttonRect = obj.button(config.screen,option2,505,config.SCREEN_HEIGHT-375,300,150,"#286ac8","#666666",obj.answerButtonTwo,fontSize = 19)   
                        config.screen.blit(secondbuttonSurface, secondbuttonRect)
 
                        thirdbuttonSurface, thirdbuttonRect = obj.button(config.screen,option3,195,config.SCREEN_HEIGHT-215,300,150,"#d29f36","#666666",obj.answerButtonThree,fontSize = 19)   
                        config.screen.blit(thirdbuttonSurface, thirdbuttonRect)

                        fourthbuttonSurface, fourthbuttonRect = obj.button(config.screen,option4,505,config.SCREEN_HEIGHT-215,300,150,"#498c2b","#666666",obj.answerButtonFour,fontSize = 19)   
                        config.screen.blit(fourthbuttonSurface, fourthbuttonRect) ##and the default option with no indicator(hence the else, the 4 choice mcq)

                pygame.display.update()
                allowedToCheck = True

        del config.dictionaryHolder[questionIndex]


def pointShowScreen(): ##shows the points !!
        config.running = True

        while config.running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                running = False
                                sys.exit()
        ##BACKGROUND
                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                config.screen.blit(background,backgroundCenter)

                finishLines = pygame.image.load('Images\FinishLines.png')
                finishLinesLocation = ((0,50))
                linesImageSize = ((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                finishLines = pygame.transform.scale(finishLines,linesImageSize)
                config.screen.blit(finishLines,finishLinesLocation)


                totalQuestions = 3*config.questionRun
                playerOnePoints = config.playerPoints[0]
                playerTwoPoints = config.playerPoints[1]
                playerThreePoints = config.playerPoints[2]

                playerOneLength = (810/totalQuestions)*playerOnePoints
                playerTwoLength = (810/totalQuestions)*playerTwoPoints
                playerThreeLength = (810/totalQuestions)*playerThreePoints ##calculates how many pixels 1 point is valued based on how many questions the mode is and then multiplies it

        ##PlayerOnePlacement
                playerOneLine = pygame.Surface((playerOneLength,100)) ##thats applied to the length to be proportionate with point size
                playerOneLineRect = ((50,150))
                playerOneLine.set_alpha(128)
                playerOneLine.fill(('#fa393d'))
                onePointsText, onePointsTextRect = obj.text(80,125,200,str(playerOnePoints),"#000000")
                playerOneIcon = pygame.image.load('Images\PlayerOneIcon.png')
                playerOneLocation = ((playerOneLength,150)) ##and then the image is put at the end coordinate of said length to always be in front of the coloured line
                oneImagesize = (90,101)
                playerOneIcon = pygame.transform.scale(playerOneIcon,oneImagesize)
                
                config.screen.blit(playerOneLine,playerOneLineRect)
                config.screen.blit(playerOneIcon,playerOneLocation)
                config.screen.blit(onePointsText, onePointsTextRect)

        ##PlayerTwoPlacement
                playerTwoLine = pygame.Surface((playerTwoLength,100))
                playerTwoLineRect = ((50,300))
                twoPointsText, twoPointsTextRect = obj.text(80,125,350,str(playerTwoPoints),"#000000")
                playerTwoLine.set_alpha(128)
                playerTwoLine.fill(('#3964fa'))
                playerTwoIcon = pygame.image.load('Images\PlayerTwoIcon.png')
                playerTwoLocation = ((playerTwoLength,300))
                twoImagesize = (90,101)
                playerTwoIcon = pygame.transform.scale(playerTwoIcon,twoImagesize)

                config.screen.blit(playerTwoLine,playerTwoLineRect)
                config.screen.blit(playerTwoIcon,playerTwoLocation)
                config.screen.blit(twoPointsText, twoPointsTextRect)
        ##PlayerThreePlacement
                playerThreeLine = pygame.Surface((playerThreeLength,100))
                playerThreeLineRect = ((50,450))
                threePointsText, threePointsTextRect = obj.text(80,125,500,str(playerThreePoints),"#000000")
                playerThreeLine.set_alpha(128)
                playerThreeLine.fill(('#36f036'))
                playerThreeIcon = pygame.image.load('Images\PlayerThreeIcon.png')
                playerThreeLocation = ((playerThreeLength,450))
                threeImagesize = (90,101)
                playerThreeIcon = pygame.transform.scale(playerThreeIcon,threeImagesize)

                config.screen.blit(playerThreeLine,playerThreeLineRect)
                config.screen.blit(playerThreeIcon,playerThreeLocation)
                config.screen.blit(threePointsText,threePointsTextRect)

                continueButton, continueButtonRect = obj.button(config.screen,"Continue",400,625,200,100,"#FFFFFF","#1ed90d",obj.nextScreenButton,"#16de20")
                config.screen.blit(continueButton,continueButtonRect)

                pygame.display.flip()                




def winnerShowScreen():
        config.running = True

        while config.running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                running = False
                                sys.exit()
        ##BACKGROUND
                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                config.screen.blit(background,backgroundCenter)
                winnerText = "Time to find the winner..."
                displayTextOne = ""
                for i in range(len(winnerText)):
                        displayTextOne += winnerText[i]
                        firstText,firstTextRect = obj.text(50,500,375,displayTextOne,'#000000')
                        config.screen.blit(background,backgroundCenter)
                        config.screen.blit(firstText,firstTextRect)
                        pygame.display.update()
                        pygame.time.delay(100)

                winnerTextTwo = "Your winner is:"
                displayTextTwo = ""

                for i in range(len(winnerTextTwo)):
                        displayTextTwo += winnerTextTwo[i]
                        secondText,secondTextRect = obj.text(50,500,375,displayTextTwo,'#000000')
                        config.screen.blit(background,backgroundCenter)
                        config.screen.blit(secondText,secondTextRect)
                        pygame.display.update()
                        pygame.time.delay(100)
                
                pygame.time.delay(2000)

                config.screen.blit(background,backgroundCenter)
                pygame.display.update() 
                pygame.time.delay(1000)
                config.running = False   

def winnerShowScreenTwo():
        config.running = True

        while config.running:

        ##BACKGROUND
                background = pygame.Surface((config.SCREEN_WIDTH-50,config.SCREEN_HEIGHT-50))
                backgroundCenter = ((config.SCREEN_WIDTH-background.get_width())/2),((config.SCREEN_HEIGHT-background.get_height())/2)
                background.fill((237, 213, 92))
                config.screen.blit(background,backgroundCenter)
                winnerText = "Time to find the winner..."
                winningPoints = max(config.playerPoints)
                winnerIndex = []
                fontSize = 60
                for i in range(len(config.playerPoints)):
                        if config.playerPoints[i] == winningPoints:
                                winnerIndex.append(i)
                if len(winnerIndex)==1:
                        winnerDisplay = config.PlayerNames[winnerIndex[0]]
                elif len(winnerIndex) == 2:
                        winnerDisplay = config.PlayerNames[winnerIndex[0]] + " and " + config.PlayerNames[winnerIndex[1]]
                elif len(winnerIndex) ==3:
                        winnerDisplay = config.PlayerNames[winnerIndex[0]] + "," + config.PlayerNames[winnerIndex[1]] + "," + " and " + config.PlayerNames[winnerIndex[2]]
                        fontSize = 40

                thirdText,thirdTextRect = obj.text(40,500,375,winnerDisplay,'#000000')
                config.screen.blit(thirdText,thirdTextRect)
                pygame.display.flip()
                pygame.time.delay(3000)
                config.running = False
