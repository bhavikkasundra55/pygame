import pygame
#Initialize pygame
pygame.init()
# Create Game screen
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Firing mortals')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player.png')
playerX = 400
playerY = 480

def player(x,y):
    screen.blit(playerimg,(x,y))

#Create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = 0.1
            if event.type == pygame.K_RIGHT:
                playerX_change = 0.1

    screen.fill((0,0,0))
    player()
    pygame.display.update()
