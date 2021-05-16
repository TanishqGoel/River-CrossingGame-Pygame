import pygame
import random
import math

from pygame import mixer
ind = 1

#Initialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Background
Background=pygame.image.load('Background.png')

# #Background Sound
# mixer.music.load('background.mp3')
# mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Crossing Roads")
icon=pygame.image.load('user.png')
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load('user.png')
playerX=380
playerY=520
playerX_change=0
playerY_change=0

level=0

#Player2
player2Img=pygame.image.load('user1.png')
player2X=380
player2Y=20
player2X_change=0
player2Y_change=0


#Obstacle1
Obstacle1Img=pygame.image.load('boat.png')
Obstacle1X=random.randint(35,720)
Obstacle1Y=300
Obstacle1X_change=0
Obstacle1Y_change=0

#Obstacle2
Obstacle2Img=pygame.image.load('boat.png')
Obstacle2X=random.randint(35,720)
Obstacle2Y=380
Obstacle2X_change=0
Obstacle2Y_change=0

#Obstacle3
Obstacle3Img=pygame.image.load('boat.png')
Obstacle3X=random.randint(35,720)
Obstacle3Y=460
Obstacle3X_change=0
Obstacle3Y_change=0

#Obstacle4
Obstacle4Img=pygame.image.load('boat.png')
Obstacle4X=random.randint(35,720)
Obstacle4Y=230
Obstacle4X_change=0
Obstacle4Y_change=0

#Obstacle5
Obstacle5Img=pygame.image.load('boat.png')
Obstacle5X=random.randint(35,720)
Obstacle5Y=160
Obstacle5X_change=0
Obstacle5Y_change=0

#Obstacle6
Obstacle6Img=pygame.image.load('boat.png')
Obstacle6X=random.randint(35,720)
Obstacle6Y=90
Obstacle6X_change=0
Obstacle6Y_change=0

#FixedObstacle1
F_Obstacle1X=147
F_Obstacle1Y=127

#FixedObstacle2
F_Obstacle2X=659
F_Obstacle2Y=117

#FixedObstacle3
F_Obstacle3X=348
F_Obstacle3Y=188

#FixedObstacle4
F_Obstacle4X=581
F_Obstacle4Y=257

#FixedObstacle5
F_Obstacle5X=262
F_Obstacle5Y=334

#FixedObstacle6
F_Obstacle6X=477
F_Obstacle6Y=334

#FixedObstacle7
F_Obstacle7X=185
F_Obstacle7Y=419

#Partitions

Partion1Y=117
Partion2Y=185
Partion3Y=266
Partion4Y=335
Partion5Y=422

#score
score_value=0
score_value2=0
font= pygame.font.Font('freesansbold.ttf',28)
textX=50
textY=40

def show_score(x,y):
	if ind==2:
		score =font.render("Score2: "+str(score_value2),True,(255,255,255))
		screen.blit(score,(x,y))

def show_score2(x,y):
	if ind==1:
		score2 =font.render("Score1: "+str(score_value),True,(255,255,255))
		screen.blit(score2,(x,y))

def show_time(x,y,time):
	Time =font.render("Time: "+str(time),True,(255,255,255))
	screen.blit(Time,(x,y))

def player(x,y):
	if ind ==1:
		screen.blit(playerImg,(x,y)) 

def player2(x,y):
	if ind == 2:
		screen.blit(player2Img,(x,y)) 

def Obstacle1(x,y):
	screen.blit(Obstacle1Img,(x,y)) 

def Obstacle2(x,y):
	screen.blit(Obstacle2Img,(x,y)) 

def Obstacle3(x,y):
	screen.blit(Obstacle3Img,(x,y))

def Obstacle4(x,y):
	screen.blit(Obstacle4Img,(x,y)) 

def Obstacle5(x,y):
	screen.blit(Obstacle5Img,(x,y)) 

def Obstacle6(x,y):
	screen.blit(Obstacle6Img,(x,y))



def isCollision(playerX,playerY,ObstacleX,ObstacleY):
	distance=math.sqrt((math.pow(ObstacleX-playerX,2))+(math.pow(ObstacleY-playerY,2)))
	if distance<27:
		return True

	else:
		return False

start  = pygame.time.get_ticks()

