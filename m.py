import pgzrun
import random

HEIGHT = 600
WIDTH = 400

pacman=Actor("pacman.png")
pacman.pos=200,300

ghost=Actor("ghost.png")
ghost.pos=200,350

score= 0
c=False
time=20
gameover= False

def timer():
    global time,gameover
    if time>0:
        time-=1
    else:
        gameover=True
        screen.draw.text("GAME OVER",(200,300),color="white")

clock.schedule_interval(timer,1.0)

def draw():
    screen.fill("Black") 
    screen.draw.text("PACMAN",(200,50))
    ghost.draw()
    pacman.draw()
    screen.draw.text(f"score:{score}",(100,50))
    screen.draw.text(f"timer:{time}",(300,50))



def update():
    global score,c
    if keyboard.left:
        pacman.x-=5
    if keyboard.right:
        pacman.x+=5
    if keyboard.up:
        pacman.y-=5
    if keyboard.down:
        pacman.y+=5

    if ghost.colliderect(pacman):
        if not c:
            score+=1
            c=True
            ghost.pos=(random.randint(15,400),random.randint(15,400))
    else:
        c=False

pgzrun.go()