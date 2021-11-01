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
