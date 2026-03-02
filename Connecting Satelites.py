import pgzrun
import random

WIDTH=700
HEIGHT=400

no_of_sats=10
sats=[]

for i in range(no_of_sats):
    satelite=Actor("satelite.png")
    satelite.x=random.randint(50,650)
    satelite.y=random.randint(50,350)
    sats.append(satelite)

def draw():
    screen.blit("star",(0,0))
    number=1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+15),color="red")
        number+=1


pgzrun.go()