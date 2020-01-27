import pygame
from settings import Settings
from main_character import Main_character
import game_functions as g_f
from animation import Animation
from pygame.sprite import Group
from teleport import Teleport
from loot import Loot
def init_game():
    pygame.init()
    clock = pygame.time.Clock()
    game_set = Settings()

    animation = Animation()
    bullets = Group()

    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    main_ch = Main_character(game_set,screen,animation)
    teleport = Teleport(screen,main_ch,game_set)
    loot = Loot(screen,game_set)
    while True:
        pygame.display.set_caption(game_set.title + " FPS: " + str(round(clock.get_fps(),1)))

        clock.tick(game_set.fps)
        g_f.update_bullets(bullets)
        g_f.check_events(main_ch, game_set, screen, bullets,teleport)
        g_f.update_screen(game_set,screen,main_ch,bullets,teleport,loot)
        mousex,mousey = pygame.mouse.get_pos()
        print(mousex,mousey)
        #print(game_set.cam_x,game_set.cam_y)
        obstacle = pygame.draw.rect(game_set.bg_image_third, (255, 0, 0), (0, 2160, 3450, 2))
        print(main_ch.main_ch_rect.y, main_ch.main_ch_rect.x)
        #print(main_ch.rect.x, obstacle.x, obstacle.y, main_ch.rect.y)
        # print(main_ch.personag.y, obstacle.y)
        # if main_ch.personag.y > obstacle.y:
        #     print("Yes")
        #if main_ch.main_ch_rect.colliderect(obstacle):
        #     game_set.cam_y -= game_set.main_speed
        #print(main_ch.rect.x)

init_game()
