####################
# Student Name: Nguyen, Anh Dung
# Student ID: 343552
# Group: Anh (Solo)
# Subject: Assignment 2 - Question 2
####################

import turtle
from turtle import Shape
from PIL import Image, ImageTk
import tkinter
from tkinter import ttk
from random import randint
import tkinter.messagebox as box

userBalance = 1000


def information():
    # Enable button state & clear the previous game if available
    submitName['state'] = tkinter.DISABLED
    clear_game()
    result.delete(1.0, tkinter.END)

    # Validate entries and conditions
    if inputName.get() == '':
        box.showinfo('Error', 'Please enter your name.')
        inputName.focus_set()
    elif inputBet.get().isnumeric() is False:
        box.showinfo('Error', 'Please enter your bet (number only).')
        inputBet.focus_set()
    elif drop.get() == '':
        box.showinfo('Error', 'Please select the dog you want to place a bet on.')
        drop.focus_set()
    else:
        # Inherite the user balance from global variance
        global userBalance
        userBal = userBalance

        # Get name, bet amount and bet choice
        name = inputName.get()
        bet = inputBet.get()
        choice = drop.get()

        # The balance value in each round will be updated in the variable, for continuous use
        # The balance will only be reset to default value when user restart the program
        # Check if the user has enough balance to play
        if userBal < 1:
            box.showinfo('Error', 'You do not have enough money to play. Please restart the game.')

        else:
            # The game will start when all conditions are satisfied
            result.insert(1.0, f'Hello, {name}!\n')
            result.insert(2.0, f'You have {userBal}$ in your balance.\n')
            result.insert(3.0, f'You bet {bet}$ on {choice}.\n')

            # Create a pending balance
            pending_bal = userBalance - int(bet)

            # Start the race
            start_race(shibu, kiki, milu, kari)

            # Get the result from the race & insert to Text widget
            final_result = find_winner(shibu, kiki, milu, kari)
            result.insert(4.0, f'Winner is {final_result}.\n')

            # Compare the result with bet choice to decide the final balance
            if choice == final_result:
                # User will receive 5x of the bet amount
                won = (int(bet) * 5)
                userBalance = pending_bal + won
                # Update to the Text widget
                result.insert(5.0, f'Congrats! You won {won}$ this round.\n')

            else:
                # Bet amount deducted from user's balance & update to the Text widget
                result.insert(5.0, 'Sorry :( You lose this round.\n')
                userBalance = pending_bal

        # Insert final balance of user to Text widget
        result.insert(6.0, f'Your final balance is {userBalance}$.')

        # Enable button state
        submitName['state'] = tkinter.NORMAL


def register_PIL(name, image):
    # Function to use customised turtle icon
    photo_image = ImageTk.PhotoImage(image)
    shape = Shape('image', photo_image)
    screen._shapes[name] = shape


def clear_game():
    # Clear the drawn lines and set dogs' position
    shibu.clear()
    shibu.reset()
    shibu.penup()
    kiki.clear()
    kiki.reset()
    kiki.penup()
    milu.clear()
    milu.reset()
    milu.penup()
    kari.clear()
    kari.reset()
    kari.penup()
    shibu.setpos(-330, 160)
    kiki.setpos(-330, 50)
    milu.setpos(-330, -65)
    kari.setpos(-330, -180)


def find_winner(a, b, c, d):
    # Compare the score and get the winner
    if a.xcor() > b.xcor() and a.xcor() > c.xcor() and a.xcor() > d.xcor():
        # box.showinfo('Info', 'Winner is Shibu')
        return 'Shibu'
    elif b.xcor() > a.xcor() and b.xcor() > c.xcor() and b.xcor() > d.xcor():
        # box.showinfo('Info', 'Winner is Kiki')
        return 'Kiki'
    elif c.xcor() > a.xcor() and c.xcor() > b.xcor() and c.xcor() > d.xcor():
        # box.showinfo('Info', 'Winner is Milu')
        return 'Milu'
    else:
        # box.showinfo('Info', 'Winner is Kari')
        return 'Kari'


