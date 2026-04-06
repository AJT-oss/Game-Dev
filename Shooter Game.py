import pgzrun

WIDTH = 400
HEIGHT = 600

rocket = Actor("rocket.png")
rocket.pos=(WIDTH//2, HEIGHT-100)

enemies=[]

bullets=[]

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].y = rocket.y
        bullets[-1].x = rocket.x

for x in range(8):
    for y in range(4):
        enemies.append(Actor("mini.png"))
        enemies[-1].x=100+40*x
        enemies[-1].y=0+20*y

direction = 1
score = 0

def drawscore():
    screen.draw.text(f"Score:{score}",(50,50))

def update():
    global direction,score
    if keyboard.left:
        rocket.x -=5
    elif keyboard.right:
        rocket.x +=5
    for bullet in bullets:
        bullet.y -= 7.5
    moveDown=False
    if len(enemies)>0 and enemies[-1].x>WIDTH-20 or enemies[0].x<20:
        moveDown=True
        direction=direction*-1
    for enemy in enemies:
        enemy.x +=2*direction
        if moveDown==True:
            enemy.y +=30

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score+=20
                bullets.remove(bullet)
                enemies.remove(enemy)


def draw():
    screen.fill("Dark Blue")
    rocket.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    drawscore()

pgzrun.go()

