import pygame
import random

# Initialize pygame
pygame.init()

# Create Game screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Firing mortals')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background.png')

playerimg = pygame.image.load('player1.png')
playerX = 400
playerY = 480
playerX_change = 0

enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(32, 250)
enemyX_change = 3
enemyY_change = 50

bulletimg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 480
bulletX_change = 3
bulletY_change = 10
bullet_state = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 1
    screen.blit(bulletimg,(x+16,y+10))


# Create game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)
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
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 740:
        enemyX_change = -2
        enemyY += enemyY_change

    if bullet_state == 1:
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
