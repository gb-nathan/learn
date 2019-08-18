import turtle

our_turtle = turtle.Turtle() # creating the turtle object

our_turtle.color('turquoise') # set color to blue

our_turtle.hideturtle() # hide the turtle or pen

print(our_turtle.shape()) # makes the turtle look like a turtle

for _draw in range(40):

    our_turtle.forward(50) # makes the turtle move forward 50 pixels
    our_turtle.left(85) #makes the turtle turn left 90 degrees

turtle.done() # calls mainloop
