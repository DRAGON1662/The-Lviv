import  pygame,math
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_set, screen, main_ch):
        super().__init__()
        self.screen = screen
        self.game_set = game_set
        self.rect = pygame.Rect(0, 0, game_set.bullet_width, game_set.bullet_height)

        self.rect.centerx = main_ch.rect.centerx
        self.rect.top = main_ch.rect.top

        '''self.y =float(self.rect.y)'''

        self.way = self.rect.x

        self.color = game_set.bullet_color
        self.speed = game_set.bullet_speed

    '''def rotate_bullet(self,x, y, mouse_pos, image):
        # Calculate x and y distances to the mouse pos.
        run, rise = (mouse_pos[0] - x, mouse_pos[1] - y)
        # Pass the rise and run to atan2 (in this order)
        # and convert the angle to degrees.
        angle = math.degrees(math.atan2(rise, run))
        # Rotate the image (use the negative angle).
        rotimage = pygame.transform.rotate(image, -angle)
        rect = rotimage.get_rect(center=(x, y))
        return rotimage, rect
    '''
    def update(self):

        self.way -= self.speed
        self.rect.x = self.way

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)