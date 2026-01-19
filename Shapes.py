import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("lightblue")
    screen.draw.text("MANDEM",(250,250))
    screen.draw.filled_circle((50,100), 100,color="Red")
    screen.draw.rect(Rect((200,300),(200,100)),"blue")



pgzrun.go()