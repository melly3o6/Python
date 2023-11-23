# libraries

import pygame
import os
pygame.init()
#########################################################################################
# variables

LIVES = 5
LEVEL = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#########################################################################################
# window

GAME_SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
pygame.display.set_caption('S P A C E I N V A D E R S')
WIDTH, HEIGHT = pygame.display.get_window_size()
TITLE_FONT = pygame.font.SysFont("comicsans", WIDTH // 14)
SUBTITLE_FONT = pygame.font.SysFont("comicsans", WIDTH // 20)
TEXT_FONT = pygame.font.SysFont("comicsans", WIDTH // 40)

#########################################################################################
# image
PLAYING_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "PLAYING_BACKGROUND.png")),
                                            (WIDTH, HEIGHT))
#########################################################################################
# player and laser images

SPACESHIP_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("Images", "SpaceShipGreen.png")),
                                         (WIDTH // 10, HEIGHT // 6))

LASER_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("Images", "LaserGreen.png")),
                                     (WIDTH // 10, HEIGHT // 20))
#########################################################################################
# class


class Laser:
    def __init__(self, x, y, laser_img):
        self.x = x
        self.y = y
        self.laser_img = laser_img
        self.speed = player.speed
        self.mask = pygame.mask.from_surface(self.laser_img)

    def draw(self):
        GAME_SCREEN.blit(self.laser_img, (self.x, self.y))

    def move(self):
        self.y -= self.speed


class Player:
    def __init__(self, x, y, ship_img):
        self.x = x
        self.y = y
        self.speed = WIDTH // 100
        self.ship_img = ship_img
        self.mask = pygame.mask.from_surface(self.ship_img)

        self.lasers = []

    def draw(self):
        GAME_SCREEN.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def movement_handling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed + self.get_width() < WIDTH:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed > HEIGHT // 4 * 3:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed + self.get_height() < HEIGHT:
            self.y += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()
            self.update_laser()

    def shoot(self):
        laser = Laser(self.x // 2, self.y, LASER_GREEN)
        self.lasers.append(laser)

    def update_laser(self):
        for laser in self.lasers:
            laser.draw()
            laser.move()
            if laser.y < 0:
                self.lasers.remove(laser)

#########################################################################################


position = 0


def background_moving():
    global position
    GAME_SCREEN.fill(BLACK)

    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position))
    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position - PLAYING_BACKGROUND.get_height()))

    position += 0.3
    if abs(position) > PLAYING_BACKGROUND.get_height():
        position = 0


#########################################################################################
# create objects
player = Player(WIDTH // 2, HEIGHT - WIDTH // 8, SPACESHIP_GREEN)
#########################################################################################
# LOOP FOR SETUP

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit()

    background_moving()
    player.draw()
    pygame.display.update()
    player.movement_handling()
#########################################################################################
