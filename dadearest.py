import pygame

def dadearest(window, mudar_foto_opponente_up, mudar_foto_opponente_right, mudar_foto_opponente_down):
    if mudar_foto_opponente_up == True:
        img_position = 1
    elif mudar_foto_opponente_right == True:
        img_position = 2
    elif mudar_foto_opponente_down == True:
        img_position = 3
    else:
        img_position = 0
    images = "Image/dad_battle.gif", "Image/Dadearest_up.png", "Image/Dadearest_right.webp", "Image/Dadearest_down.webp"
    dadearest = pygame.image.load(images[img_position])
    dadearest = pygame.transform.scale(dadearest, (200, 350))
    window.blit(dadearest, (310, 200))