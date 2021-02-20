import pygame
import random
from math import pow, sqrt

# Initialize pygame
pygame.init()

# Create Game screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Firing mortals')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background.png')

score = 0

playerimg = pygame.image.load('player1.png')
playerX = 400
playerY = 480
playerX_change = 0

enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(32, 250)
enemyX_change = 5
enemyY_change = 30

bulletimg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 480
bulletY_change = 8
bullet_state = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 1
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    dist = sqrt((pow(-bulletX + enemyX, 2)) + (pow(-bulletY + enemyY, 2)))
    if dist <= 27:
        return True
    return False


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
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state == 0:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 740:
        enemyX_change = -5
        enemyY += enemyY_change

    if bulletY <= 0:
        bullet_state = 0
        bulletY = 480

    if bullet_state == 1:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        score +=1
        bullet_state = 0
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(32, 250)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
