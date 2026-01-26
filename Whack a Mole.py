import pgzrun
import random

WIDTH=600
HEIGHT=500

mole=Actor("mole.png")
mole.pos=300,250

score=0
def draw():
    screen.fill("Light Green")
    mole.draw()
    screen.draw.text("Whack a Mole",(250,100))
    screen.draw.text(f"score:{score}",(100,50))

def on_mouse_down(pos):
    global score
    if mole.collidepoint(pos):
        mole.x=random.randint(50,550)
        mole.y=random.randint(50,550)
        score +=2
    else:
        score -=1


def update():
    draw

pgzrun.go() 

