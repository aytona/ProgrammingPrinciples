# Programming Principles Assignment 4
# By: Christopher Aytona
import string, random

class Grand_Parent(object):
    def __init__(self, name, chrom_num=12):
        self.name = name
        self.chrom_num = chrom_num
        count = 0
        self.chromosomes = []
        while count < chrom_num:
            rand_char = random.choice(string.ascii_letters)
            if 'x' not in rand_char.casefold() or 'z' not in rand_char.casefold():
                self.chromosomes.append(rand_char)
                count += 1

    def Get_Chromosomes(self):
        return self.chromosomes

    def Get_Name(self):
        return self.name

    def Pass_Chromosomes(self, num):
        temp = self.chromosomes[:]
        count = 0
        passed = []
        while count < num:
            rand_index = random.randrange(0, len(temp))
            passed.append(temp[rand_index])
            del temp[rand_index]
            count += 1
        return passed

class Parent(Grand_Parent):
    def __init__(self, name, parents):
        self.parents = parents
        self.name = name
        self.chromosomes = self.Inherit_Chromosomes()
        
    def Inherit_Chromosomes(self):
        return self.parents[0].Pass_Chromosomes(6) + self.parents[1].Pass_Chromosomes(6)

    def Get_Parent(self):
        return self.parents

class Children(Parent):
    pass

if __name__ == "__main__":
    GrandMother = Grand_Parent("GrandMother")
    GrandFather = Grand_Parent("GrandFather")
    GrandMa = Grand_Parent("GrandMa")
    GrandPa = Grand_Parent("GrandPa")
    Mother = Parent("Mother", (GrandMother, GrandFather))
    Father = Parent("Father", (GrandPa, GrandMa))
    Child = Children("Child", (Mother, Father))
    print(GrandMother.Get_Name() + ": " + str(GrandMother.Get_Chromosomes()))
    print(GrandFather.Get_Name() + ": " + str(GrandFather.Get_Chromosomes()))
    print(GrandMa.Get_Name() + ": " + str(GrandMa.Get_Chromosomes()))
    print(GrandPa.Get_Name() + ": " + str(GrandPa.Get_Chromosomes()))
    print(Mother.Get_Name() + ": " + str(Mother.Get_Chromosomes()))
    print(Father.Get_Name() + ": " + str(Father.Get_Chromosomes()))
    print(Child.Get_Name() + ": " + str(Child.Get_Chromosomes()))