import pgzrun
from random import randint

WIDTH =1250
HEIGHT = 600
Score = 0
Game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(Score), color = "black", topleft = (10, 10))

    if Game_over:
        screen.fill ("pink")
        screen.draw.text ("Final Score: " + str(Score), topleft = (10, 10), fontsize = 60)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global Game_over
    Game_over = True

def update():
    global Score


    if keyboard.left:
        fox.x = fox.x - 4
        if keyboard.space:
            fox.x = fox.x - 20
    elif keyboard.right:
        fox.x = fox.x + 4
        if keyboard.space:
            fox.x = fox.x + 20
    elif keyboard.up:
        fox.y = fox.y - 4
        if keyboard.space:
            fox.y = fox.y - 20
    elif keyboard.down:
        fox.y = fox.y + 4
        if keyboard.space:
            fox.y = fox.y + 20
    
    coin_collected = fox.colliderect (coin)

    if coin_collected:
        Score = Score + 10
        place_coin()

clock.schedule(time_up, 60.0)
place_coin()

pgzrun.go()