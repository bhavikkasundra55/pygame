import pygame
import random

# Initialize pygame
pygame.init()

# Create Game screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Firing mortals')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player.png')
playerX = 400
playerY = 480
playerX_change = 0

enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(32, 250)
enemyX_change = 0.3
enemyY_change = 50

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


# Create game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 740:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
