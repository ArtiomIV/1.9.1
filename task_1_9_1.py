import math
class Cyrcle:
    def __init__(self, radius = 0):
        self.radius = radius

    def setRadius(self, radius):
        if isinstance(radius, int):
            self.radius = radius
        else:
            return print("Введите число")

    def getCircleArea(self):
        return "Площадь круга: " + str(math.pi*self.radius**2)



