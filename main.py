# # import turtle as t
# #
# # joni_kura2 = t.Turtle()
# from turtle import Turtle
#
# joni_kura2 = Turtle()
# mango = Turtle()
# zhuri = Turtle()
#
# joni_kura2.shape("turtle")
# joni_kura2.color("medium aquamarine")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.backward(200)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.left(180)
# # timmy_the_turtle.setheading(0)

import turtle as t
import random

tim = t.Turtle()
# ######## Challenge 1 - Draw a Square ############
# for _ in range(4):
#     joni_kura2.forward(100)
#     joni_kura2.left(90)

########### Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


########### Challenge 3 - Draw Shapes ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(123):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

########### Challenge 5 - Spirograph ########
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
