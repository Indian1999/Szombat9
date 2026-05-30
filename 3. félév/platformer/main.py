import pygame # pip install pygame (terminálba)
import random
import os
pygame.font.init()

class Game:
    WIDTH = 400
    HEIGHT = 500
    FPS = 60
    FRICTION = 0.15 #Ennyi százalékkal csökkentjük a gyorsulást

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Platformer Game")

    def draw_frame(self):
        self.window.fill((200,160,200))

        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, sprite.rect)

        pygame.display.update()

    def run(self):
        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.main_platform = Platform()
        self.all_sprites.add(self.main_platform)
        self.platforms.add(self.main_platform)

        while True:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.player.move(self.platforms)

            self.draw_frame()

class Player(pygame.sprite.Sprite):
    ACC = 0.5
    WIDTH = 50
    HEIGHT = 50
    def __init__(self):
        super().__init__() # Meghívja az ősosztály (Sprite) konstuktorát
        self.surf = pygame.Surface((Player.WIDTH, Player.HEIGHT))
        self.surf.fill((210,35,89))
        self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT - 40))

        self.pos = self.rect.bottomleft # (30, 40)
        self.pos = pygame.Vector2(self.pos[0], self.pos[1])
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def move(self, platforms):
        self.acc = pygame.Vector2(0, 0.98) # gravitációs gyorsulás
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.acc.x = -Player.ACC
        if keys_pressed[pygame.K_RIGHT]:
            self.acc.x = Player.ACC

        self.acc.x -= self.vel.x * Game.FRICTION
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x + Player.WIDTH < 0:
            self.pos.x = Game.WIDTH
        if self.pos.x > Game.WIDTH:
            self.pos.x = -Player.WIDTH 
        
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top
            self.vel.y = 0

        self.rect.bottomleft = self.pos

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((Game.WIDTH, 20))
        self.surf.fill((40,50,60))
        self.rect = self.surf.get_rect(bottomleft=(0, Game.HEIGHT))

game = Game()
game.run()