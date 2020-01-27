import pygame
class Settings():
    def __init__(self):
        # Game properties
        self.screen_width = 1280
        self.screen_height = 974
        self.fps = 60
        self.title = "The Lviv"
        self.bg_color = (0,0,0)

        # Background image
        self.bg_image_third = pygame.image.load("images/zelena20x2.png")

        # Main charecter
        self.main_speed = 3
        self.sprinting_speed = 5
        self.main_const_speed = 3

        # Camera
        self.cam_x = -112
        self.cam_y = -1742

        # Bullet
        self.bullet_width = 12
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 10
        self.bullet_allowed = 3





