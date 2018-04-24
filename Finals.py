# Programming Principles Finals
# By: Christopher Aytona
class BoxMaker(object):
    pass

class CubeForm(BoxMaker):
    def Modify_Value(self):
        side_value = int(input("Enter the value of one side: "))
        return side_value

class TotalSize(CubeForm):
    def __init__(self, name):
        self.box = name
        self.side_value = super().Modify_Value()
    def SurfaceArea(self):
        self.materials = 6 * self.side_value * self.side_value
        output = ("The total material surface is: ", self.materials)
        print(output)

if __name__ == "__main__":
    box_name = TotalSize('a box')
    print(box_name.box)
    box_name.SurfaceArea()