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
gameover=False

def draw() :
    screen.blit("bg.png",(0,0))
    ball.draw()
    basket.draw()
    screen.draw.text(f"Score:{score}",(25,15))
    screen.draw.text(f"Lives:{lives}",(250,15))
    if gameover:
        screen.draw.text("GAMEOVER",(150,300),fontsize=50,color="Red")

fallingspeed = 7


def update():
    global score,c, gameover
    global lives
    if keyboard.left:
        basket.x-=5
    if keyboard.right:
        basket.x+=5
    
    if gameover:
        return

    ball.y+=fallingspeed
    if ball.y>HEIGHT:
        lives-=1
        resetball()
    if lives<=0:
        gameover=True


    

    if basket.colliderect(ball):
        score+=1
        resetball()        

    
        


def resetball():
    ball.pos= (random.randint(30,WIDTH-30),0)
    



pgzrun.go()

