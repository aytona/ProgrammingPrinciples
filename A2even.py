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

def randomColour():
    """This function returns a random RGB colour tuple"""
    return (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

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

def checkColour(randColour, turtColours):
    """This function takes in the colour that needs to be checked,
    and the list of all current colours
    if it matches to another colour already generated, it creates a new colour
    if it doesn't then return the new turtle colour list with the new colour"""
    for r,g,b in turtColours:
        print(randColour)
        print(randColour[0])
        print(r)
        if turtColours[r] == randColour[0] and turtColours[g] == randColour[1] and turtColours[b] == randColour[2]:
            print('Same colour!')
            checkColour(randcomColour(), turtColours)
        else:
            turtColours.append(randColour)
            break;

def initTurtleList(num, colourList):
    """This function takes in the number of harmonics,
    and the list of colours
    It initializes the list of turtles used to draw each harmonic"""
    _turtleList = []
    for i in range(num):
        _colour = randomColour()
        checkColour(_colour, colourList)
        _turtleList.append(createTurtle(colourList[-1]))

    return _turtleList

def main():
    random.seed(1000)
    screenColour = input('Screen colour: ')
    numOfHarmonics = int(input('Number of harmonics: '))
    turtleColours = [(0,0,0),(255,0,0),(42,136,250)]
    #harmonics = harmonicsInput(numOfHarmonics)
    wn = initScreen(screenColour, 100)
    turtleList = initTurtleList(numOfHarmonics, turtleColours)
    turtleColours.sort()
    for r,g,b in turtleColours:
        print (r,g,b)
    #wn.exitonclick()

main()
