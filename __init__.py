from character import rolldice
from character import charater
from random import *

class Character:
    def __init__(self,name = "", str = [0,0], dex = [0,0], con= [0,0] , int = [0,0] , wis = [0,0], cha = [0,0], proficiency = 0, speed = 0, AC = 0, initiative = 0, hitpoints = 0):
        self.name = name
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.proficiency = proficiency
        self.speed = speed
        self.AC = AC
        self.initiative = initiative
        self.hitpoints = hitpoints

    def create(self):
        self.name = input("Name of Character: ")
        self.str = input("[Strength, Strength Modifier]: ")
        self.dex = input("[Dexterity, Dexterity Modifier]: ")
        self.con = input("[Constitution, Constitution Modifier]: ")
        self.int = input("[Intelligence, Intelligence Modifier]: ")
        self.wis = input("[Wisdom, Wisdom Modifier]: ")
        self.cha = input("[Charisma, Charisma Modifier]: ")
        self.proficiency = input("Proficiency: ")
        self.speed = input("Speed: ")
        self.AC = input("Armor Class: ")
        self.initiative = input("Initiative: ")
        self.hitpoints = input("Hit Points: ")

    def update(self, value, change):
        if value == "name":
            self.name = change
        if value == "strength":
            self.str = change
        if value == "dexterity":
            self.dex = change
        if value == "constitution":
            self.con = change
        if value == "intelligence":
            self.int = change
        if value == "wisdom":
            self.wis = change
        if value == "charisma":
            self.cha = change
        if value == "proficiency":
            self.proficiency = change
        if value == "speed":
            self.speed = change
        if value == "armor class":
            self.AC = change
        if value == "initiative":
            self.initiative = change
        if value == "hit points":
            self.hitpoints = change

    def view(self):
        print("Character Information \n",
              "Name of Character: ", self.name, "\n",
              "Strength, Modifier: ", self.str, "\n",
              "Dexterity, Modifier: ", self.dex, "\n",
              "Constitution, Modifier: ", self.con, "\n",
              "Intelligence, Modifier: ", self.int, "\n",
              "Wisdom, Modifier: ", self.wis, "\n",
              "Charisma, Modifier: ", self.cha, "\n",
              "Proficiency: ", self.proficiency, "\n",
              "Speed: ", self.speed, "\n",
              "Armor Class: ", self.AC, "\n",
              "Initiative: ", self.initiative, "\n",
              "Hit Points: ", self.hitpoints, "\n")

class rolldice:
    def __init__(self, sides = 20, times = 1):
        self.sides = sides
        self.times = times

    def rolld4(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 4)
            values.append(x)

        return values

    def rolld6(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 6)
            values.append(x)

        return values
    def rolld8(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 8)
            values.append(x)

        return values
    def rolld10(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 10)
            values.append(x)

        return values
    def rolld12(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 12)
            values.append(x)

        return values
    def rolld20(self, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, 20)
            values.append(x)

        return values
    def rolldX(self, sides = 20, times = 1):
        values = []
        for _ in range(times):
            x = randint(1, sides)
            values.append(x)

        return values
