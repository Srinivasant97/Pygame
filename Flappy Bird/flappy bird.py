import pygame
import sys
import random

pygame.init()

screen= pygame.display.set_mode((400,600))

game_font=pygame.font.Font("freesansbold.ttf",30)

clock=pygame.time.Clock()

background= pygame.image.load('image/background.png').convert()
base=pygame.image.load('image/base.png').convert()
base=pygame.transform.scale2x(base)

bird=pygame.image.load('image/bird.png').convert_alpha()
bird_rect=bird.get_rect(center=(20,200))


pipe=pygame.image.load('image/pipe.png').convert()

Start=pygame.image.load('image/message.png').convert_alpha()


flip_pipe=pygame.transform.flip(pipe,False,True)
pipe_rect=pipe.get_rect(midtop=(350,350))
flip_pipe_rect=pipe.get_rect(midbottom=(pipe_rect.centerx,pipe_rect.centery-300))



Game=True
x_axis=0
def background1(x):
	screen.blit(background,(x,0))

def base1(x):
	screen.blit(base,(x,500))

birdy_axis=0
gravity=0.05
def bird1(y,x):
	bird_rotate=pygame.transform.rotozoom(bird,-y*10,1)
	screen.blit(bird_rotate,x)

def pipe1():
	screen.blit(pipe,pipe_rect)
	screen.blit(flip_pipe,flip_pipe_rect)

def collision(x,y):
	if bird_rect.colliderect(x) or bird_rect.colliderect(y):
		return True
		
sco=0

def Score(sco):
	scorebird=game_font.render(str(sco),True,(255,255,255))
	screen.blit(scorebird,(200,10))
	
def GameOver():
	Over=game_font.render("Game Over",True,(255,255,255))
	screen.blit(Over,(130,450))

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_UP:
				birdy_axis=0
				birdy_axis-=3
			if event.key==pygame.K_DOWN:
				birdy_axis+=3
			if event.key==pygame.K_SPACE:
				sco=0
				Game=True
				bird_rect=bird.get_rect(center=(20,200))
				birdy_axis=0
				pipe_rect=pipe.get_rect(midtop=(350,350))
				flip_pipe_rect=pipe.get_rect(midbottom=(pipe_rect.centerx,pipe_rect.centery-300))
			if event.key==pygame.K_RIGHT:
				bird_rect.centerx+=50
			if event.key==pygame.K_LEFT:
				bird_rect.centerx-=50
	
	x=-1
	x_axis+=x
	birdy_axis+=gravity
	bird_rect.centery+=birdy_axis
	background1(x_axis)
	base1(x_axis)
	if Game:
		pipe1()
		bird1(birdy_axis,bird_rect)
	else:
		GameOver()
		screen.blit(Start,(120,100))
	
	pipe_rect.centerx -=3
	flip_pipe_rect.centerx -=3

	if pipe_rect.centerx <=-10:
		if Game:
			sco+=1
		pipe_rect.centerx=400
		flip_pipe_rect.centerx=400
		pipe_rect.centery=random.choice([350,450,550])
		flip_pipe_rect.centery=pipe_rect.centery-450
	
	
	collision(pipe_rect,flip_pipe_rect)

	if collision(pipe_rect,flip_pipe_rect):
		Game=False

	if bird_rect.centery<=25:
		bird_rect.centery=27
	if bird_rect.centery>=475:
		bird_rect.centery=470

	if bird_rect.centerx<=30:
		bird_rect.centerx=30
	if bird_rect.centerx>375:
		bird_rect.centerx=350

	if x_axis<=-300:
		x_axis=0
	clock.tick(120)
	Score(sco)
	pygame.display.update()	
