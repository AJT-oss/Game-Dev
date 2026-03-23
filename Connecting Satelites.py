import pgzrun
import random

WIDTH=700
HEIGHT=400

no_of_sats=10
sats=[]
lines=[]
next=0

for i in range(no_of_sats):
    satelite=Actor("satelite.png")
    satelite.x=random.randint(50,650)
    satelite.y=random.randint(50,350)
    sats.append(satelite)

def draw():
    screen.blit("star",(0,0))
    screen.draw.text("Connecting Satelites",(350,50))
    number=1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+15),color="red")
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    
def on_mouse_down(pos):
    global next,lines,sats
    if sats[next].collidepoint(pos):
        if next:
            lines.append((sats[next-1].pos,sats[next].pos))
        next+=1
    else:
        lines=[]
        next=0

pgzrun.go()
