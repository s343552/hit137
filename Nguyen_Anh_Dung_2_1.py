####################
# Student Name: Nguyen, Anh Dung
# Student ID: 343552
# Group: Anh (Solo)
# Subject: Assignment 2 - Question 1
####################

import tkinter
import tkinter.ttk as exTk
import turtle
from random import randint


def start_draw():
    # Temporary disable the buttons
    startButton['state'] = tkinter.DISABLED
    stopButton['state'] = tkinter.DISABLED

    # Fastest speed for testing purpose:
    # turtle.speed('fastest')

    # Set the color for turtle pen
    turtle.pencolor('#688335')

    # Set the size for turtle pen
    turtle.pensize(width=1)

    # Starting to draw a Christmas tree
    # First, move turtle to the base
    turtle.pendown()

    # Creating branches
    # The root
    turtle.left(90)
    turtle.forward(75)

    # First branch
    triangle(125)
    unturtle()

    # Second branch
    triangle(100)
    unturtle()

    # Third branch
    triangle(75)
    unturtle()

    # Fourth branch
    triangle(50)

    # Move turtle to the top
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.backward(25)

    # Thus, raw a star on the top
    turtle.pendown()
    star()
    turtle.hideturtle()

    # Small stars
    small_stars()

    # Re-enable the disabled buttons
    startButton['state'] = tkinter.NORMAL
    stopButton['state'] = tkinter.NORMAL


def clear_draw():
    # Temporary disable the buttons
    startButton['state'] = tkinter.DISABLED
    stopButton['state'] = tkinter.DISABLED

    # Clear the drawn lines
    turtle.clear()
    turtle.reset()
    # Penup before moving the turtle
    turtle.penup()
    # Move the turtle to starting point
    turtle.goto(0, -200)

    # Re-enable the disabled buttons
    startButton['state'] = tkinter.NORMAL
    stopButton['state'] = tkinter.NORMAL


def triangle(x):
    # Set to fill the green colour inside drawn triangles
    turtle.fillcolor('green')
    # Start filling the color
    turtle.begin_fill()

    # Begin to move the turtle
    turtle.right(90)
    turtle.forward(x)

    turtle.left(120)
    turtle.forward(x * 2)

    turtle.left(120)
    turtle.forward(x * 2)

    turtle.left(120)
    turtle.forward(x)

    # Stop filling the color
    turtle.end_fill()


def star():
    # Set to fill the yellow colour inside drawn star
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    # Start filling the color
    turtle.begin_fill()

    # Draw the star
    for i in range(5):
        turtle.forward(50)
        turtle.right(144)

    # Stop filling the color
    turtle.end_fill()


def unturtle():
    # Use penup & pendown to move turtle to the coordinator, without leaving traces
    turtle.penup()
    turtle.left(90)
    turtle.forward(75)
    turtle.pendown()


def small_stars():
    # Creating small stars at random position
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    turtle.speed('fastest')

    for position in range(55):
        turtle.penup()
        turtle.goto(randint(-300, 300), randint(-100, 220))
        turtle.pendown()

        for side in range(5):
            turtle.left(144)
            turtle.forward(10)


# Start tkinter window
window = tkinter.Tk()

# Create the buttons to control the drawing process
# by using exTk for better visual
startButton = exTk.Button(window, text='Start', command=start_draw)
stopButton = exTk.Button(window, text='Clear', command=clear_draw)

# Set the buttons by grid
startButton.grid(row=0, column=4, padx=10)
stopButton.grid(row=0, column=5, padx=10)

# Create the canvas for turtle screen
canvas = tkinter.Canvas(window, width=650, height=500)

# Set the canvas by grid
canvas.grid(row=1, columnspan=10)

# Set the bgcolor for turtle screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor('#87CEEB')
turtle = turtle.RawTurtle(screen)

turtle.penup()
turtle.goto(0, -200)

window.mainloop()
