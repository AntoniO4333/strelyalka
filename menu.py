import pygame, help

pygame.init()
from pygame.color import THECOLORS


def menushka():
    game = False
    menu = True
    running = True
    helpa = False
    screenX = 900
    screenY = 600
    space = pygame.image.load('zemlya1.3.jpg')
    screen = pygame.display.set_mode([screenX, screenY])
    screen.blit(space, (0, 0))
    font = pygame.font.Font(None, 100)
    text_shots1 = font.render('Start', 1, THECOLORS['green'])
    screen.blit(text_shots1, [340, 120])
    text_shots2 = font.render('Help', 1, THECOLORS['black'])
    screen.blit(text_shots2, [340, 220])
    text_shots3 = font.render('Exit', 1, THECOLORS['red'])
    screen.blit(text_shots3, [340, 320])
    text_shots1 = font.render('Космическая стрелялка', 1, THECOLORS['black'])
    screen.blit(text_shots1, [50, 0])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (x >= 300) and (x <= 550):
                if (y >= 100) and (y <= 200):
                    game = True
                    menu = False
                if (y >= 200) and (y <= 300):
                    menu = False
                    helpa = True
                if (y >= 300) and (y <= 400):
                    menu = False
                    running = False
    return game, menu, running, helpa
