
import pygame
import sys
pygame.init()
import screenfunctions as screenf
font = pygame.font.SysFont('grand9kpixelregular', 40)
import config
objects = []
def nextScreenButton():
    config.running = False
    
    pygame.time.delay(200)
    config.text = ""
    config.inputActive = True ##sets config.running to false and other things like text so everything stops and then moves to the next function

def correctAnswerButton():
     pygame.event.post(pygame.event.Event(config.correctAnswer))

def incorrectAnswerButton():
     pygame.event.post(config.incorrectAnswer) ##event posting
    

def text(fontSize,x,y,text = "Text",color = "#000000"):
    font = pygame.font.SysFont('grand9kpixelregular',fontSize)
    text = font.render(text,True,color)
    textRect = text.get_rect()
    textRect.center = (x,y)
    return text,textRect ##text function that just assigns text easily

def easyButton():
    config.running = False
    
    pygame.time.delay(200)
    config.difficulty = "easy"
    config.questionRun = 4


def mediumButton():
    config.running = False
    
    pygame.time.delay(200)
    config.difficulty = "medium"
    config.questionRun = 5

def hardButton():
    config.running = False
    
    pygame.time.delay(200)
    config.difficulty = "hard"
    config.questionRun = 6 ##button functions

def answerButtonOne():
     index = 0
     if config.listOfOptions[index] == config.answer:
        pygame.event.post(pygame.event.Event(config.correctAnswer))
     else:
        pygame.event.post(pygame.event.Event(config.incorrectAnswer))
def answerButtonTwo():
     index = 1
     if config.listOfOptions[index] == config.answer:
        pygame.event.post(pygame.event.Event(config.correctAnswer))
     else:
        pygame.event.post(pygame.event.Event(config.incorrectAnswer))
def answerButtonThree():
     index = 2
     if config.listOfOptions[index] == config.answer:
        pygame.event.post(pygame.event.Event(config.correctAnswer))
     else:
        pygame.event.post(pygame.event.Event(config.incorrectAnswer))
def answerButtonFour():
     index = 3
     if config.listOfOptions[index] == config.answer:
        pygame.event.post(pygame.event.Event(config.correctAnswer))
     else:
        pygame.event.post(pygame.event.Event(config.incorrectAnswer)) ##button functions for each mcq button that references their index value into the list to check against the answer


def button(screen,msg,x,y,w,h,ic,ac,action=None,textColor = '#000000',fontSize = 40):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.SysFont('grand9kpixelregular', fontSize)         
        buttonSurface = pygame.Surface((w, h))
        buttonRect = pygame.Rect(x,y,w,h)
        buttonSurf = font.render(msg, True, (textColor))

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            
            buttonSurface.fill(ac)
            if click[0] == 1 and action != None:
                action()         
        else:
            buttonSurface.fill(ic)

        buttonSurface.blit(buttonSurf, [
            buttonRect.width/2 - buttonSurf.get_rect().width/2,
            buttonRect.height/2 - buttonSurf.get_rect().height/2
            ])
        
        screen.blit(buttonSurface, buttonRect)
        return buttonSurface,buttonRect ##a button function that checks for mouse position, referencing against its own to know when hover
        ##it also uses that combined with the mouse click (line ~~80) to surmise that the button has been pressed

def difficultythermometer(x,y,imageW,imageH,barW,barH):
    x=x
    y=y
    ##if the x or y variable changes then so should the position as long as its in a loop - Jun Nur
    mousex, mousey = pygame.mouse.get_pos()
    thermometer = pygame.image.load('Images\GameThermometer.png')
    thermometerSize = (imageW,imageH)
    thermometer = pygame.transform.scale(thermometer,thermometerSize)

    bar = pygame.Surface((barW,barH))
    barRect = ((x,mousey)) ##the thermometer bar is set to move along with the mousey

    return thermometer,x,y,bar,barRect



def inputBox(x,y,width,height,textSize,backgroundColour = 'colour',textFont = 'another', textColour = 'm'):
        background = pygame.Surface((width,height))
        backgroundCenter = ((x,y))
        background.fill(backgroundColour)
        font = pygame.font.SysFont(textFont,textSize)

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit
                sys.exit
             elif event.type == pygame.KEYDOWN and config.inputActive: ##checks if event is keydown and if its allowed to check for the keys(inputActive)
                  if event.key == pygame.K_RETURN:
                       config.inputActive = False ##turns off text ox
                  elif event.key == pygame.K_BACKSPACE: 
                       config.text = config.text[:-1] ##checks through the enter and backspace key before 
                  else: 
                       config.text += event.unicode ##inputting in the text

        text_surf = font.render(config.text,True,(textColour)) ##displays the text which constantly updates and therefore looks like typing
        textRect = ((x,y))
        text = config.text
        return background,backgroundCenter,text,text_surf,textRect

def textAnswerCheck(text,questionIndex):

    answerCorrect = bool ##algorithm to check if a short answer is correct based on the keywordThreshold
    keywords = config.dictionaryHolder[questionIndex]['keywords']
    instantWrong = config.dictionaryHolder[questionIndex]['instantWrongs']
    keywordThreshold = config.dictionaryHolder[questionIndex]['keywordThreshold']
  
    threshHoldChecker = 0


    if text == instantWrong: ##it also goes through the instant wrong inputs first to not waste time (like using while in a for loop question)
        answerCorrect = False
    else: 
        for i in range(len(keywords)):
            if keywords[i] in text:
                threshHoldChecker+=1

                text = text.replace(keywords[i],"")
    
    if threshHoldChecker >= keywordThreshold:
        answerCorrect = True
    else:
        answerCorrect = False

    return answerCorrect

def leaderboardWrite():
    def read_scores_from_file(file_path):
        scores = {}  # Create an empty dictionary to store the scores
        with open(file_path, "r") as file:  # Open the file in read mode
            for line in file:  # Iterate over each line in the file
                player, score = line.strip().split(
                    ":")  # Split the line into player and score
                scores[player] = int(score)  # Add the player and score to the dictionary
        return scores  # Return the scores dictionary

    def write_scores_to_fileTwo(keys,values, file_path):
        with open(file_path, "w") as file:  # Open the file in write mode
            for i in range(len(keys)):  # Iterate over each player and score in the dictionary
                file.write(
                    f"{keys[i]}:{values[i]}\n")  # Write the player and score to the file
                
    newDict = {}
    filePath = "leaderboardRead.txt"
    scores = read_scores_from_file(filePath)
    scoreValues = list(scores.values())
    scoreKeys = list(scores.keys())
    newKeys = []
    for i in range(3):
     scoreValues.append(config.playerPoints[i]) ##adds the points to the lists
     scoreKeys.append(config.PlayerNames[i])

    oldValues = scoreValues ##stores the values
    scoreValues = sorted(scoreValues,reverse=True) ##then it sorts the values in reverse (high to low), but the scoreKeys list isnt sorted that way
                                                ##and cant be

    for i in range(len(scoreValues)):
        indexNumber = oldValues.index(scoreValues[i]) ##so it basically just checks for the index of the value in the oldValues list
        newKeys.append(scoreKeys[indexNumber]) ##and the index of the value in the oldvalue will be the correct index for the keys

    write_scores_to_fileTwo(newKeys,scoreValues, filePath) ##then it writes it in
    
    with open(filePath, "r") as file:  # Open the file in read mode
        topThree = file.readlines()[0:3]  #and it takes the top 3 the other are in there as well and it'll always get sorted 
    return topThree
