# Programming Principles Quiz 4
# By: Christopher Aytona
import random

class Ticket(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def ShowNumbers(self):
        return (self.first, self.second)

class WinGen(Ticket):
    first = 0
    second = 0
    def __init__(self):
        self.first = random.randrange(20, 41)
        rand = random.randrange(20,41)
        while(self.first == rand):
            rand = random.randrange(20,41)
        self.second = rand

class Kiosk(WinGen):
    def Comparison(self):
        if super().first != self.first or super().second != self.second:
            return "Try Again"
        elif super().second != self.first or super().second != self.second:
            return "Try Again"
        return "Winner"

def main():
    while True:
        try:
            a_input = str(input("Would you like to manually input your numbers? (y/n)")).casefold()
            if a_input != "y" and a_input != "n":
                print("Invalid input")
                raise ValueError
            break
        except ValueError:
            pass
    if a_input == "n":
        a_rand = random.randrange(20,41)
        b_rand = random.randrange(20,41)
        while(a_rand == b_rand):
            b_rand = random.randrange(20,41)
    elif a_input == "y":
        while True:
            try:
                a_rand = int(input("First number: "))
                b_rand = int(input("Second number: "))
                if a_rand == b_rand:
                    print("Can't be the same number!")
                    raise ValueError
                elif a_rand < 20 or a_rand > 40 or b_rand < 20 or b_rand > 40:
                    print("Has to be between 20 and 40")
                    raise ValueError
                break
            except ValueError:
                pass

    a_ticket = Ticket(a_rand, b_rand)
    print(a_ticket.ShowNumbers())
    b_ticket = WinGen()
    print(b_ticket.ShowNumbers())
    compare = Kiosk()
    print(compare.Comparison())

main()