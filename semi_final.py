import pygame
from pygame.locals import *
import time
import random


size = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("D:/snakegame_materials/apple.jpg")
        self.parent_screen = parent_screen
        self.x = size * 3
        self.y = size * 3
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 22) * size
        self.y = random.randint(0, 13) * size


class Snake:
    def __init__(self, parent_screen, length, length1):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("D:/snakegame_materials/snake.png")
        self.length = length
        self.block_x = [size] * length
        self.block_y = [size] * length
        self.direction = "down"
        
        self.block1 = pygame.image.load("D:/snakegame_materials/block.jpg")
        self.length1 = length1
        self.block_x1 = [920] * length1
        self.block_y1 = [size] * length1
        self.direction1 = "down"

    
    
    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def increase_length1(self):
        self.length1 += 1
        self.block_x1.append(-1)
        self.block_y1.append(-1)

       
        

    def draw(self):
        self.parent_screen.fill((155,255,255))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        for j in range(self.length1):
            self.parent_screen.blit(self.block1, (self.block_x1[j], self.block_y1[j]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"
    def move_up1(self):
        self.direction1 = "up"

    def move_left(self):
        self.direction = "left"
    def move_left1(self):
        self.direction1 = "left"

    def move_right(self):
        self.direction = "right"
    def move_right1(self):
        self.direction1 = "right"

    def move_down(self):
        self.direction = "down"
    def move_down1(self):
        self.direction1 = "down"

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        
        if self.direction == "up":
            self.block_y[0] -= size
        if self.direction == "left":
            self.block_x[0] -= size
        if self.direction == "right":
            self.block_x[0] += size
        if self.direction == "down":
            self.block_y[0] += size
        self.draw()

        for j in range(self.length1 - 1, 0, -1):
            self.block_x1[j] = self.block_x1[j - 1]
            self.block_y1[j] = self.block_y1[j - 1]

        if self.direction1 == "up":
            self.block_y1[0] -= size
        if self.direction1 == "left":
            self.block_x1[0] -= size
        if self.direction1 == "right":
            self.block_x1[0] += size
        if self.direction1 == "down":
            self.block_y1[0] += size

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((155,255,255))
        self.snake = Snake(self.surface, 1, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

   
        

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
            return False


    def play(self):
        self.snake.walk()
        self.apple.draw()

        for i in range(self.snake.length):
            if self.is_collision(self.snake.block_x[i], self.snake.block_y[i], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()
        for j in range(self.snake.length1):
            if self.is_collision(self.snake.block_x1[j], self.snake.block_y1[j], self.apple.x, self.apple.y):
                self.snake.increase_length1()
                self.apple.move()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_UP:
                        self.snake.move_up1()

                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_LEFT:
                        self.snake.move_left1()

                    if event.key == K_d:
                        self.snake.move_right()
                    if event.key == K_RIGHT:
                        self.snake.move_right1()

                    if event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_DOWN:
                        self.snake.move_down1()

                elif event.type == QUIT:
                    exit()

            self.play()

            time.sleep(0.2)


if __name__ == "__main__":

    game = Game()
    game.run()



