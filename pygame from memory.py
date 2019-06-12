import pygame
pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)

carryOn = True

size = 500,700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello World")

while carryOn == True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            carryOn = False

    pygame.draw.lines(screen, BLACK, True, [(300,200),(400,238),(590,234)],4)

    pygame.display.flip()

pygame.QUIT()
