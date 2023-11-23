import pygame
import os
pygame.init()
##################################################################################
# variables
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
LEVEL=1
LIVES=5
##################################################################################
# game window and metadata initialisation
GAME_SCREEN=pygame.display.set_mode((0,0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
pygame.display.set_caption("S P A C E I N V A D E R S")
WIDTH,HEIGHT=pygame.display.get_window_size()
TITLE_FONT=pygame.font.SysFont("comicsans",WIDTH//14)  # comicsans = font
SUBTITLE_FONT=pygame.font.SysFont("comicsans",WIDTH//20)  # comicsans = font
TEXT_FONT=pygame.font.SysFont("comicsans",WIDTH//40)  # comicsans = font
# game metadata initialisation
##################################################################################

# Menu scene

MENU_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("Images","MENU_BACKGROUND.png")),
                                       (WIDTH,HEIGHT))

MENU_TEXT=TITLE_FONT.render("SPACE INVADERS",True,WHITE)
MENU_TEXT_RECT=MENU_TEXT.get_rect()
MENU_TEXT_RECT.center=WIDTH//2,HEIGHT//10

MENU_TEXT2=SUBTITLE_FONT.render("CLICK TO START",True,WHITE)
MENU_TEXT2_RECT=MENU_TEXT2.get_rect()
MENU_TEXT2_RECT.center=WIDTH//2,HEIGHT//2

# GameOver scene

GAMEOVER_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("Images","GAMEOVER_BACKGROUND.png")),
                                           (WIDTH,HEIGHT))

# Playing scene

PLAYING_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("Images","PLAYING_BACKGROUND.png")),
                                          (WIDTH,HEIGHT))

position=0
def background_moving():  # https://www.youtube.com/watch ?v=clm7kv88XPs
    global position
    GAME_SCREEN.fill(BLACK)

    GAME_SCREEN.blit(PLAYING_BACKGROUND,(0,position))
    GAME_SCREEN.blit(PLAYING_BACKGROUND,(0,position-PLAYING_BACKGROUND.get_height()))

    position+=0.3
    if abs(position)>PLAYING_BACKGROUND.get_height():
        position=0
LIVES_LABEL=TEXT_FONT.render(f"LIVES: {LIVES}",True,RED)
LIVES_LABEL_RECT=LIVES_LABEL.get_rect()
LIVES_LABEL_RECT.center=WIDTH-WIDTH//10,HEIGHT//8
LEVEL_LABEL=TEXT_FONT.render(f"LEVEL: {LEVEL}",True,RED)
LEVEL_LABEL_RECT=LEVEL_LABEL.get_rect()
LEVEL_LABEL_RECT.center=WIDTH//10,HEIGHT//8

##################################################################################
# classes and functions
# PLAYER IMAGES
SPACESHIP_GREEN=pygame.transform.scale(pygame.image.load(os.path.join("Images","SpaceShipGreen.png")),
                                       (WIDTH//10,HEIGHT//6))

LASER_GREEN=pygame.transform.scale(pygame.image.load(os.path.join("Images","LaserGreen.png")),
                                   (WIDTH//10,HEIGHT//20))
##################################################################################
# Player & Bullet
class Lasers:
    def __init__(self,x,y,laser_img):
        self.x=x
        self.y=y
        self.speed=3
        self.laser_x=7
        self.laser_y=21
        self.laser_img=laser_img
    def laser_move(self):
        self.y-=self.speed
    def draw(self):
        GAME_SCREEN.blit(self.laser_img,(self.x,self.y))
class Ships:

    def __init__(self,x,y,ship_x,ship_y,ship_img):
        self.x=x
        self.y=y
        self.ship_x=ship_x
        self.ship_y=ship_y
        self.speed=WIDTH//100
        self.ship_img=ship_img

        self.lasers=[]
        self.laser_cooldown=500
        self.last_laser_time=0
    def draw(self):
        GAME_SCREEN.blit(self.ship_img,(self.x,self.y))
    def move_left(self):
        self.ship_x-=self.speed
        if self.ship_x<0:
            self.ship_x=0
    def move_right(self):
        self.ship_x+=self.speed
        if self.ship_x>WIDTH-self.ship_x:
            self.ship_x=WIDTH-self.ship_x
    def move_up(self):
        self.ship_y-=self.speed
        if self.ship_y<0:
            self.ship_y=0
    def move_down(self):
        self.ship_y+=self.speed
        if self.ship_y>HEIGHT-self.ship_y:
            self.ship_y=HEIGHT-self.ship_y
    def handle_keys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_SPACE]:
            current_time=pygame.time.get_ticks()
            if current_time-self.last_laser_time>self.laser_cooldown:
                self.shoot()
                self.last_laser_time=current_time
    def shoot(self):
        laser_x=self.ship_x+self.ship_x//2-2
        laser_y=self.ship_y

        laser=Lasers(laser_x,laser_y,LASER_GREEN)
        self.lasers.append(laser)
    def update_bullets(self):
        for laser in self.lasers:
            laser.laser_move()
            if laser.y<0:
                self.lasers.remove(laser)


##################################################################################
# main loop's variables
PLAYER = Player(WIDTH // 2, HEIGHT - WIDTH // 8, SPACESHIP_GREEN, LASER_GREEN)
MAIN = False
MENU = False
PLAYING = False
GAMEOVER = False
# main loop
if __name__ == "__main__":
    while not MAIN:
        for main_event in pygame.event.get():
            if main_event.type == pygame.KEYUP:
                if main_event.key == pygame.K_ESCAPE:
                    exit()

        MENU=True
        while MENU:
            for menu_event in pygame.event.get():
                if menu_event.type==pygame.KEYUP:
                    if menu_event.key==pygame.K_ESCAPE:
                        exit()

                if menu_event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_TEXT2_RECT.collidepoint(menu_event.pos):
                        MENU = False

            GAME_SCREEN.blit(MENU_BACKGROUND, (0, 0))
            GAME_SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
            GAME_SCREEN.blit(MENU_TEXT2, MENU_TEXT2_RECT)
            pygame.display.update()

        if not MENU:
            PLAYING=True

        while PLAYING:
            for playing_event in pygame.event.get():
                if playing_event.type==pygame.KEYUP:
                    if playing_event.key==pygame.K_ESCAPE:
                        exit()