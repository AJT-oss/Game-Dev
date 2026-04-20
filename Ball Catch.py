import pgzrun
import random

WIDTH = 400
HEIGHT = 600

ball= Actor("ball.png")
ball.pos= 200,15

basket= Actor("basket.png")
basket.pos=200,550

score=0
lives=3

def draw() :
    screen.blit("bg.png",(0,0))
    ball.draw()
    basket.draw()
    screen.draw.text(f"Score:{score}",(25,15))
    screen.draw.text(f"Lives:{lives}",(250,15))

fallingspeed = 7


def update():
    global score,c
    global lives
    if keyboard.left:
        basket.x-=5
    if keyboard.right:
        basket.x+=5
    
    ball.y+=fallingspeed
    if ball.y>HEIGHT:
        lives-=1
        resetball()


    

    if basket.colliderect(ball):
        score+=1
        resetball()

    if lives<1:
        screen.draw.text("Game Over",(300,200))


def resetball():
    ball.pos= (random.randint(30,WIDTH-30),0)
    



pgzrun.go()

