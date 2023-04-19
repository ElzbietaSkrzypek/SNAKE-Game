from turtle import Turtle
import random
list_of_shape = ["turtle", "circle", "square"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(list_of_shape))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(list_of_shape))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

