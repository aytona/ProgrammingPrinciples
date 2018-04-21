# Programming Principles Assignment 4
# By: Christopher Aytona
import string, random

class Grand_Parent(object):
    def __init__(self, name, upper, chrom_num=12):
        self.name = name
        self.chrom_num = chrom_num
        count = 0
        self.chromosomes = []
        while count < chrom_num:
            if upper:
                rand_char = random.choice(string.ascii_uppercase)
            else:
                rand_char = random.choice(string.ascii_lowercase)
            if 'x' not in rand_char.casefold() and 'z' not in rand_char.casefold():
                if rand_char not in self.chromosomes:
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
    def Percentage(self, alien):
        clone_alien = list(alien.Get_Chromosomes())
        union_list = []
        for i in range(len(self.chromosomes)):
            if self.chromosomes[i] in clone_alien:
                union_list.append(self.chromosomes[i])
                clone_alien.remove(self.chromosomes[i])
        return len(union_list)/len(self.chromosomes)

if __name__ == "__main__":
    GrandMother = Grand_Parent("GrandMother", False)
    GrandFather = Grand_Parent("GrandFather", False)
    GrandMa = Grand_Parent("GrandMa", True)
    GrandPa = Grand_Parent("GrandPa", True)
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
    print("{:.2%} of chromosomes came from {}".format(Child.Percentage(GrandPa), "GrandPa"))
    print("{:.2%} of chromosomes came from {}".format(Child.Percentage(GrandMother), "GrandMother"))