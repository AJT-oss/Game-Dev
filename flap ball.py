import pgzrun
import random

TITLE="Flap Ball"
WIDTH=800
HEIGHT=600

R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)

CLR=R,G,B

GRAVITY=2000.0

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
        self.color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.color)

balls=[Ball(100,100),Ball(600,200),Ball(300,100),Ball(450,100),Ball(150,400),Ball(200,400),Ball(600,400),Ball(400,300),Ball(400,500)]

def draw():
    screen.fill("white")
    for ball in balls:
        ball.draw()

def update(dt):
    for ball in balls:
        uy=ball.vy
        ball.vy +=GRAVITY*dt
        ball.y +=(uy+ball.vy)*0.5*dt

        if ball.y>HEIGHT-ball.radius:
            ball.y=HEIGHT-ball.radius
            ball.vy=-ball.vy*0.9
        ball.x +=ball.vx*dt

        if ball.x>WIDTH-ball.radius or ball.x<ball.radius:
            ball.vx=-ball.vx

def on_key_down(key):
    if key==keys.SPACE:
        for ball in balls:
            ball.vy=random.randint(-500,-400)

    
pgzrun.go()
