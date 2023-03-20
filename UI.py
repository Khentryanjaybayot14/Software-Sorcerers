import pygame
from pygame.locals import *
import time

def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    bg = pygame.image.load("D:/snakegame_materials/background.jpg")
    surface = pygame.display.set_mode((500, 500))
    surface.fill((110, 110, 5))

    block = pygame.image.load("D:/snakegame_materials/block.jpg").convert()

    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))

    surface.blit(bg,(0,0))
    pygame.display.flip()

    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))
    pygame.display.update()
    running = True

    time.sleep(5)