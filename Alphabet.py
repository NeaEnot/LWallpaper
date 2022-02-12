import turtle
import random


class MoveSymbol:
    def __init__(self, lmin, lmax, lkoef, thick, thick_koef, color):
        self.lmin = lmin
        self.lmax = lmax
        self.lkoef = lkoef
        self.thick = thick
        self.thick_koef = thick_koef
        self.color = color

    def execute(self, canvas):
        l = random.randint(self.lmin, self.lmax) * self.lkoef ** len(canvas.stack)
        t = self.thick * self.thick_koef ** len(canvas.stack)
        if t == 0:
            t = 1

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
        angle = random.uniform(self.amin, self.amax) * self.akoef ** len(canvas.stack)

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
        thick = random.randint(self.size_min, self.size_max)

        canvas.turtle.pencolor(self.color)
        canvas.turtle.pensize(thick)
        canvas.turtle.forward(thick)


class StubSymbol:
    def __init__(self):
        pass

    def execute(self, canvas):
        pass


class PushSymbol:
    def __init__(self):
        pass

    def execute(self, canvas):
        canvas.stack.append(turtle.xcor())
        canvas.stack.append(turtle.ycor())
        canvas.stack.append(turtle.heading())


class PopSymbol:
    def __init__(self):
        pass

    def execute(self, canvas):
        canvas.turtle.penup()
        canvas.turtle.setheading(canvas.stack.pop())
        canvas.turtle.sety(canvas.stack.pop())
        canvas.turtle.setx(canvas.stack.pop())
        canvas.turtle.pendown()


def generate_color():
    abc = '0123456789abcdef'

    color = '#'

    for i in range(6):
        ch = abc[random.randint(0, len(abc) - 1)]
        color += ch

    return color


class Alphabet:
    def __init__(self, nsymbols=0):
        abc = 'abcdefghijklmnopqrstuvwxyz'

        self.dict = {'[': PushSymbol(), ']': PopSymbol()}
        if nsymbols == 0:
            nsymbols = random.randint(2, 10)

        for i in range(nsymbols):
            ch = abc[random.randint(0, len(abc) - 1)]
            abc = abc.replace(ch, '')

            k = random.randint(0, 2)

            if k == 0:
                lmin = random.randint(15, 30)
                lmax = random.randint(lmin, int(lmin * 1.5))
                lk = random.uniform(0.7, 1)
                t = random.randint(4, 8)
                tk = random.uniform(0.5, 0.9)
                color = generate_color()

                self.dict.update({ch: MoveSymbol(lmin, lmax, lk, t, tk, color)})
                print(f'Symbol {ch}: move')

            if k == 1:
                direct = '+'
                amin = random.uniform(1, 90)
                amax = random.uniform(amin, 180)
                ak = random.uniform(0, 1.5)

                d = random.randint(0, 2)
                if d == 1:
                    direct = '-'

                self.dict.update({ch: TurnSymbol(direct, amin, amax, ak)})
                print(f'Symbol {ch}: turn')

            if k == 2:
                smin = random.randint(4, 8)
                smax = random.randint(smin, int(smin * 1.5))
                color = generate_color()

                self.dict.update({ch: LeafSymbol(smin, smax, color)})
                print(f'Symbol {ch}: leaf')

            if k == 3:
                self.dict.update({ch: StubSymbol()})
                print(f'Symbol {ch}: stub')
