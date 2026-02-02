import pgzrun
import random

WIDTH=600
HEIGHT=500
tom=Actor("tom.png")
tom.pos=(200,150)
jerry=Actor("jerry.png")
jerry.pos=(350,350)

score=0
c=False
def draw():
    screen.fill("Grey")
    tom.draw()
    jerry.draw()
    screen.draw.text("Tag, Your It!",(250,100))
    screen.draw.text(f"score:{score}",(100,50))

def update():
    global score,c
    if keyboard.left:
        tom.x-=5
    if keyboard.right:
        tom.x+=5
    if keyboard.up:
        tom.y+=5
    if keyboard.down:
        tom.y-=5

    if jerry.colliderect(tom):
        if not c:
            score+=1
            c=True
            jerry.pos=(random.randint(50,550),random.randint(50,550))
    else:
        c=False


pgzrun.go()