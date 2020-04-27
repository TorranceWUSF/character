from random import *

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