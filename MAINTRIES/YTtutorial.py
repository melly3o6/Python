import pygame
# import sys
import os

#########################################################################################


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Images", "SpaceShipGreen.png")),
                                         (WIDTH // 10, HEIGHT // 6))
        self.rect = self.image.get_rect(midbottom=pos)
#########################################################################################


class Game:
    def __init__(self):
        player_sprite = Player((WIDTH // 2, HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(GAME_SCREEN)
        # update all sprite groups
        # draw all sprite groups

#########################################################################################


position = 0


def background_moving():

    global position
    GAME_SCREEN.fill(BLACK)

    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position))
    GAME_SCREEN.blit(PLAYING_BACKGROUND, (0, position-PLAYING_BACKGROUND.get_height()))

    position += 0.3
    if abs(position) > PLAYING_BACKGROUND.get_height():
        position = 0


#########################################################################################

if __name__ == '__main__':

    pygame.init()
#########################################################################################
    BLACK = (0, 0, 0)
#########################################################################################
    GAME_SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    pygame.display.set_caption('S P A C E I N V A D E R S')
    WIDTH, HEIGHT = pygame.display.get_window_size()
#########################################################################################
    PLAYING_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "PLAYING_BACKGROUND.png")),
                                                (WIDTH, HEIGHT))
#########################################################################################

    clock = pygame.time.Clock()
    game = Game()
#########################################################################################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exit()

        background_moving()

        pygame.display.update()
        game.run()
        clock.tick(60)
#########################################################################################
# https://www.youtube.com/watch?v=o-6pADy5Mdg
