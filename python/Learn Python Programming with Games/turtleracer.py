import turtle
import time
from time import sleep

# define screen size

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_AREA_START_X = - ((SCREEN_WIDTH // 2) - 50)
GAME_AREA_START_Y = - ((SCREEN_HEIGHT // 2) - 50)

BORDER_WIDTH = SCREEN_WIDTH -100
BORDER_HEIGHT = SCREEN_HEIGHT -100
BORDER_HEIGHT_HALF = BORDER_HEIGHT// 2


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor('gray')
    screen.tracer(2) # delay drawing by two frames
    screen.update() # update the screen


def draw_game_area():
    area_turtle = turtle.Turtle()
    area_turtle.setundobuffer(None) # no undo buffer to speed up the drawing
    area_turtle.hideturtle() # hide the turtle
    area_turtle.speed(0) # 0 is the fastest speed
    area_turtle.color('black', 'green') # pencolor and fillcolor
    area_turtle.penup() # don't draw while moving into position
    area_turtle.setpos(GAME_AREA_START_X, GAME_AREA_START_Y) # left bottom corner
    area_turtle.pendown() # now start drawing
    area_turtle.pensize(4) # set the pen size to 4

    area_turtle.begin_fill()
    for _border in range(2):
        area_turtle.fd(BORDER_WIDTH)
        area_turtle.lt(90)
        area_turtle.fd(BORDER_HEIGHT)
        area_turtle.lt(90)
    area_turtle.end_fill()


def create_game_screen(): # creates the game screen
    setup_screen()
    draw_game_area()

def draw_running_track(draw_turtle):
    draw_turtle.setheading(90)

    draw_turtle.circle(-50, 90)
    draw_turtle.fd(BORDER_WIDTH - 120)

    draw_turtle.circle(50, 180)
    draw_turtle.fd(BORDER_WIDTH - 140)

    draw_turtle.circle(-50, 180)
    draw_turtle.fd(BORDER_WIDTH - 180)

    draw_turtle.circle(50, 180)
    draw_turtle.fd(BORDER_WIDTH - 230)

    draw_turtle.circle(-50, 180)
    draw_turtle.fd(BORDER_WIDTH - 290)

    draw_turtle.circle(50, 90)

def create_running_track():
    track_turtle = turtle.Turtle()
    track_turtle.hideturtle()
    track_turtle.setundobuffer(None)
    track_turtle.speed(0)
    track_turtle.color('yellow', 'brown')

    track_turtle.penup()

    start_pos = GAME_AREA_START_X + 10 # start ten pixels into the x game area
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.pendown()
    track_turtle.pensize(3)

    draw_running_track(track_turtle) # now draw the runninng track
    track_turtle.penup()

def write_labels():
    start_pen = turtle.Turtle() # crate a new turtle to write with
    start_pen.speed(0)
    start_pen.color('white')
    start_pen.penup()
    start_pen.setpos(GAME_AREA_START_X - 25, GAME_AREA_START_Y - 25)
    start_string = 'START'
    start_pen.write(start_string, align= 'left', font=('Arial', 14, 'bold'))
    start_pen.hideturtle()

    finish_pen = turtle.Turtle() # create a new turtle to write with
    finish_pen.speed(0)
    finish_pen.color('red')
    finish_pen.penup()
    finish_pen.setpos((BORDER_WIDTH // 2) - 140, BORDER_HEIGHT // 2)
    finish_string = 'FINISH'
    finish_pen.write(finish_string, align= 'left', font=('Arial', 14, 'bold'))
    finish_pen.hideturtle()

def create_track_with_labels():
    create_running_track()
    write_labels()

def run_track():
    # use the code that draws the track to run the track
    runner = turtle.Turtle()
    runner.penup()
    runner.color('turquoise', 'blue') # pencolor, fillcolor
    runner.pensize(5)
    runner.shape('turtle')

    # position runner at the start of the track
    start_pos = GAME_AREA_START_X + 10
    runner.setpos(start_pos, GAME_AREA_START_Y)
    runner.pendown()

    # run the track
    sleep(1)
    draw_running_track(runner, slowtime=1)

def create_track ():
    track_turtle = turtle.Turtle()
    track_turtle.setundobuffer (None)
    track_turtle.hideturtle()
    track_turtle.speed(0)
    track_turtle.color('black', 'brown')
    
    track_turtle.penup()
    track_turtle.begin_fill()
    start_pos = 20
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.pendown()
    track_turtle.setpos(start_pos, BORDER_HEIGHT_HALF)
    track_turtle.setpos(-start_pos, BORDER_HEIGHT_HALF)
    track_turtle.setpos(-start_pos, GAME_AREA_START_Y)
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.end_fill()


def create_racer_turtle():
    running_turtle = turtle.Turtle()
    running_turtle.shape('turtle')
    running_turtle.setundobuffer(None)
    running_turtle.penup()
    running_turtle.speed(0)
    running_turtle.color('blue', 'turquoise') # turtle outline is blue and fill is turquoise

    running_turtle.setpos(0, GAME_AREA_START_Y)
    running_turtle.setheading(90)
    running_turtle.showturtle()

    for run in range(BORDER_HEIGHT):
        running_turtle.setpos(0, GAME_AREA_START_Y + run)
        print(run)
        if run % 12:
            running_turtle.setpos(0 + 1, GAME_AREA_START_Y + run) # wiggle the turtle runner
        time.sleep( 0.01 )    

if __name__ == '__main__': # ?
    create_game_screen() # calls the function
    create_track_with_labels() # creates the running track with labels
    run_track()
    turtle.done() # keeps the game window up