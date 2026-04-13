import pgzrun
import random

WIDTH = 400
HEIGHT = 600

ball= Actor("ball.png")
ball.pos= 200,15

basket= Actor("basket.png")
basket.pos=200,550

score=0

def draw() :
    screen.blit("bg.png",(0,0))
    ball.draw()
    basket.draw()
    screen.draw.text(f"Score:{score}",(25,15))


def update():
    global score,c
    if keyboard.left:
        basket.x-=5
    if keyboard.right:
        basket.x+=5
        



pgzrun.go()

