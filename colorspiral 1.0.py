"""A module for drawing colorful spirals"""
import turtle
import random
import time


def cspiral(sides=6, size=360, x=0, y=0):
    """Draws a colorful spiral on a black background.

    Arguments:
    sides -- the number of sides in the spiral (default 6)
    size -- the length of the last side (default 360)
    x, y -- the location of the spiral, from the center of the screen
    sleep -- the number that program will wait for the users to look at the art (default 5)
    """
    t = turtle.Pen()
    t.speed(0)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    turtle.bgcolor("black")
    colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    for n in range(size):
        t.pencolor(colors[n%sides])
        t.forward(n*3/sides+n)
        t.left(360/sides+1)
        t.width(n*sides/100)


def random_spiral(number=10, sides_min=3, sides_max=6, size_min=25, size_max=75, x_min=-300, x_max=300, y_min=-300, y_max=300, sleep=5):
    """Draws some colorful spiral on a black background.

        Arguments:
        number -- the number of spiral (default 10)
        sides_min -- the number of least amount of sides in the spiral (default 3)
        sides_max -- the number of largest amount of sides in the spiral (default 6)
        size_min -- the number of least amount of length of the last side (default 25)
        size_max -- the number of largest amount of length of the last side (default 75)
        x_min, y_min -- the location of the spiral could least be (default -300)
        x_max, y_max -- the location of the spiral could largest be (default 300)
        sleep -- the number that program will wait for the users to look at the art (default 5)
        """
    t = turtle.Pen()
    t.speed(0)
    t.penup()
    turtle.bgcolor("black")
    colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    for a in range(number):
        sides = random.randint(sides_min, sides_max)
        size = random.randint(size_min, size_max)
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        t.setpos(x, y)
        t.pendown()
        for n in range(size):
            t.pencolor(colors[n % sides])
            t.forward(n * 3 / sides + n)
            t.left(360 / sides + 1)
            t.width(n * sides / 100)
        t.penup()
    time.sleep(sleep)
