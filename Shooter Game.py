import pgzrun

WIDTH = 400
HEIGHT = 600

rocket = Actor("rocket.png")
rocket.pos=(WIDTH//2, HEIGHT-100)

enemies=[]

for x in range(8):
    for y in range(4):
        enemies.append(Actor("mini.png"))
        enemies[-1].x=100+40*x
        enemies[-1].y=0+20*y

def update():
    pass

def draw():
    screen.fill("Dark Blue")
    rocket.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
