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
            if 'x' not in rand_char.casefold() and 'z' not in rand_char.casefold():
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
        
    def Inherit_Chromosomes(self, chromo_amount=6):
        return self.parents[0].Pass_Chromosomes(chromo_amount) + self.parents[1].Pass_Chromosomes(chromo_amount)

    def Get_Parent(self):
        return self.parents

class Children(Parent):
    def GrandParent_Percentage(self, name):
        for i in range(2):
            for j in range(2):
                if super().Get_Parent()[i].Get_Parent()[j].Get_Name() == name:
                    tempSuperChromo = list(super().Get_Parent()[i].Get_Parent()[j].Get_Chromosomes())
                    for x in range(len(self.chromosomes)):
                        if self.chromosomes[x] in tempSuperChromo:
                           tempSuperChromo.remove(self.chromosomes[x]) 
                    return (len(self.chromosomes) - len(tempSuperChromo))/len(self.chromosomes)*100
    
    def Parent_Percentage(self, name):
        for i in range(2):
            if super().Get_Parent()[i].Get_Name() == name:
                tempSuperChromo = list(super().Get_Parent()[i].Get_Chromosomes())
                for x in range(len(self.chromosomes)):
                    if self.chromosomes[x] in tempSuperChromo:
                        tempSuperChromo.remove(self.chromosomes[x])
                return (len(self.chromosomes) - len(tempSuperChromo))/len(self.chromosomes)*100

if __name__ == "__main__":
    GrandMother = Grand_Parent("GrandMother")
    GrandFather = Grand_Parent("GrandFather")
    GrandMa = Grand_Parent("GrandMa")
    GrandPa = Grand_Parent("GrandPa")
    Mother = Parent("Mother", (GrandMother, GrandFather))
    Father = Parent("Father", (GrandPa, GrandMa))
    Child = Children("Child", (Mother, Father))
    print("{}: {}".format(GrandMother.Get_Name(), GrandMother.Get_Chromosomes()))
    print("{}: {}".format(GrandFather.Get_Name(), GrandFather.Get_Chromosomes()))
    print("{}: {}".format(GrandMa.Get_Name(), GrandMa.Get_Chromosomes()))
    print("{}: {}".format(GrandPa.Get_Name(), GrandPa.Get_Chromosomes()))
    print("{}: {}".format(Mother.Get_Name(), Mother.Get_Chromosomes()))
    print("{}: {}".format(Father.Get_Name(), Father.Get_Chromosomes()))
    print("{}: {}".format(Child.Get_Name(), Child.Get_Chromosomes()))
    print("{:g}% of chromosomes came from {}".format(round(Child.GrandParent_Percentage("GrandPa"),3), "GrandPa"))
    print("{:g}% of chromosomes came from {}".format(round(Child.GrandParent_Percentage("GrandMother"),3), "GrandMother"))