import threading
import pygame
from girlfriend2 import girlfriend

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((1000, 900))
    t = threading.Thread(target=girlfriend(window))
    t.setDaemon(True)
    t.start()
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.time.delay(100)
quit()