#Game Loop
running = True
while running:
	time = pygame.time.get_ticks() - start	
	score_value=-time/1000
	score_value2=-time/1000
	screen.fill((0,0,0))
	screen.blit(Background, (0,0))
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			running = False
	
		#if keystroke is pressed
		if ind==1:	
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					playerX_change = -1
				if event.key==pygame.K_RIGHT:
					playerX_change = 1
				if event.key==pygame.K_UP:
					playerY_change = -1
				if event.key==pygame.K_DOWN:
					playerY_change = 1

		#if keystroke is pressed
		if ind==2:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_a:
					player2X_change = -1
				if event.key==pygame.K_d:
					player2X_change = 1
				if event.key==pygame.K_w:
					player2Y_change = -1
				if event.key==pygame.K_s:
					player2Y_change = 1

		
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				playerX_change=0 	
			if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
				playerY_change=0

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_a or event.key==pygame.K_d:
				player2X_change=0 	
			if event.key==pygame.K_w or event.key==pygame.K_s:
				player2Y_change=0
	
	playerX+=playerX_change
	if playerX<=35:
		playerX=35
	elif playerX>=720:
		playerX=720
	
	playerY+=playerY_change		
	if playerY<=30:
		playerY=30
	elif playerY>=520:
		playerY=520

	player2X+=player2X_change
	if player2X<=35:
		player2X=35
	elif player2X>=720:
		player2X=720
	
	player2Y+=player2Y_change		
	if player2Y<=30:
		player2Y=30
	elif player2Y>=520:
		player2Y=520
	
	
	#player 1 score  
	if playerY<Partion1Y:
		score_value=score_value + 20
	if playerY<Partion2Y:
		score_value=score_value + 15
	if playerY<Partion3Y:
		score_value=score_value + 15
	if playerY<Partion4Y:
		score_value=score_value + 20
	if playerY<Partion5Y:
		score_value=score_value + 15

	if player2Y>Partion5Y:
		score_value2=score_value2 + 15
	if player2Y>Partion4Y:
		score_value2=score_value2 + 20
	if player2Y>Partion3Y:
		score_value2=score_value2 + 15
	if player2Y>Partion2Y:
		score_value2=score_value2 + 15
	if player2Y>Partion1Y:
		score_value2=score_value2 + 20 

	
	if Obstacle1X >=720:
		Obstacle1X = 35

	if Obstacle2X >=720:
		Obstacle2X = 35

	if Obstacle3X >=720:
		Obstacle3X = 35	

	if Obstacle4X >=720:
		Obstacle4X = 35

	if Obstacle5X >=720:
		Obstacle5X = 35

	if Obstacle6X >=720:
		Obstacle6X = 35		

	Obstacle1X +=1+level
	Obstacle2X +=1+level
	Obstacle3X +=1+level
	Obstacle4X +=1+level
	Obstacle5X +=1+level
	Obstacle6X +=1+level

	collision1=isCollision(playerX,playerY,Obstacle1X,Obstacle1Y)
	if collision1:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	collision2=isCollision(playerX,playerY,Obstacle2X,Obstacle2Y)
	if collision2:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	collision3=isCollision(playerX,playerY,Obstacle3X,Obstacle3Y)
	if collision3:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	collision4=isCollision(playerX,playerY,Obstacle4X,Obstacle4Y)
	if collision4:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	collision5=isCollision(playerX,playerY,Obstacle5X,Obstacle5Y)
	if collision5:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	collision6=isCollision(playerX,playerY,Obstacle6X,Obstacle6Y)
	if collision6:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485


	F_collision1=isCollision(playerX,playerY,F_Obstacle1X,F_Obstacle1Y)
	if F_collision1:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	F_collision2=isCollision(playerX,playerY,F_Obstacle2X,F_Obstacle2Y)
	if F_collision2:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	F_collision3=isCollision(playerX,playerY,F_Obstacle3X,F_Obstacle3Y)
	if F_collision3:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485
	
	F_collision4=isCollision(playerX,playerY,F_Obstacle4X,F_Obstacle4Y)
	if F_collision4:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485
	
	F_collision5=isCollision(playerX,playerY,F_Obstacle5X,F_Obstacle5Y)
	if F_collision5:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	F_collision6=isCollision(playerX,playerY,F_Obstacle6X,F_Obstacle6Y)
	if F_collision6:
		ind =2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485

	F_collision7=isCollision(playerX,playerY,F_Obstacle7X,F_Obstacle7Y)
	if F_collision7:
		ind=2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485
		

	if playerY<35:
		ind=2
		start  = pygame.time.get_ticks()
		playerX= 380
		playerY= 485
		level=level+1

	if player2Y>480:
		player2X= 380
		player2Y= 35
		level=level+1
		ind=1
		start  = pygame.time.get_ticks()


	collision1=isCollision(player2X,player2Y,Obstacle1X,Obstacle1Y)
	if collision1:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	collision2=isCollision(player2X,player2Y,Obstacle2X,Obstacle2Y)
	if collision2:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
		
	
	collision3=isCollision(player2X,player2Y,Obstacle3X,Obstacle3Y)
	if collision3:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	collision4=isCollision(player2X,player2Y,Obstacle4X,Obstacle4Y)
	if collision4:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	collision5=isCollision(player2X,player2Y,Obstacle5X,Obstacle5Y)
	if collision5:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	collision6=isCollision(player2X,player2Y,Obstacle6X,Obstacle6Y)
	if collision6:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	F_collision1=isCollision(player2X,player2Y,F_Obstacle1X,F_Obstacle1Y)
	if F_collision1:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35

	F_collision2=isCollision(player2X,player2Y,F_Obstacle2X,F_Obstacle2Y)
	if F_collision2:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35

	F_collision3=isCollision(player2X,player2Y,F_Obstacle3X,F_Obstacle3Y)
	if F_collision3:
		ind = 1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y=collision4=isCollision(player2X,player2Y,F_Obstacle4X,F_Obstacle4Y)
	if F_collision4:
		ind = 1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35

	F_collision5=isCollision(player2X,player2Y,F_Obstacle5X,F_Obstacle5Y)
	if F_collision5:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35

	F_collision6=isCollision(player2X,player2Y,F_Obstacle6X,F_Obstacle6Y)
	if F_collision6:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35
	
	F_collision7=isCollision(player2X,player2Y,F_Obstacle7X,F_Obstacle7Y)
	if F_collision7:
		ind =1
		start  = pygame.time.get_ticks()
		player2X= 380
		player2Y= 35

	player(playerX,playerY)
	player2(player2X,player2Y)
	Obstacle1(Obstacle1X,Obstacle1Y)
	Obstacle2(Obstacle2X,Obstacle2Y)
	Obstacle3(Obstacle3X,Obstacle3Y)
	Obstacle4(Obstacle4X,Obstacle4Y)
	Obstacle5(Obstacle5X,Obstacle5Y)
	Obstacle6(Obstacle6X,Obstacle6Y)
	show_score(textX,textY)
	show_score2(50,520)
	show_time(600,50,time/1000)

	pygame.display.update()