import pygame, sys
from pygame.locals import *
import time
import random
import webbrowser

link_color = (0,0,255)


pygame.init()

#font
font = pygame.font.SysFont('Agency fb', 23)
font1 = pygame.font.SysFont('algerian', 50)

#Headings
heading = "Software Sorcerers"
#names
bayot = "Khent Ryan Jay Bayot"
aribal = "Christian Aribal"
apostol = "Brenard Jairuz Apostol"
balusada = "Mary Gold Balusada"
baslan = "Christy Mae Baslan"
mons = "Dairel Monsuller"

#position
bayot_position = "Team Leader"
aribal_position = "Back End Developer"
apostol_position = "Back End Developer"
balusada_position = "User Interface Designer"
baslan_position = "Back End Developer"
mons_position = "User Interface Designer"

#pictures
bayot_pic = pygame.image.load("D:/bayot.png")
aribal_pic = pygame.image.load("D:/aribal.png")
apostol_pic = pygame.image.load("D:/apostol.png")
balusada_pic = pygame.image.load("D:/balusada.png")
baslan_pic = pygame.image.load("D:/baslan.png")
mons_pic = pygame.image.load("D:/monsuller.png")


#fb links
bayot_link = r"https://www.facebook.com/khentrj.tuppal"
aribal_link = r'''https://www.facebook.com/profile.php?id=100075138132589'''
apostol_link = r"https://www.facebook.com/skim.carme"
balusada_link = r"https://www.facebook.com/profile.php?id=100076475830733"
baslan_link = r"https://www.facebook.com/ytsirhc.nalsab.5"
mons_link = r"https://www.facebook.com/"
default_link = "Facebook.com"

############################################################################################################
ui = pygame.display.set_mode((1320,680))
ui.fill((0,100,0))

#inerting position
bayot_font_position = font.render(bayot_position, True, (255,255,255))
ui.blit(bayot_font_position, (618,325))
aribal_font_position = font.render(aribal_position, True, (255,255,255))
ui.blit(aribal_font_position, (96, 580))
apostol_font_position = font.render(apostol_position, True, (255,255,255))
ui.blit(apostol_font_position, (346, 580))
balusada_font_position = font.render(balusada_position, True, (255,255,255))
ui.blit(balusada_font_position, (579,580))
baslan_font_position = font.render(baslan_position, True, (255,255,255))
ui.blit(baslan_font_position, (846, 580))
mons_font_position = font.render(aribal_position, True, (255,255,255))
ui.blit(mons_font_position, (1098,580))

#inserting links

bayot_font_link = ui.blit(font.render(default_link, True, link_color), (615,350))
aribal_hyperlink = ui.blit(font.render(default_link, True, link_color), (110, 605))
apostol_hyperlink = ui.blit(font.render(default_link, True, link_color), (363, 605))
balusada_hyperlink = ui.blit(font.render(default_link, True, link_color), (615, 605))
baslan_hyperlink = ui.blit(font.render(default_link, True, link_color), (867, 605))
mons_hyperlink = ui.blit(font.render(default_link, True, link_color), (1115, 605))

#inserting heading
heading_font = font1.render(heading, True, (0,255,255))
ui.blit(heading_font, (400, 50))

#inserting names
bayot_name = font.render(bayot, True, (255,255,0))
ui.blit(bayot_name, (590, 300))
aribal_name = font.render(aribal, True, (255,255,0))
ui.blit(aribal_name, (107, 555))
apostol_name = font.render(apostol, True, (255,255,0))
ui.blit(apostol_name, (331, 555))
balusada_name = font.render(balusada, True, (255,255,0))
ui.blit(balusada_name, (596, 555))
baslan_name = font.render(baslan, True, (255,255,0))
ui.blit(baslan_name, (846,555))
mons_name = font.render(mons, True, (255,255,0))
ui.blit(mons_name, (1106,555))


#inserting image
ui.blit(bayot_pic, (600,200))
ui.blit(aribal_pic, (100, 450))
ui.blit(apostol_pic, (350, 450))
ui.blit(balusada_pic, (600, 450))
ui.blit(baslan_pic, (850, 450))
ui.blit(mons_pic, (1100, 450))

#click me
color_ = (0,0,0)
color_1 = (0,0,0)
cfont = pygame.font.SysFont("Agency fb", 45)
click_me = ui.blit(cfont.render("Click me to continue", True, color_), (160,225))
click_me1 = ui.blit(cfont.render("Click space to continue", True, color_1), (900, 230))

############################################################################################################
run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            if event.key == K_SPACE:
                run = False
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if bayot_font_link.collidepoint(pos):
                webbrowser.open(bayot_link)
            if aribal_hyperlink.collidepoint(pos):
                webbrowser.open(aribal_link)
            if apostol_hyperlink.collidepoint(pos):
                webbrowser.open(apostol_link)
            if balusada_hyperlink.collidepoint(pos):
                webbrowser.open(balusada_link)
            if baslan_hyperlink.collidepoint(pos):
                webbrowser.open(baslan_link)
            if mons_hyperlink.collidepoint(pos):
                webbrowser.open(mons_link)

            if click_me.collidepoint(pos):
                run = False

    if click_me.collidepoint(pygame.mouse.get_pos()):
        link_color = (255,255,255)
    else:
        link_color = (255,255,255)
        
    pygame.display.update()



