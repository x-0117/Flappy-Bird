# -*- coding: utf-8 -*-
import pygame
import random, time, threading, sys
from pygame.locals import *
gameover = 0
night = 0
pygame.init()
sky = (135,206,235)
brick = (245,197,44)
bird = (0, 255, 0)
DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
l1 = [[' ' for _ in range(30)] for __ in range(20)]
shit = 8
y_coordinate = 200
score = 0
for j in range(0, shit):
    l1[j][0] = 'H'
for j in range(shit + 5, 20):
    try:
        l1[j][0] = 'H'
    except:
        pass
flag = 1
for i in range(1, 30):
    if flag == 0:
        shit = max(1, shit + random.randint(-2, 2))
        if shit >= 15:
            shit -= 2
        for j in range(0, shit):
            l1[j][i] = 'H'
        for j in range(shit + 5, 20):
            try:
                l1[j][i] = 'H'
            except:
                pass
    flag = (flag + 1) % 3


pygame.display.set_caption('Flappy Bird')


def birdCoordinates():
    global y_coordinate
    global gameover
    while gameover == 0:
        y_coordinate += 2
        time.sleep(0.1)


def game():
    global flag, shit, gameover, score, l1
    while True:
        for i in l1:
            i.pop(0)
            i.append(' ')
        if flag == 0:
            shit = max(1, shit + random.randint(-2, 2))
            if shit >= 15:
                shit -= 2
            for j in range(0, shit):
                l1[j][-1] = 'H'
            for j in range(shit + 5, 20):
                try:
                    l1[j][-1] = 'H'
                except:
                    pass
        flag = (flag + 1) % 3
        score += 10
        time.sleep(1)
        

pygame.draw.rect(DISPLAYSURF, sky, pygame.Rect(0, 0, 600, 400),  0)
font = pygame.font.SysFont(None, 40)
pygame.draw.rect(DISPLAYSURF, (169,169,169), (50, 15, 30, 6))
centre = (50, 18)
pygame.draw.circle(DISPLAYSURF, (255, 255, 255), centre, 8, 0)
img1 = font.render('Press any key to start...', True, (255, 255, 255))
DISPLAYSURF.blit(img1, (160, 175))
font = pygame.font.SysFont(None, 20)
img1 = font.render('Night', True, (255, 255, 255))
DISPLAYSURF.blit(img1, (7, 10))
pygame.display.update()
while True:
    mx, my = pygame.mouse.get_pos()
    start = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = 1
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            start = 1
            break
        if event.type == MOUSEBUTTONDOWN and 40 < mx and mx < 90 and my < 20:
            night = (night + 1) % 2
            if night == 1:
                sky = (13, 17, 23)
                brick = (139,69,19)
                bird = (0,100,0)
                centre = (50, 18)
            else:
                sky = (135,206,235)
                brick = (245,197,44)
                bird = (0, 255, 0)
                centre = (80, 19)
            pygame.draw.rect(DISPLAYSURF, sky, pygame.Rect(0, 0, 600, 400),  0)
            font = pygame.font.SysFont(None, 40)
            pygame.draw.rect(DISPLAYSURF, (169,169,169), (50, 15, 30, 6))
            pygame.draw.circle(DISPLAYSURF, (255, 255, 255), centre, 8, 0)
            img1 = font.render('Press any key to start...', True, (255, 255, 255))
            DISPLAYSURF.blit(img1, (160, 175))
            font = pygame.font.SysFont(None, 20)
            img1 = font.render('Night', True, (255, 255, 255))
            DISPLAYSURF.blit(img1, (7, 10))
            pygame.display.update()
    if start == 1:
        break
t1 = threading.Thread(target=birdCoordinates)
t1.start()
t4 = threading.Thread(target=game)
t4.start()


while gameover == 0:
    pygame.display.update()
    pygame.draw.rect(DISPLAYSURF, sky, pygame.Rect(0, 0, 600, 400),  0)
    for i in range(20):
        for j in range(30):
            if l1[i][j] == 'H':
                pygame.draw.rect(DISPLAYSURF, brick, (20 * j, 20 * i, 20, 20))
                pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (20 * j, 20 * i, 20, 20), 1)
                pygame.draw.line(DISPLAYSURF, (0, 0, 0), (20 * (j + 1) - 5, 20 * i + 5), (20 * j + 5, 20 * (i + 1) - 5), 1)
                pygame.draw.line(DISPLAYSURF, (0, 0, 0), (20 * (j + 1) - 5, 20 * i + 9), (20 * j + 9, 20 * (i + 1) - 5), 1)
    if DISPLAYSURF.get_at((10, y_coordinate - 10)) == sky and DISPLAYSURF.get_at((10, y_coordinate + 10)) == sky:
        pygame.draw.circle(DISPLAYSURF, bird, (10, y_coordinate), 12, 0)
    else:
        gameover = 1
        hiscore = max(int(open('hiscore.txt', 'r').read()), score)
        open('hiscore.txt', 'w').write(str(hiscore))
        pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (180, 150, 240, 110))
        font = pygame.font.SysFont(None, 40)
        img1 = font.render('Game Over!', True, (255, 255, 255))
        img2 = font.render('Score : {}'.format(score), True, (255, 255, 255))
        img3 = font.render('High score : {}'.format(hiscore), True, (255, 255, 255))
        DISPLAYSURF.blit(img1, (225, 155))
        DISPLAYSURF.blit(img2, (225, 190))
        DISPLAYSURF.blit(img3, (185, 225))
        pygame.display.update()
        break
    for event in pygame.event.get():
        if gameover == 1:
            break
        if event.type == QUIT:
            gameover = 1
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            y_coordinate -= 10


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
