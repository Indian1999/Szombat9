import pygame # pip install pygame (terminálba)
import os
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

SPACESHIP_WIDTH = WIDTH // 11
SPACESHIP_HEIGHT = HEIGHT // 7

VELOCITY = 5 # pixel per frame

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War!")

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

LASER_SOUND = pygame.mixer.Sound(os.path.join(ASSETS, "laser.wav"))
LASER_SOUND.set_volume(0.2)

EXPLOSION_SOUND = pygame.mixer.Sound(os.path.join(ASSETS, "explosion.wav"))
EXPLOSION_SOUND.set_volume(0.2)

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)

BACKGROUND = pygame.image.load(os.path.join(ASSETS, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

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

def draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WINDOW.blit(BACKGROUND, (0,0))

    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, (255, 255, 0), bullet)

    font = pygame.font.SysFont("Arial", 40)
    red_text = font.render(f"Red health: {red_health}", True, (255, 255, 255))
    yellow_text = font.render(f"Yellow health: {yellow_health}", True, (255, 255, 255))
    WINDOW.blit(red_text, (10, 10))
    WINDOW.blit(yellow_text, (WIDTH - yellow_text.get_width() - 10, 10))

    pygame.display.update()

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x += VELOCITY + 2
        if bullet.x > WIDTH + 50:
            red_bullets.remove(bullet)
        if bullet.colliderect(yellow):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= (VELOCITY + 2)
        if bullet.colliderect(red):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x < -50:
            yellow_bullets.remove(bullet)

def draw_winner(text):
    font = pygame.font.SysFont("Arial", 100)
    surf = font.render(text, True, (255, 255, 255))
    WINDOW.blit(surf, (WIDTH//2 - surf.get_width() // 2, HEIGHT//2 - surf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000) # 5000 ms -> 5 s

def main():
    red = pygame.Rect(20, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, 
                        SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH - 20 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, 
                        SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10
    
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
                if event.key == pygame.K_LCTRL and len(red_bullets) < 3:
                    bullet = pygame.Rect(
                        red.x + SPACESHIP_WIDTH,
                        red.y + SPACESHIP_HEIGHT // 2, 10, 5
                    )
                    red_bullets.append(bullet)
                    LASER_SOUND.play()
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < 3:
                    bullet = pygame.Rect(
                        yellow.x - 10,
                        yellow.y + SPACESHIP_HEIGHT // 2, 10, 5
                    )
                    yellow_bullets.append(bullet)
                    LASER_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                EXPLOSION_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                EXPLOSION_SOUND.play()

        red_control(red)
        yellow_control(yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        if red_health <= 0:
            gameOn = False
            draw_winner("Yellow Wins!")
        if yellow_health <= 0:
            gameOn = False
            draw_winner("Red Wins!")

if __name__ == "__main__":
    main()