black = (0,0,0)
green = (10,249, 50)
red = (255,0,0)

blue_green = (0,255,247)
blue = (34,0,255)
violet = (222,0,255)

size = 40
background_color = (110,110,5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_x = random.randint(1,32) * size
        self.apple_y = random.randint(1,16) * size
        self.apple = pygame.image.load("D:/snakegame_materials/apples.jpg").convert()

    def move(self):
        self.apple_x = random.randint(1, 32) * size
        self.apple_y = random.randint(1, 16) * size
        pygame.display.flip()

    def draw(self):
        self.parent_screen.blit(self.apple, (self.apple_x, self.apple_y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length, length1):
        self.parent_screen = parent_screen
        self.direction = 'down'
        self.snake = pygame.image.load("D:/snakegame_materials/blocks.jpg").convert()

        self.length = length
        self.block_x = [600] * length
        self.block_y = [size] * length
        
        # self.block_x1 = [1040] * length1

        self.snake1 = pygame.image.load("D:/snakegame_materials/blocks1.png").convert()
        self.direction1 = 'up'

        self.length1 = length1
        self.block_x1 = [600] * length1 #
        self.block_y1 = [600] * length1

        self.x = len(self.block_x)
        self.x1 = len(self.block_x1)

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)
    def increase_length1(self):
        self.length1 += 1
        self.block_x1.append(-1)
        self.block_y1.append(-1)

    def draw(self):
        for i in range(self.length1):
            self.parent_screen.blit(self.snake, (self.block_x1[i], self.block_y1[i]))
        for j in range(self.length):
            self.parent_screen.blit(self.snake1, (self.block_x[j], self.block_y[j]))
        pygame.display.flip()

    def move_down(self):
        self.direction = "down"

    def move_up(self):
        self.direction = "up"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_down1(self):
        self.direction1 = "down"

    def move_up1(self):
        self.direction1 = "up"

    def move_left1(self):
        self.direction1 = "left"

    def move_right1(self):
        self.direction1 = "right"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        if self.direction == "down":
            self.block_y[0] += size
        if self.direction == "up":
            self.block_y[0] -= size
        if self.direction == "right":
            self.block_x[0] += size
        if self.direction == "left":
            self.block_x[0] -= size
        self.draw()

        for j in range(self.length1 - 1, 0, -1):
            self.block_x1[j] = self.block_x1[j - 1]
            self.block_y1[j] = self.block_y1[j - 1]
        if self.direction1 == "down":
            self.block_y1[0] += size
        if self.direction1 == "up":
            self.block_y1[0] -= size
        if self.direction1 == "right":
            self.block_x1[0] += size
        if self.direction1 == "left":
            self.block_x1[0] -= size
        self.draw()
        
class Game:
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((1320,680))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface, length=2, length1=1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
            return False
    
    def hit_boudary(self):
        if not (0 <= self.snake.block_x[0] <= 1319 and 0 <= self.snake.block_y[0] <= 650):
            sound = pygame.mixer.Sound("D:/snakegame_materials/crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "Hit the boundry error"
        if not (0 <= self.snake.block_x1[0] <= 1319 and 0 <= self.snake.block_y1[0] <= 650):
            sound = pygame.mixer.Sound("D:/snakegame_materials/crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "Hit the boundry error"

    def colliding_with_apple(self):
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.apple_x, self.apple.apple_y):
            sound = pygame.mixer.Sound("D:/snakegame_materials/ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()
        if self.is_collision(self.snake.block_x1[0], self.snake.block_y1[0], self.apple.apple_x, self.apple.apple_y):
            sound = pygame.mixer.Sound("D:/snakegame_materials/ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length1()
            self.apple.move()

    def colliding_with_itself(self):
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i], self.snake.block_y[i]):
                sound1 = pygame.mixer.Sound("D:/snakegame_materials/crash.mp3")
                pygame.mixer.Sound.play(sound1)
                raise "Game over"
        for j in range(1, self.snake.length1):
            if self.is_collision(self.snake.block_x1[0], self.snake.block_y1[0], self.snake.block_x1[j], self.snake.block_y1[j]):
                sound1 = pygame.mixer.Sound("D:/snakegame_materials/crash.mp3")
                pygame.mixer.Sound.play(sound1)
                raise "Game over"
            
    def play_background_music(self):
        pygame.mixer.music.load("D:/snakegame_materials/pou1.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        self.bg = pygame.image.load("D:/snakegame_materials/background.jpg")
        self.surface.blit(self.bg, (0,0))
        pygame.display.flip()

    def level(self):
        if self.snake.length >= 5 and self.snake.length <= 10:
            self.surface.fill(green)
            
        if self.snake.length1 >= 5 and self.snake.length1 <= 10:
            self.surface.fill(blue_green)

        if self.snake.length > 10 and self.snake.length <= 20:
            self.surface.fill(red)
        if self.snake.length1 > 10 and self.snake.length1 <= 20:
            self.surface.fill(violet)

        if self.snake.length > 20 and self.snake.length <= 30:
            self.surface.fill(blue)
        if self.snake.length1 > 20 and self.snake.length1 <= 30:
            self.surface.fill(black)
        pygame.display.flip()

    def f(self):
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x1[0], self.snake.block_y1[0]):
            sound = pygame.mixer.Sound("D:/snakegame_materials/crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "collide with other snake"

    


    def play(self):
        self.render_background()
        self.level()
        self.snake.walk() 
        self.apple.draw()
        self.display_score()
        self.colliding_with_apple()
        pygame.display.flip()

        self.colliding_with_itself()
        self.hit_boudary()
        self.f()
    
        
    def display_score(self):
        font = pygame.font.SysFont("Arial", 20)
        self.score = font.render(f"Yellow Snake {self.snake.length - 1}", True, (255,255,255))
        self.surface.blit(self.score, (170, 10))
        self.score1 = font.render(f"Blue Snake {self.snake.length1}", True, (255,255,255))
        self.surface.blit(self.score1, (1000, 10))

    def show_game_over(self):
        self.surface.fill(background_color)
        font = pygame.font.SysFont("Arial", 30)
        line1 = font.render(f"Score: Yellow Snake {self.snake.length - 1}", True, (255,255,0))
        self.surface.blit(line1, (510,200))
        line2 = font.render("To play again hit enter, to exit pres Escape", True, (255,255,255))
        self.surface.blit(line2, (400,400))

        font1 = pygame.font.SysFont("Arial", 50)
        line21 = font1.render("Game over", True, (255,0,0))
        self.surface.blit(line21, (520,300))
        line3 = font.render(f"Score: Blue Snake {self.snake.length1}", True, (0,0,255))
        self.surface.blit(line3, (510,250))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def text_pause(self):
        font = pygame.font.SysFont("Arial", 50)
        line = font.render("Game paused, Press Enter to resume, press ESC to exit", True, (0,0,0))
        self.surface.blit(line, (120,300))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, length=2, length1=1)
        self.apple = Apple(self.surface)

    def Time(self):
        self.t = time.sleep(0.1)



    def run(self):
        running = False
        pause = False
        howtoloop = True
        
        font2 = pygame.font.SysFont('Agency fb', 30)
        font7 = pygame.font.SysFont('Arial', 35)

        howto_1 = "How to Play:"
        howto_2 = "Player 1 = W,A,S,D controls the Yellow Snake."
        howto_3 = "player 2 = Arrow keys control the Blue Snake."
        howto_4 = "key space to pause the game"
        howto_5 = "key enter to resume"
        howto_6 = "key esc to quit"
        howto_7 = "Press Key_Space to Play"

        while howtoloop:
            pygame.mixer.music.stop()
            light_green = 102,255,255
            light_green1 = 178, 255, 102
            light_pink = 255,153,253
            light_red = 255,153,51
            
            self.surface.fill((0,102,0))
            h1 = font2.render(howto_1, True, (light_green))
            h2 = font2.render(howto_2, True, (light_pink))
            h3 = font2.render(howto_3, True, (light_red))
            h4 = font2.render(howto_4, True, (light_green1))
            h5 = font2.render(howto_5, True, (0, 0, 0))
            h6 = font2.render(howto_6, True, (0, 0, 0))
            h7 = font7.render(howto_7, True, (255,255,51))

            self.surface.blit(h1, (350, 20))
            self.surface.blit(h2, (480, 100))
            self.surface.blit(h3, (480, 140))
            self.surface.blit(h4, (480, 180))
            self.surface.blit(h5, (480, 220))
            self.surface.blit(h6, (480, 260))
            self.surface.blit(h7, (480, 600))

            c1 = (0,0,0)
            clickme = self.surface.blit(font7.render("Press me to continue", True, c1), (480, 550))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = event.pos
                    if clickme.collidepoint(pos1):
                        howtoloop = False
                        running = True
                        pygame.mixer.music.play()


                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_SPACE:
                        pygame.mixer.music.play()
                        howtoloop = False
                        running = True
                
                        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                        pygame.mixer.music.play()
                    if not pause:
                        if event.key == K_s:
                            self.snake.move_down()
                        if event.key == K_w:
                            self.snake.move_up()
                        if event.key == K_a:
                            self.snake.move_left()
                        if event.key == K_d:
                            self.snake.move_right()

                        if event.key == K_DOWN:
                            self.snake.move_down1()
                        if event.key == K_UP:
                            self.snake.move_up1()
                        if event.key == K_LEFT:
                            self.snake.move_left1()
                        if event.key == K_RIGHT:
                            self.snake.move_right1()

                    if event.key == K_SPACE:
                        self.text_pause()
                        pause = True
                        pygame.mixer.music.pause()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
                
            self.Time()      
        
if __name__ == "__main__":
    game = Game()
    game.run()