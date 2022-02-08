import turtle


class Canvas:
    def __init__(self):
        self.turtle = turtle
        self.turtle.reset()
        self.turtle.hideturtle()
        self.turtle.tracer(0)
        self.turtle.screensize(6000, 2000)
        self.turtle.bgcolor('#000000')
        self.stack = []
