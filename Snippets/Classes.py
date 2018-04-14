import math
class SomeClass(object):
    instConst = 999
    def __init__(self, temp, x, y):
        const = 123
        tempConst = 456
        self.tempConst = temp
        self.x = x
        self.y = y
        print(SomeClass.instConst)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self):
        result = math.hypot(self.x, self.y)
        return result

class Mother(object):
    colour = ""
    def __init__(self, name, colour):
        self.name = name
        Mother.colour = colour
        self.colour = Mother.colour
    def getName(self):
        return self.name
    def getColour(self):
        return self.colour

class Daughter(Mother):
    def __init__(self, name):
        self.colour = super().colour
        self.name = name

def main():
    omega = SomeClass(0,3,5)
    print(omega.tempConst)
    print(omega.x)
    print(omega.y)

    pointy = Point(5,10)
    print(pointy.getX())
    print(pointy.getY())
    print(pointy.distance())

    a = Mother("Mom", "White")
    b = Daughter("Daughter")

    print(a.getName())
    print(a.getColour())
    print(b.getName())
    print(b.getColour())

main()