##################################################################################
# libraries

import pygame
import os
pygame.init()

##################################################################################
# constant variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LEVEL = 1
LIVES = 5

##################################################################################
# window

GAME_SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
pygame.display.set_caption("S P A C E I N V A D E R S")
WIDTH, HEIGHT = pygame.display.get_window_size()
TITLE_FONT = pygame.font.SysFont("comicsans", WIDTH // 14)
SUBTITLE_FONT = pygame.font.SysFont("comicsans", WIDTH // 20)
TEXT_FONT = pygame.font.SysFont("comicsans", WIDTH // 40)

##################################################################################
# images

SPACESHIP_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("Images", "SpaceShipGreen.png")),
                                         (WIDTH // 10, HEIGHT // 6))

LASER_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("Images", "LaserGreen.png")),
                                     (WIDTH // 10, HEIGHT // 20))

##################################################################################
# scenes

# Menu scene


MENU_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "MENU_BACKGROUND.png")),
                                         (WIDTH, HEIGHT))

MENU_TEXT = TITLE_FONT.render("SPACE INVADERS", True, WHITE)
MENU_TEXT_RECT = MENU_TEXT.get_rect()
MENU_TEXT_RECT.center = WIDTH // 2, HEIGHT // 10

MENU_TEXT2 = SUBTITLE_FONT.render("CLICK TO START", True, WHITE)
MENU_TEXT2_RECT = MENU_TEXT2.get_rect()
MENU_TEXT2_RECT.center = WIDTH // 2, HEIGHT // 2

# GameOver scene

GAMEOVER_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "GAMEOVER_BACKGROUND.png")),
                                             (WIDTH, HEIGHT))

# Playing scene

PLAYING_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "PLAYING_BACKGROUND.png")),
                                            (WIDTH, HEIGHT))

position = 0


def background_moving():  # https://www.youtube.com/watch?v=clm7kv88XPs
    global position
    GAME_SCREEN.fill(BLACK)

    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position))
    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position - PLAYING_BACKGROUND.get_height()))

    position += 0.3
    if abs(position) > PLAYING_BACKGROUND.get_height():
        position = 0


LIVES_LABEL = TEXT_FONT.render(f"LIVES: {LIVES}", True, RED)
LIVES_LABEL_RECT = LIVES_LABEL.get_rect()
LIVES_LABEL_RECT.center = WIDTH - WIDTH // 10, HEIGHT // 8
LEVEL_LABEL = TEXT_FONT.render(f"LEVEL: {LEVEL}", True, RED)
LEVEL_LABEL_RECT = LEVEL_LABEL.get_rect()
LEVEL_LABEL_RECT.center = WIDTH // 10, HEIGHT // 8

##################################################################################
# classes
class Ship:
    def __init__(self):

class
##################################################################################
# main loop variables
##################################################################################
# main loop
