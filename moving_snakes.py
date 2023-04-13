import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    def draw():
        surface.fill((0,0,0))
        surface.blit(blue_snake, (blue_snake_x, blue_snake_y))
        surface.blit(yellow_snake, (yellow_snake_x, yellow_snake_y))
        pygame.display.flip()

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

                if event.key == K_w:
                    blue_snake_y -= 10
                    draw()
                if event.key == K_s:
                    blue_snake_y += 10
                    draw()
                if event.key == K_a:
                    blue_snake_x -= 10
                    draw()
                if event.key == K_d:
                    blue_snake_x += 10
                    draw()

                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_LEFT:
                    pass
                if event.key == K_RIGHT:
                    pass

            elif event.type == QUIT:
                running = False

