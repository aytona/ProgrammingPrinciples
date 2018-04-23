# Programming Principles Assignment 4
# By: Christopher Aytona
import string, random

class Grand_Parent(object):
    gene_pool_a = [letters for letters in string.ascii_lowercase if letters != 'x' and letters != 'z']
    gene_pool_b = [letters for letters in string.ascii_uppercase if letters != 'X' and letters != 'Z']
    
    def __init__(self, name, gender, chrom_num=12):
        self.name = name
        self.chrom_num = chrom_num
        count = 0
        self.chromosomes = []
        if gender.casefold() == "male":
            pool = Grand_Parent.gene_pool_a
        else:
            pool = Grand_Parent.gene_pool_b
        while count < chrom_num:
            rand_index = random.randrange(len(pool))
            self.chromosomes.append(pool[rand_index])
            del pool[rand_index]
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
        intersection = list(set(self.chromosomes) & set(alien.Get_Chromosomes()))
        return float(len(intersection))/float(len(self.chromosomes))

if __name__ == "__main__":
    GrandMother = Grand_Parent("GrandMother", "Female")
    GrandFather = Grand_Parent("GrandFather", "Male")
    GrandMa = Grand_Parent("GrandMa", "Male")
    GrandPa = Grand_Parent("GrandPa", "Female")
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
    print("{:.2%} of chromosomes came from {}".format(Child.Percentage(GrandPa), GrandPa.Get_Name()))
    print("{:.2%} of chromosomes came from {}".format(Child.Percentage(GrandMother), GrandMother.Get_Name()))