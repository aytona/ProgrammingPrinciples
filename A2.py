# Christopher Aytona
# Programming Principles: Assignment 2
# This program does both Part 1 and Part 2 of the assignment
# It also has the option to let the user define as much harmonics as they want and it will output the sum
import turtle, math, random

def initScreen(colour, maxAmp):
    """This function takes in a string for colour and int for maxAmp,
    it initializes the screen window and returns the screen object"""
    _wn = turtle.Screen()
    _wn.colormode(255)
    _wn.setworldcoordinates(0, -maxAmp - (maxAmp/10) , 550, maxAmp)
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
        while True:
            try:
                _harmonics.append((float(input('Amplitude of harmonic {}: '.format(i+1))), float(input('Frequency of harmonic {}: '.format(i+1)))))
                break
            except ValueError:
                pass
                print('Values must be in decimal format(can be float)')
            
    return _harmonics

def totalAmp(harmonic):
    """This program takes in the harmonics list,
    and adds all the amplitudes and returns it"""
    _allAmps = [x[0] for x in harmonic]
    _total = 0.0
    for i in range(len(_allAmps)):
        _total += _allAmps[i]
    return _total

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
            pass
            print('This colour is already used')

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
    for i in range(len(harmonic)):
        drawHarmonics(turtles[i+1], harmonic[i])
    sumHarmonic(turtles[0], harmonic)
        
def drawHarmonics(turt, harmonic):
    """This function takes in the turtle object, and the harmonic inputs
    to draw each individual harmonic"""
    for x in range(361):
        turt.goto(x, harmonic[0] * math.sin(math.radians(x * harmonic[1])))

def sumHarmonic(turt, harmonic):
    """This function is similar to drawHarmonics but instead of taking in a tuple,
    it will take in a list of tuples which is the list of amps and freqs inputs"""
    _amps = [amp[0] for amp in harmonic]
    _freqs = [freq[1] for freq in harmonic]
    turt.pensize(2)
    for x in range(361):
        y = 0
        for i in range(len(harmonic)):
            y += _amps[i] * math.sin(math.radians(x * _freqs[i]))
        turt.goto(x, y)

def sineDoubleFreq(amount):
    """This function creates a list of tuples that contains a specified amount of harmonics
    each harmonic's frequency is doubled, while its amplitude remains constant.
    It then returns the list of all harmonic tuples"""
    _harmonics = []
    for i in range(amount):
        _harmonics.append((100.0/(i+1.0)*2.0, (i + 1.0) * 2.0))

    return _harmonics

def assignmentEven(sColour, tColours):
    """This function executes part 1 of assignment 2"""
    _firstAmp = 1/3
    _secondAmp = 1/5
    _harmonics = [(1.0, 1.0), (_firstAmp, 3.0), (_secondAmp, 5.0)]
    _totalAmp = totalAmp(_harmonics)
    _wn = initScreen(sColour, _totalAmp)
    _turtleList = initTurtleList(len(_harmonics), tColours)
    drawSineWaves(_turtleList, _harmonics)
    writeFormulas(_harmonics, tColours, _totalAmp)
    return _wn

def assignmentOdd(sColour, tColours):
    """This function executes part 2 of assignment 2"""    
    _waveAmount = int(input('Amount of sine waves: '))
    _harmonics = sineDoubleFreq(_waveAmount)
    _totalAmp = totalAmp(_harmonics)
    _wn = initScreen(sColour, _totalAmp)
    _turtleList = initTurtleList(len(_harmonics), tColours)
    drawSineWaves(_turtleList, _harmonics)
    writeFormulas(_harmonics, tColours, _totalAmp)
    return _wn

def userHarmonics(sColour, tColours):
    """This function executes the program according to user inputs"""
    _numOfHarmonics = int(input('Number of harmonics: '))
    _harmonics = harmonicsInput(_numOfHarmonics)
    _totalAmp = totalAmp(_harmonics)
    _wn = initScreen(sColour, _totalAmp)
    _turtleList = initTurtleList(_numOfHarmonics, tColours)
    drawSineWaves(_turtleList, _harmonics)
    writeFormulas(_harmonics, tColours, _totalAmp)
    return _wn

def writeFormulas(harmonics, tColours, maxAmp):
    """This function writes out the formulas of each wave"""
    _amps = [amp[0] for amp in harmonics]
    _freqs = [freq[1] for freq in harmonics]
    _amps.insert(0, sum(_amps))
    _freqs.insert(0, sum(_freqs))
    _textBuffer = maxAmp/len(tColours)
    for i in range(len(tColours)):
        _turt = turtle.Turtle()
        _turt.hideturtle()
        _turt.color(tColours[i])
        _turt.penup()
        _turt.goto(375, maxAmp-_textBuffer-(_textBuffer*i))
        _turt.write('y={:g}sin({:g}f)'.format(round(_amps[i],3),round(_freqs[i],3)), align='left', font=('Arial', 14, 'normal'))


def main():
    programType = input('Welcome!\nType "even" for part 1 or "odd" for part 2.\nAny other input will let users add and define as much harmonics as they want.\nInput: ').lower()
    screenColour = input('Screen colour: ')
    wn = None
    turtleColours = [(0,0,0)]
    if programType == "even":
        wn = assignmentEven(screenColour, turtleColours)
    elif programType == "odd":
        wn = assignmentOdd(screenColour, turtleColours)
    else:
        wn = userHarmonics(screenColour, turtleColours)
    wn.exitonclick()

main()
