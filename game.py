import pygame
pygame.init()
window = pygame.display.set_mode([450,450])

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    window.fill((255,255,255))

    pygame.display.update()


pygame.quit()

