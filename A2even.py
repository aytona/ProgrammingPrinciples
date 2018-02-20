# Christopher Aytona
# Programming Principles: Assignment 2 - Even
# This program draw x amount of harmonics and add them together
import turtle, math, random, threading

def initScreen(colour, maxAmp):
    """This function takes in a string for colour and int for maxAmp,
    it initializes the screen window and returns the screen object"""
    _wn = turtle.Screen()
    _wn.colormode(255)
    _wn.setworldcoordinates(0, -maxAmp - 1, 370, maxAmp)
    while True:
        try:
            _wn.bgcolor(colour)
            break
        except:
            pass
        colour = input('Invalid screen colour!\nNew colour: ')
    
    return _wn

def createTurtle(colour):
    """This function takes in a string param for turtle colour
    and returns a turtle object"""
    _turtle = turtle.Turtle(shape='turtle')
    _turtle.color(colour)
    return _turtle

def harmonicsInput(num):
    """This function iterates through each harmonic to get its amplitude and frequency,
    it then returns an array of tuples containing these information"""
    _harmonics = []
    for i in range(num):
        _harmonics.append((int(input('Amplitude of harmonic {}: '.format(i+1))), int(input('Frequency of harmonic {}: '.format(i+1)))))
    return _harmonics

def getMaxAmp(harmonic):
    """This program takes in the harmonics list,
    and returns the highest value amplitude"""
    return max([x[0] for x in harmonic])

def generateColour(turtColours):
    """This function takes in the list of already used colours,
    and generates a random colour that hasn't been used yet"""
    while True:
        try:
            _newColour = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
            if _newColour in turtColours:
                raise Exception
            else:
                turtColours.append(_newColour)
                break
        except Exception:
            print('This colour is already used')
            pass

def initTurtleList(num, colourList):
    """This function takes in the number of harmonics,
    and the list of colours
    It initializes the list of turtles used to draw each harmonic"""
    _turtleList = []
    for i in range(len(colourList)):
        _turtleList.append(createTurtle(colourList[i]))
    for i in range(num):
        generateColour(colourList)
        _turtleList.append(createTurtle(colourList[-1]))

    return _turtleList

def drawSineWaves(turtles, harmonic):
    """This function takes in the list of turtle objects and draw the sine waves"""
    fundamental = threading.Thread(target=drawHarmonics, args=(turtles[1], (1,1)))
    fundamental.start()
    for i in range(len(harmonic)):
        _newHarmonic = threading.Thread(target=drawHarmonics, args=(turtles[i+2], harmonic[i]))
        _newHarmonic.start()

def drawHarmonics(turt, harmonic):
    """This function takes in the turtle object, and the harmonic inputs
    to draw each individual harmonic"""
    for x in range(361):
        turt.goto(x, harmonic[0] * math.sin(math.radians(x * harmonic[1])))

def main():
    screenColour = input('Screen colour: ')
    numOfHarmonics = int(input('Number of harmonics: '))
    turtleColours = [(0,0,0),(255,0,0)]
    harmonics = harmonicsInput(numOfHarmonics)
    wn = initScreen(screenColour, getMaxAmp(harmonics))
    turtleList = initTurtleList(numOfHarmonics, turtleColours)
    drawSineWaves(turtleList, harmonics)
    wn.exitonclick()

main()
