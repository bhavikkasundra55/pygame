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
font = pygame.font.Font('freesansbold.ttf',32)
fontX = 10
fontY = 10

def show_score(x,y):
    score_value = font.render('Score : '+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

playerimg = pygame.image.load('player1.png')
playerX = 400
playerY = 480
playerX_change = 0

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemy = 3

for i in range(no_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(32, 150))
    enemyX_change.append(5)
    enemyY_change.append(30)

bulletimg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 480
bulletY_change = 8
bullet_state = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


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

    for i in range(no_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            score += 1
            bullet_state = 0
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(32, 250)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bullet_state = 0
        bulletY = 480

    if bullet_state == 1:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(fontX,fontY)
    pygame.display.update()
