import pygame,sys
class Teleport():
    def __init__(self,screen,main_ch,game_set):
        self.screen = screen
        self.main_ch = main_ch
        self.game_set = game_set

        self.int_range = 20

        self.display_but_e = False
        self.location_mag_b_1 = False

        # E button
        self.e_img_cur = pygame.image.load("images/buttons/e1.png")

        self.e_img_1 = pygame.image.load("images/buttons/e1.png")
        self.e_img_2 = pygame.image.load("images/buttons/e2.png")

    def update(self):
        # For location teleport
        #print(self.main_ch.main_ch_rect.y, self.game_set.obstacle.y)
        if self.game_set.cam_x in range(-634 - self.int_range, -634 + self.int_range) and self.game_set.cam_y in range(-1716 - self.int_range, -1716 + self.int_range):
            if self.location_mag_b_1:
                self.game_set.cam_y += 1440
                self.main_ch.main_ch_rect.y = 735
                self.main_ch.main_ch_rect.x = 1260
            self.display_but_e = True
        elif self.game_set.cam_x in range(-634 - self.int_range,-634 + self.int_range) and self.game_set.cam_y in range(-1716 + 1440 - self.int_range, -1716 + 1440 + self.int_range):
            if self.location_mag_b_1:
                self.game_set.cam_y -= 1440
                self.main_ch.main_ch_rect.y = 2188
                self.main_ch.main_ch_rect.x = 1144
            self.display_but_e = True
        elif self.game_set.cam_x in range(-984 - self.int_range,-984 + self.int_range) and self.game_set.cam_y in range(-1716 - self.int_range, -1716 + self.int_range):
            if self.location_mag_b_1:
                self.game_set.cam_y += 1440
                self.main_ch.main_ch_rect.y = 735
                self.main_ch.main_ch_rect.x = 1600
            self.display_but_e = True
        elif self.game_set.cam_x in range(-984 - self.int_range,-984 + self.int_range) and self.game_set.cam_y in range(-1716 + 1440 - self.int_range, -1716 + 1440 + self.int_range):
            if self.location_mag_b_1:
                self.game_set.cam_y -= 1440
                self.main_ch.main_ch_rect.y = 2188
                self.main_ch.main_ch_rect.x = 1489
            self.display_but_e = True
        else:
            self.display_but_e = False

        self.location_mag_b_1 = False


    def blitme(self):
        if self.display_but_e:
            self.screen.blit(self.e_img_cur, (self.main_ch.rect.x, self.main_ch.rect.y - 40))





