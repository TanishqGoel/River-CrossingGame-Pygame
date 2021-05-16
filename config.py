import pygame
import random
pygame.init()
Background=pygame.image.load('Background.png')


pygame.display.set_caption("Crossing Roads")
icon=pygame.image.load('user.png')
pygame.display.set_icon(icon)
playerImg=pygame.image.load('user.png')

player2Img=pygame.image.load('user1.png')
Obstacle1Img=pygame.image.load('boat.png')
Obstacle2Img=pygame.image.load('boat.png')
Obstacle3Img=pygame.image.load('boat.png')
Obstacle4Img=pygame.image.load('boat.png')
Obstacle5Img=pygame.image.load('boat.png')
Obstacle6Img=pygame.image.load('boat.png')
font= pygame.font.Font('freesansbold.ttf',28)
ind = 1
