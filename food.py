import turtle
from turtle import Turtle
import random

colors = ["royal blue", "green", "gold", "dark orange", "red", "coral", "dark orchid", "medium slate blue"]
random_color = random.choice(colors)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random_color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
