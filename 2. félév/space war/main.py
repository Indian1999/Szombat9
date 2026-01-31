import pygame # pip install pygame (terminálba)
import os

WIDTH = 900
HEIGHT = 500

SPACESHIP_WIDTH = WIDTH // 11
SPACESHIP_HEIGHT = HEIGHT // 7

VELOCITY = 5 # pixel per frame

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War!")

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)

BACKGROUND = pygame.image.load(os.path.join(ASSETS, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

def draw_frame(red, yellow):
    WINDOW.blit(BACKGROUND, (0,0))

    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    pygame.display.update()

def red_control(red):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and red.x > 0:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_d] and red.x < WIDTH // 2 - SPACESHIP_WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_w] and red.y > 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_s] and red.y < HEIGHT - SPACESHIP_HEIGHT:
        red.y += VELOCITY

def yellow_control(yellow):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and yellow.x > WIDTH // 2:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and yellow.x < WIDTH - SPACESHIP_WIDTH:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP] and yellow.y > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y < HEIGHT - SPACESHIP_HEIGHT:
        yellow.y += VELOCITY

def main():
    red = pygame.Rect(20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, 
                        SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH - 20 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, 
                        SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    gameOn = True
    clock = pygame.time.Clock()
    while gameOn:
        clock.tick(60) # FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(
                        red.x + SPACESHIP_WIDTH,
                        red.y - SPACESHIP_HEIGHT // 2, 10, 5
                    )
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(
                        yellow.x - 10,
                        yellow.y - SPACESHIP_HEIGHT // 2, 10, 5
                    )
                    red_bullets.append(bullet)
        red_control(red)
        yellow_control(yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        draw_frame(red, yellow, red_bullets, yellow_bullets)

if __name__ == "__main__":
    main()
