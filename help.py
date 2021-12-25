import pygame

pygame.init()
screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])
from pygame.color import THECOLORS


def help1():
    running, helpa, menu = True, True, False
    screen.fill([0, 0, 0])
    h = open('help1.txt', 'r')
    lines = h.readlines()
    dlina = len(lines)
    h.close()
    y = 100
    x = 20
    font = pygame.font.Font(None, 100)
    text_shots1 = font.render('Помощь', 1, THECOLORS['white'])
    screen.blit(text_shots1, [240, 20])
    for i in range(dlina):
        lin = lines[i]
        stroka = lin[0:len(lin) - 1]
        font = pygame.font.Font(None, 60)  # задаем шрифт
        tt = font.render(stroka, True, [255, 255, 255])
        screen.blit(tt, [x, y])
        y = y + 50
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            helpa = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = True
                helpa = False
    pygame.display.flip()
    return running, helpa, menu

