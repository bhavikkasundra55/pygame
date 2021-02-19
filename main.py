import pygame

#Initialize pygame
pygame.init()

# Create Game screen
screen = pygame.display.set_mode((720,720))

#Create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
