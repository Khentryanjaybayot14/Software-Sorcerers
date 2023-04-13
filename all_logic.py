
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
        self.level()
        pygame.display.flip()


    def level(self):
        if self.snake.length >= 6 and self.snake.length <= 10:
            self.surface.fill(blue)
        if self.snake.length1 >= 5 and self.snake.length1 <= 10:
            self.surface.fill(blue_green)

        if self.snake.length > 10 and self.snake.length <= 20:
            self.surface.fill(red)
        if self.snake.length1 > 10 and self.snake.length1 <= 20:
            self.surface.fill(violet)

        if self.snake.length > 20 and self.snake.length <= 30:
            self.surface.fill(green)
        if self.snake.length1 > 20 and self.snake.length1 <= 30:
            self.surface.fill(black)
        
        if self.snake.length > 30 and self.snake.length <= 40:
            self.surface.fill((102,102,255))#light blue
        if self.snake.length1 > 30 and self.snake.length1 <= 40:
            self.surface.fill((153,255,153)) #light green

        if self.snake.length > 40 and self.snake.length <= 50:
            self.surface.fill((255, 128, 0))#orange
        if self.snake.length1 > 40 and self.snake.length1 <= 50:
            self.surface.fill((160,160,160)) #gray

    def collide_with_other_snake(self):
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

        # self.collide_all_snake()
        self.colliding_with_itself()
        self.hit_boudary()
        pygame.display.flip()
        self.collide_with_other_snake()
        
    
        
    def display_score(self):
        font = pygame.font.SysFont("Arial", 20)
        self.score = font.render(f"Yellow Snake {self.snake.length1}", True, (255,255,255))
        self.surface.blit(self.score, (170, 10))
        self.score1 = font.render(f"Blue Snake {self.snake.length - 1}", True, (255,255,255))
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
        self.running = False
        self.pause = False
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
                        self.running = True
                        pygame.mixer.music.play()


                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_SPACE:
                        pygame.mixer.music.play()
                        howtoloop = False
                        self.running = True
                
                        
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_RETURN:
                        self.pause = False
                        pygame.mixer.music.play()
                    if not self.pause:
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
                        self.pause = True
                        pygame.mixer.music.pause()

                elif event.type == QUIT:
                    self.running = False
            try:
                if not self.pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                self.pause = True
                self.reset()
                
            self.Time()      
        
if __name__ == "__main__":
    game = Game()
    game.run()