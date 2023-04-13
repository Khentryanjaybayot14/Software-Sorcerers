import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.yellow_snake = pygame.image.load("D:/snakegame_materials/yellow_snake.jpg")
        self.yellow_snake_x = 400
        self.yellow_snake_y = 50
        self.direction1 = "down"
        
        self.blue_snake = pygame.image.load("D:/snakegame_materials/blue_snake.png")
        self.blue_snake_x = 50
        self.blue_snake_y = 50
        self.direction = "down"
    def draw(self):
        self.parent_screen.fill((0,0,0))
        self.parent_screen.blit(self.blue_snake, (self.blue_snake_x, self.blue_snake_y))
        self.parent_screen.blit(self.yellow_snake, (self.yellow_snake_x, self.yellow_snake_y))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"

    def move_up1(self):
        self.direction1 = "up"
    def move_down1(self):
        self.direction1 = "down"
    def move_left1(self):
        self.direction1 = "left"
    def move_right1(self):
        self.direction1 = "right"

    def walk(self):
        if self.direction == "up":
            self.yellow_snake_y -= 10
        if self.direction == "down":
            self.yellow_snake_y += 10
        if self.direction == "left":
            self.yellow_snake_x -= 10
        if self.direction == "right":
            self.yellow_snake_x += 10

        if self.direction1 == "up":
            self.blue_snake_y -= 10
        if self.direction1 == "down":
            self.blue_snake_y += 10
        if self.direction1 == "left":
            self.blue_snake_x -= 10
        if self.direction1 == "right":
            self.blue_snake_x += 10
        
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((0,0,0))
        self.snake = Snake(self.surface)
        self.snake.draw()      

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_w:
                        self.snake.move_up1()
                    if event.key == K_s:
                        self.snake.move_down1()
                    if event.key == K_a:
                        self.snake.move_left1()
                    if event.key == K_d:
                        self.snake.move_right1()

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
        
            self.snake.walk()
            time.sleep(.3)

if __name__ == "__main__":
    game = Game()
    game.run()
   