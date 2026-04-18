import pygame # pip install pygame (terminálba)
import random

class Food:
    def __init__(self, x, y, pixel_size, xlim, ylim):
        self.random_pos()

    def random_pos(self):
        self.xpos = random.randint(0, self.xlim-self.pixel_size)
        self.ypos = random.randint(0, self.ylim-self.pixel_size)

    def draw(self, surf, color):
        pygame.draw.rect(surf, color, pygame.Rect(self.xpos, self.ypos, self.pixel_size, self.pixel_size))


class Snake:
    def __init__(self, x, y, speed, xlim, ylim):
        self.x = x
        self.y = y
        self.speed = speed
        self.xlim = xlim
        self.ylim = ylim
        self.length = 1
        self.x_vel = 0
        self.y_vel = 0
        self.dire = None
        self.is_dead = False
        self.body = [(self.x, self.y)]

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop(0)
        # Ellenerőzzik, hogy meghal-e
        self.is_dead = (self.x, self.y) in self.body[:-1]
        if self.x >= self.xlim or self.x < 0 or self.y >= self.ylim or self.y < 0:
            self.is_dead = True
    
    def set_direction(self, dire):
        if dire == "right" and self.dire != "left":
            self.dire = "right"
            self.x_vel = self.speed
            self.y_vel = 0
        elif dire == "left" and self.dire != "right":
            self.dire = "left"
            self.x_vel = -self.speed
            self.y_vel = 0
        elif dire == "up" and self.dire != "down":
            self.dire = "up"
            self.x_vel = 0
            self.y_vel = -self.speed
        elif dire == "down" and self.dire != "up": 
            self.dire = "down"
            self.x_vel = 0
            self.y_vel = self.speed

    def draw(self, surf, color):
        for pixel in self.body:
            pygame.draw.rect(surf, color, pygame.Rect(pixel[0], pixel[1], self.speed, self.speed))

class Game:
    BACKGROUND_COLOR = (123, 78, 67)
    SNAKE_COLOR = (0,0,0)
    FOOD_COLOR = (15, 218, 31)

    #Konstruktór
    def __init__(self, rows = 12, cols = 15, pixel_size = 30, fps = 10):
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.fps = fps
        self.width = cols * pixel_size
        self.height = rows * pixel_size
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

    def draw_frame(self):
        self.window.fill(Game.BACKGROUND_COLOR)

        self.snake.draw(self.window, Game.SNAKE_COLOR)

        pygame.display.update()

    def run(self):
        game_over = False
        app_close = False

        self.snake = Snake(
            x = 5*self.pixel_size, 
            y = 5*self.pixel_size,
            speed = self.pixel_size, 
            xlim = self.width, 
            ylim = self.height
        )

        while not app_close:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.set_direction("left")
                    if event.key == pygame.K_RIGHT:
                        self.snake.set_direction("right")
                    if event.key == pygame.K_UP:
                        self.snake.set_direction("up")
                    if event.key == pygame.K_DOWN:
                        self.snake.set_direction("down")
            
            self.snake.move()
            if self.snake.is_dead:
                game_over = True
                continue
            # Felevett-e egy kaját

            self.draw_frame()


jatek = Game() # A Game __init__() metódusát
jatek.run()