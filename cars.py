from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


class Car(Turtle):
    def __init__(self, dir, lane):
        super().__init__()
        self.shape("square")
        self.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.penup()
        self.shapesize()
        self.setheading(180 if dir == 1 else 0)
        self.goto(300 if dir == 1 else -300, lane*70)
        self.speed("slowest")