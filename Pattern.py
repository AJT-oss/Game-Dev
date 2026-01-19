import pgzrun
import random


WIDTH = 300
HEIGHT = 300

def draw():
    w=WIDTH
    h=HEIGHT-200
    for i in range (15):
        Rectangle=Rect((0,0),(w,h))
        Rectangle.center=150,150
        r= random.randint(0,255)
        g= 255
        b=0
        screen.draw.rect(Rectangle,(r,g,b))
        w-=10
        h+=10
        b+=0
        g-=255
pgzrun.go()