def start_race(a, b, c, d):
    # Racing movements
    for i in range(420):
        a.forward(randint(0, 3))
        b.forward(randint(0, 3))
        c.forward(randint(0, 3))
        d.forward(randint(0, 3))


# Create the tkinter main window
window = tkinter.Tk()

# Set fixed size
window.geometry('805x800')
window.resizable(False, False)
window.title('Doggolympics - 300m Short Track Race')
window.configure(bg='light green')

# Create labels for labels, entries and button
labelName = tkinter.Label(window, text='Enter name:', bg="light green")
inputName = tkinter.Entry(window, bg="light green")
inputName.insert(0, 'Dung Nguyen S343552')
labelBet = tkinter.Label(window, text='Enter bet ($):', bg="light green")
inputBet = tkinter.Entry(window, bg="light green")
inputBet.insert(0, 100)
labelDogs = tkinter.Label(window, text='Choose dog:', bg="light green")
dogs = ['Shibu', 'Kiki', 'Milu', 'Kari']  # Combobox menu options
drop = ttk.Combobox(window, values=dogs, state='readonly')  # Create Combobox menu
submitName = tkinter.Button(window, text="Let's Race!", width=18, height=2, command=information, bg="light green")
result = tkinter.Text(window, width=50, height=7, bg="light green", font=("Helvetica", 15))

# Set positions for labels, entries and button
labelName.grid(row=0, column=0, padx=50, pady=5)
inputName.grid(row=0, column=1, padx=5, pady=5)
labelBet.grid(row=1, column=0, padx=50, pady=5)
inputBet.grid(row=1, column=1, padx=5, pady=5)
labelDogs.grid(row=0, column=3, padx=20, pady=5)
drop.grid(row=0, column=4, padx=5, pady=5)
submitName.grid(row=1, column=4, padx=5, pady=5)
result.place(x=150, y=630)

# Focus on name entry and set default choice of combobox
inputName.focus_set()
drop.current(0)
result.config(state=tkinter.NORMAL)
submitName['state'] = tkinter.DISABLED

# A separator between above and beyond fields
sep = ttk.Separator(window).place(x=0, y=100, relwidth=1)

# Create a canvas for turtle
canvas = tkinter.Canvas(window, width=800, height=500)
canvas.place(x=0, y=110)

# Create turtles playground for 4 turtles
screen = turtle.TurtleScreen(canvas)
screen.bgcolor('light green')
screen.bgpic('./icons/bgr.gif')
screen.update()

# Write dog names
description = turtle.RawTurtle(screen)
description.hideturtle()

# #################
# Create dog 1 name 'shibu'
shibu = turtle.RawTurtle(screen)

# Change turtle to customised icon
shibuIcon = Image.open("./icons/dog1.png")
register_PIL("shibuIcon", shibuIcon)
shibu.shape("shibuIcon")

# Move to the ready place
description.penup()
description.goto(-50, 170)
description.write('Shibu\n', font='Arial 25')

# #################
# Create dog 2 name 'kiki'
kiki = turtle.RawTurtle(screen)

# Change turtle to customised icon
kikiIcon = Image.open("./icons/dog2.png")
register_PIL("kikiIcon", kikiIcon)
kiki.shape("kikiIcon")

# Move to the ready place
description.penup()
description.goto(-50, 55)
description.write('Kiki\n', font='Arial 25')

# #################
# Create dog 3 name 'Milu'
milu = turtle.RawTurtle(screen)

# Change turtle to customised icon
miluIcon = Image.open("./icons/dog3.png")
register_PIL("miluIcon", miluIcon)
milu.shape("miluIcon")

# Move to the ready place
description.penup()
description.goto(-50, -60)
description.write('Milu\n', font='Arial 25')

# #################
# Create dog 4 name 'Kari'
kari = turtle.RawTurtle(screen)

# Change turtle to customised icon
kariIcon = Image.open("./icons/dog4.png")
register_PIL("kariIcon", kariIcon)
kari.shape("kariIcon")

# Move to the ready place
description.penup()
description.goto(-50, -175)
description.write('Kari\n', font='Arial 25')

# Enable button state
submitName['state'] = tkinter.NORMAL

# Begin the mainloop for tkinter window
window.mainloop()
