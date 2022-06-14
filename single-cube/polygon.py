import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((800, 600))

window.fill((255, 255, 255))


clock = pygame.time.Clock()
while True:

    string = "%s, %s" % (str(pygame.mouse.get_pos()[0]), str(pygame.mouse.get_pos()[1]))

    pygame.display.set_caption(string)

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    pygame.draw.polygon(window, (255, 0, 0), [[524, 336], [524, 393], [467, 210], [467, 153]])
    pygame.draw.polygon(window, (0, 0, 255), [[276, 207], [333, 390], [524, 336], [467, 153]])

    pygame.display.update()

