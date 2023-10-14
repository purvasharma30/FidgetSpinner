# Import the turtle graphics library to create graphical animations.
from turtle import *

# Initialize a dictionary to store the state of the spinner, with an initial 'turn' value of 0.
state = {'turn': 0}

# Define a function to draw and animate the spinner.
def spinner():
    clear()  # Clear the screen to prepare for the next frame.
    angle = state['turn'] / 10  # Calculate the angle of rotation based on the 'turn' value.
    right(angle)  # Rotate the turtle by the calculated angle.
    forward(100)  # Move the turtle forward by a fixed distance.
    dot(120, 'red')  # Draw a red dot at the current position.
    back(100)  # Move the turtle back to the starting position.
    right(120)  # Rotate the turtle to the right by 120 degrees.
    forward(100)  # Move forward again.
    dot(120, 'green')  # Draw a green dot.
    back(100)  # Move back to the starting position.
    right(120)  # Rotate the turtle to the right by 120 degrees.
    forward(100)  # Move forward one more time.
    dot(120, 'blue')  # Draw a blue dot.
    back(100)  # Move back to the starting position.
    right(120)  # Rotate the turtle to the right by 120 degrees.
    update()  # Update the screen to display the changes.

# Define a function to animate the spinner.
def animate():
    if state['turn'] > 0:
        state['turn'] -= 1  # Decrease the 'turn' value to slow down the animation.

    spinner()  # Call the spinner function to draw a frame.
    ontimer(animate, 20)  # Schedule the next frame to be drawn after 20 milliseconds.

# Define a function to increase the 'turn' value, which accelerates the spinner.
def flick():
    state['turn'] += 10  # Increase the 'turn' value by 10.

# Set up the turtle graphics window.
setup(420, 420, 370, 0)
hideturtle()  # Hide the turtle cursor.
tracer(False)  # Turn off automatic screen updates for smoother animation.
width(20)  # Set the drawing pen's width.

# Listen for the 'space' key to trigger the 'flick' function when pressed.
onkey(flick, 'space')
listen()  # Start listening for keyboard events.

# Start the animation loop by calling the 'animate' function and enter the main event loop.
animate()

# The 'done' function keeps the window open until the user closes it.
done()
