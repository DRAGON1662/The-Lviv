import pygame

class Loot():
    def __init__(self,screen,game_set):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.game_set = game_set

        # Fort21 pistol
        self.fort21_img = pygame.image.load("images/loot/guns/starter/fort_21.png")
        self.fort21_rect = self.fort21_img.get_rect()
        self.fort21_rect.centerx = 1520
        self.fort21_rect.centery = 620


    def blitme(self):
        self.game_set.bg_image_third.blit(self.fort21_img,self.fort21_rect)

