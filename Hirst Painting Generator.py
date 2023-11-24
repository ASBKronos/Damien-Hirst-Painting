import colorgram
from turtle import Turtle, Screen
import random

color_list = colorgram.extract('Damien Hirst Painting - Flumequine.jpg',30)
rgb_colors = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r,g,b))

print(rgb_colors)

sam = Turtle()
screen = Screen()
screen.colormode(255)

screen.screensize(600,600,'lightgray')

sam.speed('fastest')
sam.penup()
sam.setx(-300)
sam.sety(-400)

for i in range(10):
    for j in range(10):
        sam.pendown()
        sam.dot(20,random.choice(rgb_colors))
        sam.penup()
        sam.forward(50)
    sam.sety(-200 + (50 * i+1))
    sam.setx(-225)

screen.exitonclick()

