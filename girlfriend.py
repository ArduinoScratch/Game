import pygame

def girlfriend(window):
    images = "Image/Girlfriend/girlfriend1.png", "Image/Girlfriend/girlfriend2.png", "Image/Girlfriend/girlfriend3.png", "Image/Girlfriend/girlfriend4.png", "Image/Girlfriend/girlfriend5.png", "Image/Girlfriend/girlfriend6.png", "Image/Girlfriend/girlfriend7.png", "Image/Girlfriend/girlfriend8.png", "Image/Girlfriend/girlfriend9.png", "Image/Girlfriend/girlfriend10.png", "Image/Girlfriend/girlfriend11.png", "Image/Girlfriend/girlfriend12.png", "Image/Girlfriend/girlfriend13.png", "Image/Girlfriend/girlfriend14.png", "Image/Girlfriend/girlfriend15.png", "Image/Girlfriend/girlfriend16.png", "Image/Girlfriend/girlfriend17.png", "Image/Girlfriend/girlfriend18.png", "Image/Girlfriend/girlfriend19.png", "Image/Girlfriend/girlfriend20.png", "Image/Girlfriend/girlfriend21.png", "Image/Girlfriend/girlfriend22.png", "Image/Girlfriend/girlfriend23.png", "Image/Girlfriend/girlfriend24.png", "Image/Girlfriend/girlfriend25.png"
    img_position = 0
    while (True):
        img_position += 1
        pygame.time.delay(10)
        if img_position > 24:
            img_position = 0
        girlfriend = pygame.image.load(images[img_position])
        girlfriend = pygame.transform.scale(girlfriend, (330, 289))
        window.blit(girlfriend, (450, 200))
