import pygame,sys
from bullet import Bullet

def check_events(main_ch, game_set, screen, bullets, teleport):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, main_ch, game_set, screen, bullets, teleport)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, main_ch, teleport)

def check_keyup_events(event, main_ch, teleport):
    # Sprint check button
    if event.key == pygame.K_LSHIFT:
        main_ch.sprint = False

    # Right button main_char check
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        main_ch.moving_right = False
        main_ch.image = main_ch.image_right

    # Left button main_char check
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        main_ch.moving_left = False
        main_ch.image = main_ch.image_left

    # Up button main_char check
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        main_ch.moving_up = False
        main_ch.image = main_ch.image_up

    # Down(bottom) button main_char check
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        main_ch.moving_down = False
        main_ch.image = main_ch.image_bottom

    if event.key == pygame.K_e:
        teleport.location_mag_b_1 = False
        teleport.e_img_cur = teleport.e_img_1

def check_keydown_events(event, main_ch, game_set, screen, bullets, teleport):
    # Quit game with ESC
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    # Sprint check button
    if event.key == pygame.K_LSHIFT:
        main_ch.sprint = True

    # Left button main_char check
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        main_ch.moving_left = True

    # Right button main_char check
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        main_ch.moving_right = True

    # Up button main_char check
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        main_ch.moving_up = True

    # Down(bottom) button main_char check
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        main_ch.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullets(main_ch, game_set, screen, bullets)

    if event.key == pygame.K_DOWN or event.key == pygame.K_e:
        teleport.location_mag_b_1 = True
        teleport.e_img_cur = teleport.e_img_2

def update_screen(game_set,screen,main_ch,bullets,teleport,loot):
    pygame.display.flip()
    screen.fill(game_set.bg_color)

    screen.blit(game_set.bg_image_third, (game_set.cam_x,game_set.cam_y))

    main_ch.update()
    main_ch.blitme()

    teleport.update()
    teleport.blitme()

    loot.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(main_ch, game_set, screen, bullets):
    #if len(bullets) <= game_set.bullet_allowed:
    new_bullet = Bullet(game_set, screen, main_ch)
    bullets.add(new_bullet)