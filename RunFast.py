import pgzrun
import random

WIDTH=600
HEIGHT=500

po=Actor("po.png")
po.pos=(250,250)
dum=Actor("dum.png")
dum.pos=(350,400)

score=0
c=False
def draw():
    screen.fill("Grey")
    po.draw()
    dum.draw()
    screen.draw.text("Run Fast!",(250,100))
    screen.draw.text(f"score:{score}",(100,50))

def update():
    global score,c
    if keyboard.left:
        po.x-=5
    if keyboard.right:
        po.x+=5
    if keyboard.up:
        po.y-=5
    if keyboard.down:
        po.y+=5

if dum.colliderect(po):
    if not c:
        score+=1
        c=True
        dum.pos=(random.randint(50,550),random.randint(50,550))
    else:
        c=False

 
    
pgzrun.go()


