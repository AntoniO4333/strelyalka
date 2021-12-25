import pygame

pygame.init()
screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])

def lose():
    menu = False
    running = True
    loser = True
    game = False
    screenX = 900
    screenY = 600
    screen = pygame.display.set_mode([screenX, screenY])
    screen.fill([0, 0, 0])
    font = pygame.font.Font(None, 100)
    text_shots1 = font.render('Вы проиграли', 1, [255, 0, 0])
    screen.blit(text_shots1, [200, 200])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            loser = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = True
                loser = False
    pygame.display.flip()
    return running, menu, loser, game


def win():
    menu = False
    running = True
    winner = True
    game = False
    space = pygame.image.load('zemlya1.3.jpg')
    screenX = 900
    screenY = 600
    screen = pygame.display.set_mode([screenX, screenY])
    screen.blit(space, (0, 0))
    font = pygame.font.Font(None, 100)
    text_shots1 = font.render('Вы выиграли!', 1, [0, 255, 0])
    screen.blit(text_shots1, [200, 200])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            winner = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = True
                winner = False
    pygame.display.flip()
    return running, menu, winner, game