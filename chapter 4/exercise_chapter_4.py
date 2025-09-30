# If you just want turtle graphics in PyCharm, you don’t need jupyturtle at all, as Python has a built-in turtle module.

import turtle

# Exerscise 1
# Draw a rectangle with given width and height using turtle graphics.
def rectangle (width, height):
    for i in range(2): #repeat twice
        turtle.forward(width)   #move forward by width
        turtle.left(90)         #turn 90 degrees
        turtle.forward(height)  #move forward by height
        turtle.left(90)         #turn 90 degrees



# Exercise 2
# Write a function called rhombus that draws a rhombus with a given side length and a given interior angle.
# For example with side length 50 and an interior angle of 60 degrees

import turtle

def rhombus(c, angle): #c is side length
    for i in range(2): #repeat twice
        turtle.left(angle)
        turtle.forward(c)
        turtle.left(180-angle)
        turtle.forward(c)



# Exercise 3
# Now write a more general function called parallelogram that draws a quadrilateral with parallel sides. Then rewrite rectangle and rhombus to use parallelogram.

GAP_SIZE=100                  # change this once to control all gaps at once

def parallelogram(a, b, angle):
     for i in range(2): #repeat twice
        turtle.forward(a)
        turtle.left(angle)
        turtle.forward(b)
        turtle.left(180-angle)


def gap(base_length):
    turtle.penup()
    turtle.setheading(0)        # always move horizontally
    turtle.forward(base_length + GAP_SIZE)    # move without drawing
    turtle.pendown()

def make_turtle():
    turtle.speed(0)             # fast
    turtle.hideturtle()         # hide cursor

    rectangle(80,40)            # first figure
    gap(80)                     # space between figures

    rhombus(50,60)              # second figure
    gap(50)                     # space between figures

    parallelogram(80, 50, 70)   # third figure
    gap(80)                     # space between figures



# Exercise 4
# Write an appropriately general set of functions that can draw shapes like this (many triangles in one)


import turtle
import math

def draw_triangle(side, angle, heading):    # Draw an isosceles triangle starting from the apex (top corner)
    base = 2 * side * math.sin(math.radians(angle / 2))
    base_angle = (180 - angle) / 2

    turtle.setheading(heading)         # face downward from the top (apex)

    turtle.forward(side)               # draw left side down
    turtle.left(180 - base_angle)      # turn to draw the base
    turtle.forward(base)               # draw the base
    turtle.left(180 - base_angle)      # turn up
    turtle.forward(side)               # draw right side up back to apex

def pie(side, angle):
    number_of_triangles = int(360 / angle)
    heading = -90
    for triangle in range(number_of_triangles):
        print(f"Triangle Number: {triangle} Heading: {heading}")
        draw_triangle(side, angle, heading)
        heading = heading + angle


# turtle.speed(10.0)                      # speed
# pie(100, 60)                            # example: side length 100, central angle 60 → 6 slices
# turtle.done()



# Exercise 5
# Write an appropriately general set of functions that can draw flowers like this.


import turtle

def draw_petal(radius, angle):                  # Draw one petal made of two circular arcs
    turtle.circle(radius, angle)                # First arc
    turtle.left(180 - angle)                    # Turn to mirror the arc for a petal shape
    turtle.circle(radius, angle)                # Second arc
    turtle.left(180 - angle)                    # Reorient to original heading for the caller


def flower(num_petals, radius, angle):          # define the flower outlook.
                                                # num_petals defines how many petals there will be drawn
    for petal in range(num_petals):             # repeats drawing the petals with the value defined in "num_petals"
        draw_petal(radius, angle)               # draw the first petal
        turtle.left(360 / num_petals)           # rotate to start the next petal

turtle.speed(10)
flower(num_petals=20, radius=50, angle=120)     # draw the flower
turtle.hideturtle()                             # hide the turtle
turtle.done()

"hej"