import pygame
class Animation():
    def __init__(self):
        self.main_current_img = None
        self.main_current_numb = 1

        # Anim images right (main char)
        self.m_ch_1_r = pygame.image.load("images/animation/main_char/right/D_1.png")
        self.m_ch_2_r = pygame.image.load("images/animation/main_char/right/D_2.png")
        self.m_ch_3_r = pygame.image.load("images/animation/main_char/right/D_3.png")
        self.m_ch_4_r = pygame.image.load("images/animation/main_char/right/D_4.png")
        self.m_ch_5_r = pygame.image.load("images/animation/main_char/right/D_5.png")
        self.m_ch_6_r = pygame.image.load("images/animation/main_char/right/D_6.png")
        self.m_ch_7_r = pygame.image.load("images/animation/main_char/right/D_7.png")
        self.m_ch_8_r = pygame.image.load("images/animation/main_char/right/D_8.png")
        self.m_ch_9_r = pygame.image.load("images/animation/main_char/right/D_9.png")
        self.m_ch_10_r = pygame.image.load("images/animation/main_char/right/D_10.png")

        # Anim images left (main char)
        self.m_ch_1_l = pygame.image.load("images/animation/main_char/left/A_1.png")
        self.m_ch_2_l = pygame.image.load("images/animation/main_char/left/A_2.png")
        self.m_ch_3_l = pygame.image.load("images/animation/main_char/left/A_3.png")
        self.m_ch_4_l = pygame.image.load("images/animation/main_char/left/A_4.png")
        self.m_ch_5_l = pygame.image.load("images/animation/main_char/left/A_5.png")
        self.m_ch_6_l = pygame.image.load("images/animation/main_char/left/A_6.png")
        self.m_ch_7_l = pygame.image.load("images/animation/main_char/left/A_7.png")
        self.m_ch_8_l = pygame.image.load("images/animation/main_char/left/A_8.png")
        self.m_ch_9_l = pygame.image.load("images/animation/main_char/left/A_9.png")
        self.m_ch_10_l = pygame.image.load("images/animation/main_char/left/A_10.png")

        # Anim images up (main char)
        self.m_ch_1_u = pygame.image.load("images/animation/main_char/up/W_1.png")
        self.m_ch_2_u = pygame.image.load("images/animation/main_char/up/W_2.png")
        self.m_ch_3_u = pygame.image.load("images/animation/main_char/up/W_3.png")
        self.m_ch_4_u = pygame.image.load("images/animation/main_char/up/W_4.png")
        self.m_ch_5_u = pygame.image.load("images/animation/main_char/up/W_5.png")
        self.m_ch_6_u = pygame.image.load("images/animation/main_char/up/W_6.png")
        self.m_ch_7_u = pygame.image.load("images/animation/main_char/up/W_7.png")
        self.m_ch_8_u = pygame.image.load("images/animation/main_char/up/W_8.png")
        self.m_ch_9_u = pygame.image.load("images/animation/main_char/up/W_9.png")
        self.m_ch_10_u = pygame.image.load("images/animation/main_char/up/W_10.png")
        self.m_ch_11_u = pygame.image.load("images/animation/main_char/up/W_11.png")

        # Anim images bottom (main char)
        self.m_ch_1_b = pygame.image.load("images/animation/main_char/bottom/S_1.png")
        self.m_ch_2_b = pygame.image.load("images/animation/main_char/bottom/S_2.png")
        self.m_ch_3_b = pygame.image.load("images/animation/main_char/bottom/S_3.png")
        self.m_ch_4_b = pygame.image.load("images/animation/main_char/bottom/S_4.png")
        self.m_ch_5_b = pygame.image.load("images/animation/main_char/bottom/S_5.png")
        self.m_ch_6_b = pygame.image.load("images/animation/main_char/bottom/S_6.png")
        self.m_ch_7_b = pygame.image.load("images/animation/main_char/bottom/S_7.png")
        self.m_ch_8_b = pygame.image.load("images/animation/main_char/bottom/S_8.png")
        self.m_ch_9_b = pygame.image.load("images/animation/main_char/bottom/S_9.png")
        self.m_ch_10_b = pygame.image.load("images/animation/main_char/bottom/S_10.png")
        self.m_ch_11_b = pygame.image.load("images/animation/main_char/bottom/S_11.png")



    def main_ch_left(self):
        if self.main_current_numb == 1:
            self.main_current_img = self.m_ch_1_l
        if self.main_current_numb == 2:
            self.main_current_img = self.m_ch_2_l
        if self.main_current_numb == 3:
            self.main_current_img = self.m_ch_3_l
        if self.main_current_numb == 4:
            self.main_current_img = self.m_ch_4_l
        if self.main_current_numb == 5:
            self.main_current_img = self.m_ch_5_l
        if self.main_current_numb == 6:
            self.main_current_img = self.m_ch_6_l
        if self.main_current_numb == 7:
            self.main_current_img = self.m_ch_7_l
        if self.main_current_numb == 8:
            self.main_current_img = self.m_ch_8_l
        if self.main_current_numb == 9:
            self.main_current_img = self.m_ch_9_l
        if self.main_current_numb == 10:
            self.main_current_img = self.m_ch_10_l
        if self.main_current_numb == 10:
            self.main_current_numb = 1
        else:
            self.main_current_numb += 1
        return self.main_current_img


    def main_ch_right(self):
        if self.main_current_numb == 1:
            self.main_current_img = self.m_ch_1_r
        if self.main_current_numb == 2:
            self.main_current_img = self.m_ch_2_r
        if self.main_current_numb == 3:
            self.main_current_img = self.m_ch_3_r
        if self.main_current_numb == 4:
            self.main_current_img = self.m_ch_4_r
        if self.main_current_numb == 5:
            self.main_current_img = self.m_ch_5_r
        if self.main_current_numb == 6:
            self.main_current_img = self.m_ch_6_r
        if self.main_current_numb == 7:
            self.main_current_img = self.m_ch_7_r
        if self.main_current_numb == 8:
            self.main_current_img = self.m_ch_8_r
        if self.main_current_numb == 9:
            self.main_current_img = self.m_ch_9_r
        if self.main_current_numb == 10:
            self.main_current_img = self.m_ch_10_r
        if self.main_current_numb == 10:
            self.main_current_numb = 1
        else:
            self.main_current_numb += 1
        return self.main_current_img

    def main_ch_up(self):
        if self.main_current_numb == 1:
            self.main_current_img = self.m_ch_1_u
        if self.main_current_numb == 2:
            self.main_current_img = self.m_ch_2_u
        if self.main_current_numb == 3:
            self.main_current_img = self.m_ch_3_u
        if self.main_current_numb == 4:
            self.main_current_img = self.m_ch_4_u
        if self.main_current_numb == 5:
            self.main_current_img = self.m_ch_5_u
        if self.main_current_numb == 6:
            self.main_current_img = self.m_ch_6_u
        if self.main_current_numb == 7:
            self.main_current_img = self.m_ch_7_u
        if self.main_current_numb == 8:
            self.main_current_img = self.m_ch_8_u
        if self.main_current_numb == 9:
            self.main_current_img = self.m_ch_9_u
        if self.main_current_numb == 10:
            self.main_current_img = self.m_ch_10_u
        if self.main_current_numb == 10:
            self.main_current_numb = 1
        else:
            self.main_current_numb += 1
        return self.main_current_img

    def main_ch_bottom(self):
        if self.main_current_numb == 1:
            self.main_current_img = self.m_ch_1_b
        if self.main_current_numb == 2:
            self.main_current_img = self.m_ch_2_b
        if self.main_current_numb == 3:
            self.main_current_img = self.m_ch_3_b
        if self.main_current_numb == 4:
            self.main_current_img = self.m_ch_4_b
        if self.main_current_numb == 5:
            self.main_current_img = self.m_ch_5_b
        if self.main_current_numb == 6:
            self.main_current_img = self.m_ch_6_b
        if self.main_current_numb == 7:
            self.main_current_img = self.m_ch_7_b
        if self.main_current_numb == 8:
            self.main_current_img = self.m_ch_8_b
        if self.main_current_numb == 9:
            self.main_current_img = self.m_ch_9_b
        if self.main_current_numb == 10:
            self.main_current_img = self.m_ch_10_b
        if self.main_current_numb == 10:
            self.main_current_numb = 1
        else:
            self.main_current_numb += 1
        return self.main_current_img