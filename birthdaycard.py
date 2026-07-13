import pygame
import time
pygame.init()

WIDTH=600
HEIGHT=600


displaysurface=pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Birthday Greeting")

img=pygame.image.load("image")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    font=pygame.font.SysFont("Arial",60)
    text=font.render("Happy Birthday",True,"Black")
    displaysurface.fill((255,255,255))
    displaysurface.blit("card1.jpg"(0,0))
    displaysurface.blit("Wishing you a Happy B-DAY",(175,300))
    pygame.display.update()
    time.sleep(2)

    img=pygame.image.load("image1")
    image1=pygame.transform.scale(img,(WIDTH,HEIGHT))
    font=pygame.font.SysFont("Arial",60)
    text=font.render("Happy Birthday",True,"Black")
    displaysurface.fill((255,255,255))
    displaysurface.blit("card2.jpg"(0,0))
    displaysurface.blit("Hope you remain a bright and kind person along the years",(175,300))
    pygame.display.update()
    time.sleep(2)

    img=pygame.image.load("image2")
    image2=pygame.transform.scale(img,(WIDTH,HEIGHT))
    displaysurface.fill((255,255,255))
    displaysurface.blit("card3.png"(0,0))
    pygame.display.update()
    time.sleep(2)