import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "The Bumblebee and the Flower"

score = 0
game_over = False

bee = Actor("bumblebee")
bee.pos = (100, 100)
flower = Actor("flower")
flower.pos = (200, 200)

def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(f"Score: {score}", color = "black", topleft = (10, 10))
    
    if game_over:
        screen.clear()
        screen.fill("black")
        screen.draw.text(f"TIME UP \n FINAL SCORE: {score}", color = "red", fontsize = 40, midtop = (WIDTH / 2, HEIGHT / 2))

def time_up():
    global game_over
    game_over = True

def place_flower():
    flower.x = randint(70, WIDTH - 70)
    flower.y = randint(70, HEIGHT - 70)

def update():
    global score
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.up:
        bee.y -= 2
    if keyboard.down:
        bee.y += 2

    if bee.colliderect(flower):
        score += 10 
        place_flower()

clock.schedule(time_up, 30.0)

pgzrun.go()