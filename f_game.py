import pygame, random
from strelyalka import *
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
nlo = pygame.image.load("nlo.xcf")
korabl = pygame.image.load("korabl.xcf")
rocket = pygame.image.load("rocket.png")
space = pygame.image.load("space1.jpg")
nlo_bullet = pygame.image.load("bullet_lvl2.png")

nlo.set_colorkey((255, 255, 255))
korabl.set_colorkey((255, 255, 255))
rocket.set_colorkey((255, 255, 255))

running = True
menu = True
game = False
helpa = False
loser = False


def game1():
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
                lvl_number = 1
                zapolnenie_nlo = True
                nlo = pygame.image.load("nlo.xcf")
                rocket = pygame.image.load("rocket.png")
                space = pygame.image.load("space1.jpg")
                nlo.set_colorkey((255, 255, 255))
                korabl.set_colorkey((255, 255, 255))
                rocket.set_colorkey((255, 255, 255))

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