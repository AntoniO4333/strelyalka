import pygame, random, time
from menu import *
from help import *
from myhelp import *
pygame.init()
screenX = 900
screenY = 600
korablX = 450
korablY = 530
screen = pygame.display.set_mode([screenX, screenY])
screen.fill([0, 0, 0])
x = []
y = []
razmer_nlo_right = 70
razmer_nlo_left = 0
rocketX = []
rocketY = []
d = []
n = 7
lvl_number = 1
zapolnenie_nlo = True
speed = 5
rockets_count = 0
hit_count = 0
dlina = 'До земли остался 1 млн км'
nlo = pygame.image.load("nlo.xcf")
korabl = pygame.image.load("korabl.xcf")
rocket = pygame.image.load("rocket.png")
space = pygame.image.load("space1.jpg")


nlo.set_colorkey((255, 255, 255))
korabl.set_colorkey((255, 255, 255))
rocket.set_colorkey((255, 255, 255))

running = True
menu = True
game = False
helpa = False
loser = False
winner = False
pobeda = False


def move_korabl(korablX):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and korablX > -10:
        korablX -= speed
    elif keys[pygame.K_RIGHT] and korablX < 840:
        korablX += speed
    return korablX


def rocket_update():
    global rockets_count
    for i in range(rockets_count):
        if rocketY[i] > -32:
            rocketY[i] -= 6
            screen.blit(rocket, (rocketX[i], rocketY[i]))
        else:
            rockets_count -= 1
            rocketY.pop(i)
            rocketX.pop(i)
            return


def hit_check():
    global hit_count
    global n
    global rockets_count
    for i in range(rockets_count):
        for j in range(n):
            if (x[j] - razmer_nlo_left <= rocketX[i]) and (rocketX[i] <= x[j] + razmer_nlo_right):
                if (y[j] <= rocketY[i]) and (rocketY[i] <= y[j] + razmer_nlo_right):
                    n -= 1
                    x.pop(j)
                    y.pop(j)
                    d.pop(j)
                    rockets_count -= 1
                    rocketY.pop(i)
                    rocketX.pop(i)
                    hit_count += 1
                    return


def zapolnenie_nlo_lvl1(x, y, d, zapolnenie_nlo):
    if zapolnenie_nlo == True:
        dy = 0
        for i in range(n):
            x += [random.randint(0, 830)]
            y += [dy]
            d += [random.randint(1, 10)]
            dy += 70
            zapolnenie_nlo = False
    return zapolnenie_nlo


def move_nlo_lvl1():
    for i in range(n):  # nlo
        x[i] += d[i]
        if (x[i] + d[i] + 70 >= screenX) or (x[i] < 0):  # Условия отражения
            d[i] = -d[i]


def zapolnenie_nlo_lvl2(x, y, d, zapolnenie_nlo, nlo, space):
    if zapolnenie_nlo == True:
        for i in range(n):
            nlo = pygame.image.load("nlo_lvl2.png")
            space = pygame.image.load("space2.1.jpg")
            x += [random.randint(0, 860)]
            y += [random.randint(0, 260)]
            d += [random.randint(1, 3)]
            zapolnenie_nlo = False
    return zapolnenie_nlo, nlo, space


def move_nlo_lvl2():
    for i in range(n):  # nlo
        y[i] += d[i]
        if y[i] >= screenY + 40:
            y[i] = -40
        if d[i] <= 0:
            d[i] = -d[i]


def crash_check():
    loser = False
    game = True
    for i in range(n):
        if (korablY <= y[i]) and (y[i] <= korablY + 64):
            if (korablX - 40 <= x[i]) and (x[i] <= korablX + 40):
                loser = True
                game = False
    return loser, game


def obnovlenie_i_otrisovka():
    screen.blit(space, (0, 0))
    for i in range(n):
        screen.blit(nlo, (x[i], y[i]))
    screen.blit(korabl, (korablX, korablY))
    font = pygame.font.Font(None, 60)
    text = str(hit_count)
    aboba = font.render('Нло сбито' + ' ' + str(text), 1, THECOLORS['white'])
    screen.blit(aboba, [600, 540])
    rocket_update()
    pygame.time.delay(10)
    pygame.display.flip()


while running:
    korablX = 450
    korablY = 530
    x = []
    y = []
    razmer_nlo_right = 70
    razmer_nlo_left = 0
    rocketX = []
    rocketY = []
    d = []
    n = 7
    hit_count = 0
    lvl_number = 1
    pobeda = False
    zapolnenie_nlo = True
    nlo = pygame.image.load("nlo.xcf")
    rocket = pygame.image.load("rocket.png")
    space = pygame.image.load("space1.jpg")
    nlo.set_colorkey((255, 255, 255))
    korabl.set_colorkey((255, 255, 255))
    rocket.set_colorkey((255, 255, 255))
    while menu:
        game, menu, running, helpa = menushka()
    while helpa:
        running, helpa, menu = help1()
    while loser:
        running, menu, loser, game = lose()
    while winner:
        running, menu, winner, game = win()
    while game:
        if lvl_number == 1:
            zapolnenie_nlo = zapolnenie_nlo_lvl1(x, y, d, zapolnenie_nlo)
            move_nlo_lvl1()
        if lvl_number == 2:
            zapolnenie_nlo, nlo, space = zapolnenie_nlo_lvl2(x, y, d, zapolnenie_nlo, nlo, space)
            move_nlo_lvl2()
            loser, game = crash_check()
        hit_check()
        korablX = move_korabl(korablX)
        obnovlenie_i_otrisovka()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if rockets_count < 5:
                        rocketX.append(korablX + 19)
                        rocketY.append(korablY + 10)
                        rockets_count += 1
                if event.key == pygame.K_ESCAPE:
                    menu = True
                    game = False

        if n == 0:
            if n == 0:
                speed_k = 5
                korablY -= speed_k
            if korablY <= -70:
                korablY = 900
            if (korablY <= 535) and (korablY > 530):
                speed_k = 0
                korablY = 530
                lvl_number += 1
                if lvl_number == 2:
                    n = 10
                    razmer_nlo_right = 40
                    razmer_nlo_left = 40
                    zapolnenie_nlo = True
                    rockets_count = 0
                    rocketX = []
                    rocketY = []
                    dlina = 'До земли осталось 500 тыс км'
                if lvl_number == 3:
                    dlina = 'До земли осталось 5 тыс км'
                    pobeda = True
                    space = pygame.image.load('zemlya1.3.jpg')
                print(lvl_number)
            if (korablY <= -65) and pobeda:
                game = False
                winner = True
pygame.quit()
