import pygame
class Main_character():
    def __init__(self,game_settings, screen, animation):

        self.anim = animation
        self.screen = screen
        self.game_set = game_settings

        self.image = pygame.image.load("images/animation/main_char/right/D_1.png")

        self.image_right = pygame.image.load("images/animation/main_char/right/D_1.png")
        self.image_left = pygame.image.load("images/animation/main_char/left/A_1.png")
        self.image_up = pygame.image.load("images/animation/main_char/up/W_1.png")
        self.image_bottom = pygame.image.load("images/animation/main_char/bottom/S_1.png")

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.sprint = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.first_room = False
        self.main_ch_rect = pygame.Rect(self.rect.x, 2188, 40, 85)

        self.obstacle = pygame.draw.rect(game_settings.bg_image_third, pygame.Color(0, 0, 0, 0), (0, 2170, 3450, 2))

        #rooms
        self.ob_down = pygame.draw.rect(game_settings.bg_image_third, (0, 0, 0), (1150, 818, 800, 2))
        self.ob_up = pygame.draw.rect(game_settings.bg_image_third, (0, 0, 0), (1150, 608, 800, 2))

        #room1
        self.ob1_right = pygame.draw.rect(game_settings.bg_image_third, (0, 255, 0), (1350, 480, 0, 330))
        self.ob1_left = pygame.draw.rect(game_settings.bg_image_third, (0, 255, 0), (1150, 480, 0, 330))

        #room2
        self.ob2_right = pygame.draw.rect(game_settings.bg_image_third, (0, 0, 0), (1740, 480, 0, 330))
        self.ob2_left = pygame.draw.rect(game_settings.bg_image_third, (0, 0, 0), (1435, 480, 0, 330))



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        # Animate player movement
        if (self.moving_down or self.moving_up) and self.moving_right:
            self.image = self.anim.main_ch_right()
        elif (self.moving_down or self.moving_up) and self.moving_left:
            self.image = self.anim.main_ch_left()
        elif self.moving_down and self.moving_right != True and self.moving_left != True:
            self.image = self.anim.main_ch_bottom()
        elif self.moving_up and self.moving_right != True and self.moving_left != True:
            self.image = self.anim.main_ch_up()
        elif self.moving_left and self.moving_up != True and self.moving_down != True and self.moving_right != True:
            self.image = self.anim.main_ch_left()
        elif self.moving_right and self.moving_up != True and self.moving_down != True and self.moving_left != True:
            self.image = self.anim.main_ch_right()

        # When player runs
        if self.sprint:
            self.game_set.main_speed = self.game_set.sprinting_speed
        else:
            self.game_set.main_speed = self.game_set.main_const_speed

        # When player goes right
        if self.main_ch_rect.colliderect(self.ob1_right) or self.main_ch_rect.colliderect(self.ob2_right):
            pass
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            # Stopping our camera (when player comes to map edge)
            if self.game_set.cam_x < -2187:
                self.game_set.cam_x = -2187
                self.rect.centerx += self.game_set.main_speed
                self.main_ch_rect.x += self.game_set.main_speed

            # If our player is not in the center of the screen, we move only player
            elif self.rect.centerx != self.screen_rect.centerx:
                self.rect.centerx += self.game_set.main_speed
                self.main_ch_rect.x += self.game_set.main_speed
            # If our player is in the center of the screen, we move only camera
            elif self.rect.centerx == self.screen_rect.centerx:
                self.game_set.cam_x -= self.game_set.main_speed
                self.main_ch_rect.x += self.game_set.main_speed

        # When player goes left
        if self.main_ch_rect.colliderect(self.ob1_left) or self.main_ch_rect.colliderect(self.ob2_left):
            pass
        elif self.moving_left and self.rect.left >= self.screen_rect.left:
             if self.game_set.cam_x > 0:
                 self.game_set.cam_x = 0
                 self.rect.centerx -= self.game_set.main_speed
                 self.main_ch_rect.x -= self.game_set.main_speed
             elif self.rect.centerx != self.screen_rect.centerx:
                 self.rect.centerx -= self.game_set.main_speed
                 self.main_ch_rect.x -= self.game_set.main_speed
             elif self.rect.centerx == self.screen_rect.centerx:
                 self.game_set.cam_x += self.game_set.main_speed
                 self.main_ch_rect.x -= self.game_set.main_speed

        # When player goes upd
        if self.main_ch_rect.colliderect(self.obstacle) or self.main_ch_rect.colliderect(self.ob_up):
            pass
        #and self.main_ch_rect.y > self.game_set.obstacle.y
        elif self.moving_up and self.rect.top > self.screen_rect.top : #and self.game_set.cam_y < -1700
            self.game_set.cam_y += self.game_set.main_speed
            self.main_ch_rect.y -= self.game_set.main_speed


        # When player goes down
        if self.main_ch_rect.colliderect(self.ob_down):
            pass
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.game_set.cam_y -= self.game_set.main_speed
            self.main_ch_rect.y += self.game_set.main_speed















