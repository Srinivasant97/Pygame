import pygame
import random
import math
from pygame import mixer

pygame.init()

pygame_Window = pygame.display.set_mode((800,600))
running = True

mixer.music.load('background.wav')
mixer.music.play(-1)

Background = pygame.image.load('galaxy.jpg')
Icon = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(Icon)


playerImg = pygame.image.load('space-invaders.png')
Xaxis = 380
Yaxis = 450
X_change = 0

no_of_enemy = 5

EnemyImg = []
Enemy_Xaxis =[]
Enemy_Yaxis = []
Enemy_X_Change = []
Enemy_Y_Change = []
for i in range(no_of_enemy):
    EnemyImg.append(pygame.image.load('rocksteady.png'))
    Enemy_Xaxis.append(random.randint(10,735))
    Enemy_Yaxis.append(random.randint(50,150))
    Enemy_X_Change.append(5)
    Enemy_Y_Change.append(40)

BulletImg = pygame.image.load("B.png")
Bullet_Xaxis = 0
Bullet_Yaxis = Yaxis
Bullet_X_Change = 0
Bullet_Y_Change = 0
Bullet_state= "Ready"
score = 0
Score_string = pygame.font.Font('freesansbold.ttf',32)

GameOver = pygame.font.Font('freesansbold.ttf',64)


def Score_s(x,y):
    Score_value= Score_string.render("Score:"+str(score),True,(255,255,255))
    pygame_Window.blit(Score_value,(x,y))


def player(x,y):
    pygame_Window.blit(playerImg,(x,y))

def Enemy(x,y,i):
    pygame_Window.blit(EnemyImg[i], (x,y))

def Bullet(x,y):
    pygame_Window.blit(BulletImg, (x+15,y+10))


def Game_over(x,y):
    GameOver_string= GameOver.render("Game Over",True,(255,255,255))
    pygame_Window.blit(GameOver_string,(x,y))


def Collision(Enemyx,Bulletx,EnemyY,BulletY):
    distance = math.sqrt((math.pow(Enemyx - Bulletx,2))+(math.pow(EnemyY - BulletY,2)))
    if distance < 27:
        return True
    else:
        return False
while running:
    pygame_Window.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_change = -5
            if event.key == pygame.K_RIGHT:
                X_change = 5
            if event.key == pygame.K_UP:
                if Bullet_state == "Ready":
                    Bullet_Sound = mixer.Sound('laser.wav')
                    Bullet_Sound.play()
                    Bullet_Xaxis = Xaxis
                    Bullet_Y_Change = 4
                    Bullet_state = "Fired"


        if event.type == pygame.KEYUP:
            X_change =0






    Xaxis += X_change
    if Bullet_state == "Ready":
        Bullet_Xaxis = Xaxis

    if Xaxis <= 0:
        Xaxis =0
    if Xaxis >=735:
        Xaxis = 735

    for i in range(no_of_enemy):
        if Enemy_Yaxis[i] > 420:
            for j in range(no_of_enemy):
                Enemy_Yaxis[j]=2000
            Game_over(300,250)
            break

    Bullet(Bullet_Xaxis, Bullet_Yaxis)
    player(Xaxis, Yaxis)
    Bullet_Yaxis -= Bullet_Y_Change
    if Bullet_Yaxis <= 0:
        Bullet_Yaxis = 450
        if Bullet_state == "Fired":
            Bullet_Y_Change = 0
            Bullet_Xaxis = Xaxis
            Bullet_state = "Ready"


    for i in range(no_of_enemy):
        Enemy_Xaxis[i] += Enemy_X_Change[i]
        if Enemy_Xaxis[i] >= 735:
            Enemy_X_Change[i] = -5
            Enemy_Yaxis[i] += Enemy_Y_Change[i]
        if Enemy_Xaxis[i] <= 0:
            Enemy_X_Change[i] = 5
            Enemy_Yaxis[i] += Enemy_Y_Change[i]

        Collide = Collision(Enemy_Xaxis[i],Bullet_Xaxis,Enemy_Yaxis[i],Bullet_Yaxis)
        if Collide:
            Collision_sound = mixer.Sound('explosion.wav')
            Collision_sound.play()
            Bullet_Yaxis = 450
            Bullet_state = "Ready"
            Bullet_Y_Change = 0
            Enemy_Xaxis[i] = random.randint(10,735)
            Enemy_Yaxis[i] = random.randint(50,150)
            score += 1

        Enemy(Enemy_Xaxis[i],Enemy_Yaxis[i],i)
        Score_s(10, 10)

    pygame.display.update()

