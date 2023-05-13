import pygame

def bolinha(window):
    x=80
    y=80
    xd=1
    yd=1
    while True:
        window.fill((0,0,255))
        pygame.draw.circle(window,(255,0,0,255),(x,y),80)
        pygame.display.flip()
        x=x+xd
        y=y+yd
        if x==(1000-80) or x==80:
            xd=-xd
        if y==(900-80) or y==80:
            yd=-yd
        pygame.time.delay(10)