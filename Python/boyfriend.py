import pygame

def boyfriend(window):
    if pygame.key.get_pressed()[pygame.K_a]:
        img_position = 2
    elif pygame.key.get_pressed()[pygame.K_s]:
        img_position = 3
    elif pygame.key.get_pressed()[pygame.K_w]:
        img_position = 4
    elif pygame.key.get_pressed()[pygame.K_d]:
        img_position = 1
    else:
         img_position = 0
    images = "Image/boyfriend.gif", "Image/Boyfriend_right.png", "Image/boyfriend_left.png", "Image/boyfriend_down.png", "Image/boyfriend_up.png"
    boyfriend = pygame.image.load(images[img_position])
    boyfriend = pygame.transform.scale(boyfriend, (250, 242))
    window.blit(boyfriend, (730, 300))
