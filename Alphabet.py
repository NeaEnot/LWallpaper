from random import random

class MoveSymbol:
    def __init__(self, lmin, lmax, lkoef, thick, thick_koef, color):
        self.lmin = lmin
        self.lmax = lmax
        self.lkoef = lkoef
        self.thick = thick
        self.thick_koef = thick_koef
        self.color = color

    def execute(self, canvas):
        l = random(self.lmin, self.lmax) * self.lkoef ** len(canvas.stack)
        t = self.thick * self.thick_koef ** len(canvas.stack)

        canvas.turtle.pencolor(self.color)
        canvas.turtle.pensize(t)
        canvas.turtle.forward(l)

class TurnSymbol:
    def __init__(self, direction, amin, amax, akoef):
        self.direction = direction
        self.amin = amin
        self.amax = amax
        self.akoef = akoef

    def execute(self, canvas):
        angle = random(self.amin, self.amax) * self.akoef ** len(canvas.stack)

        if self.direction == '+':
            canvas.turtle.right(angle)
        elif self.direction == '-':
            canvas.turtle.left(angle)

class LeafSymbol:
    def __init__(self, size_min, size_max, color):
        self.size_min = size_min
        self.size_max = size_max
        self.color = color

    def execute(self, canvas):
        thick = random(self.size_min, self.size_max)
        l = random(self.size_min, self.size_max)

        canvas.turtle.pencolor(self.color)
        canvas.turtle.pensize(thick)
        canvas.turtle.forward(l)
