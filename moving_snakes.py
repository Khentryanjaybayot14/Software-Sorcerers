import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()


    surface = pygame.display.set_mode((1000, 600))
    surface.fill((0,0,0))
    

    blue_snake = pygame.image.load("D:/snakegame_materials/blue_snake.png")
    blue_snake_x = 50
    blue_snake_y = 50
    surface.blit(blue_snake, (blue_snake_x, blue_snake_y))

    yellow_snake = pygame.image.load("D:/snakegame_materials/yellow_snake.jpg")
    yellow_snake_x = 400
    yellow_snake_y = 50
    surface.blit(yellow_snake, (yellow_snake_x, yellow_snake_y))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

