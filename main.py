import pygame
import math
import random
import time

pygame.init()


class PlayerRacket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.test_image = pygame.image.load("images/tennis_racket.png").convert_alpha()
        self.x = 250
        self.y = 720

        self.size = self.test_image.get_size()

        # create an image half bigger than self.image
        self.image = pygame.transform.scale(self.test_image, (int(self.size[0] * 0.5), int(self.size[1] * 0.5)))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.mask_image = pygame.mask.from_surface(self.image)
        self.mask = pygame.mask.from_surface(self.image)

        self.hit_effect = pygame.mixer.Sound("music_and_sounds/player_hit_sound.MP3")


    def move_racket(self, x):
        self.rect.center = (x, self.y)

        self.mask = pygame.mask.from_surface(self.image)
        
class TennisBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/tennis_ball.png").convert_alpha()
        self.original_image = self.image

        self.image_mask = pygame.mask.from_surface(self.image)
        self.image_of_mask = self.image_mask.to_surface()

        self.image_of_new_mask = self.image_of_mask

        self.original_mask_image = self.image_of_mask

        self.movement_speed = 7

        #self note: original x and y values are (197, 12)
        self.x = 250
        self.y = 12

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

        #declaration of variables in order to calculate the scale of the tennis ball moving around the page
        self.minimum_y = 12
        self.maximum_y = 720
        self.maximum_scale = 2
        self.minimum_scale = 0.5
        self.default_scale = 1.0
    
    def move_forward(self, ang_fact):
        self.y = self.y + self.movement_speed
        angle = ang_fact[0] + 4

        factor = ang_fact[1] + 0.015
        tennis_ball.update_scale(angle)

        return (angle,factor)
    
    def move_backward(self, ang_fact):
        #moving backward stuff
        self.target_x_back = 250
        self.target_y_back = 12
        angle_back = math.atan2(self.target_y_back - self.y, self.target_x_back - self.x)

        self.dx_back = math.cos(angle_back) * self.movement_speed
        self.dy_back = math.sin(angle_back) * self.movement_speed

        self.x += self.dx_back
        self.y += self.dy_back

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        angle = ang_fact[0] + 4

        factor = ang_fact[1] - 0.016 
        
        tennis_ball.update_scale(angle)
        return((angle, factor))

    
    def move_angle_left(self, ang_fact):
        #angle left stuff
        self.target_x_1 = 25
        self.target_y_1 = 720
        angle_1 = math.atan2(self.target_y_1 - self.y, self.target_x_1 - self.x)

        self.dx_1 = math.cos(angle_1) * self.movement_speed
        self.dy_1 = math.sin(angle_1) * self.movement_speed
        
        self.x = self.x + int(self.dx_1)
        self.y = self.y + int(self.dy_1)

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        angle = ang_fact[0] + 4

        factor = ang_fact[1] + 0.015
        tennis_ball.update_scale(angle)
        
        return (angle,factor)

    def move_angle_right(self, ang_fact):
        #angle right stuff
        self.target_x_2 = 475
        self.target_y_2 = 720
        angle_2 = math.atan2(self.target_y_2 - self.y, self.target_x_2 - self.x)

        self.dx_2 = math.cos(angle_2) * self.movement_speed
        self.dy_2 = math.sin(angle_2) * self.movement_speed

        self.x = self.x + int(self.dx_2)
        self.y = self.y + int(self.dy_2)

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        angle = ang_fact[0] + 4

        factor = ang_fact[1] + 0.015
        tennis_ball.update_scale(angle)
        
        return (angle,factor)
    
    def update_scale(self, angle):
        progress_on_window = (self.y - self.minimum_y) / (self.maximum_y - self.minimum_y)
        self.scale = (self.minimum_scale + progress_on_window)  * (self.maximum_scale - self.minimum_scale)

        new_width = int(self.original_image.get_width() * self.scale)
        new_height = int(self.original_image.get_height() * self.scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image)
        
        rotated_image = pygame.transform.rotate(self.image, angle)

        self.image = rotated_image

        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image)
    
class CatOpponent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/meme_cat.png").convert_alpha()

        self.x = 250
        self.y = 55

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)
    
    def move(self):
        self.x = cat_racket.x - 50
        self.update()
    
    def update(self):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)

class CatRacket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/final_cat_racket.png").convert_alpha()

        self.x = 260
        self.y = 55

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.hit_sound = pygame.mixer.Sound("music_and_sounds/cat_hit_sound.mp3")
    
    def move(self):
        self.x = tennis_ball.x
        self.update()
    
    def update(self):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)

class RedCircleTest(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 10
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.color = color

        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, color):
        pos = pygame.mouse.get_pos()
        self.rect.center = (pos)
        self.image.fill(color)

class CatCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/cat_cent_image.png").convert_alpha()

        self.mask = pygame.mask.from_surface(self.image)
        self.x = random.randint(20,450)
        self.y = 0
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)
        
    def move_down(self):
        self.y = self.y + 2
        self.update()
    
    def collision_collect(self):
        self.kill()
        
    
    def restart_from_position(self):
        self.x = random.randint(20, 450)
        self.y = 0
    
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    



def starting_menu(play_again, score, total_score, total_coins):
    background = pygame.image.load("menu_screen/background_image.png")

    size = 0 

    screen.blit(background, (0,0))

    pos = pygame.mouse.get_pos()

    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    again_button = pygame.image.load("menu_screen/play_again_button.png").convert_alpha()
    start_button = pygame.image.load("menu_screen/start_button.png").convert_alpha()
    if play_again:
        draw_text("Womp Womp, You Missed the Ball :(", smaller_anime_font, (235,166,64), 100, 300)
        draw_text("the Ball :(", smaller_anime_font, (235,166,64), 215, 320)
        draw_text(score, smaller_anime_font, (235,166,64), 200, 350)
        draw_text(total_score, smaller_anime_font, (235, 166, 64), 200, 375)
        draw_text(total_coins, smaller_anime_font, (235, 166, 64), 200, 400)
    
        screen.blit(again_button, (175,200))
    else:
        screen.blit(start_button, (175,200))

    start_button_rect = start_button.get_rect(topleft = (175, 200))
    again_button_rect = again_button.get_rect(topleft = (175, 200))
    
    if start_button_rect.collidepoint(pos) or again_button_rect.collidepoint(pos):
        circle_test.update("green")
        if click:
            return False

    pygame.display.update()

    return True

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)

    screen.blit(img, (x,y))
    


# Set up screens
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_racket = PlayerRacket()
tennis_ball = TennisBall()
meme_cat = CatOpponent()
cat_racket = CatRacket()
new_coin = CatCoin()

col = "red"
circle_test = RedCircleTest(col)

player_racket_group = pygame.sprite.Group()
tennis_ball_group = pygame.sprite.Group()
meme_cat_group = pygame.sprite.Group()
cat_racket_group = pygame.sprite.Group()
cat_coin_group = pygame.sprite.Group()

circle_test_group = pygame.sprite.Group()


player_racket_group.add(player_racket)
tennis_ball_group.add(tennis_ball)
meme_cat_group.add(meme_cat)
cat_racket_group.add(cat_racket)
#cat_coin_group.add(cat_coin)

circle_test_group.add(circle_test)

clock = pygame.time.Clock()
run = True
angle = 0
angle_factor = (0, 1)  #angle stored in [0] and scale factor stored in [1]
forward = False
backward = True
factor = 20
game_over = False

pos_assign_num = 0
angle_left = False
angle_forward = False
angle_right = False

startup_menu = True

only_once = False

send_coin = False

collision_trigger_down = True

text_font = pygame.font.SysFont(None, 30)
anime_font = pygame.font.SysFont('FOT-Yuruka Std', 30)
smaller_anime_font = pygame.font.SysFont('FOT-Yuruka Std', 15)

score = 0
total_score = 0

cat_coins = 0
total_cat_coins = 0

play_again_que = False

pygame.mixer.music.load("music_and_sounds/wii_music.mp3")


click = False

score_image = pygame.image.load("images/score_logo.png")
coins_image = pygame.image.load("images/coins_logo.png")
background_field = pygame.image.load("images/background_field.png")

saved_score_path = ("save_data/score.txt")
with open(saved_score_path, 'r') as file_obj:
    first_char = file_obj.read(1)

    if not first_char:
        write_obj = open(saved_score_path, "w")
        write_obj.write("0")
        write_obj.close()
    else:
        read_obj = open(saved_score_path, 'r')
        total_score = read_obj.read()
        total_score = int(total_score)

while run:
    score_text = str(score)
    cat_coins_text = str(cat_coins)

    clock.tick(60)
    
    while startup_menu:
        clock.tick(60)
        pygame.display.update()

        screen.fill("blue")

        status = starting_menu(play_again_que, str(score), str(total_score), str(total_cat_coins))
        startup_menu = status
        circle_test_group.draw(screen)
        circle_test_group.update(col)

        if startup_menu:
            pygame.mixer.music.play(loops=-1)

    screen.blit(background_field, (0, 0))
    
    screen.blit(score_image, (-75,100))
    draw_text(score_text , anime_font, (235,166,64), 70, 200)

    screen.blit(coins_image, (265, 100))
    draw_text(cat_coins_text, anime_font, (235, 166, 64), 400, 200)

    pos = pygame.mouse.get_pos()

    #move tennis racket
    player_racket.move_racket(pos[0])

    player_racket_rect = player_racket.image.get_rect(center=(player_racket.x, player_racket.y))

    tennis_ball_rect = tennis_ball.image.get_rect(center=(tennis_ball.x, tennis_ball.y))

    #draw images
    player_racket_group.draw(screen)
   
    tennis_ball_group.draw(screen)

    meme_cat_group.draw(screen)

    cat_racket_group.draw(screen)

    cat_coin_group.draw(screen)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while tennis_ball.y <= 12:
        if pos_assign_num == 1:
            angle_left = True
            factor = 1
            break

        elif pos_assign_num == 2:
            angle_forward = True
            factor = 1
            break

        elif pos_assign_num == 3:
            angle_right = True
            factor = 1
            break

        else:
            factor = 1
            pos_assign_num = random.randint(1,3)
            pygame.mixer.find_channel().play(cat_racket.hit_sound)
        
        
    if game_over:
        forward = False
        backward = False
        play_again_que = True

        total_score += score
        total_cat_coins += cat_coins

        pygame.mixer.music.stop()
        startup_menu = True
        click = False

        new_coin.y = 0
        send_coin = False
        
        for k in cat_coin_group:
            k.kill()

        write_obj = open(saved_score_path, "w")
        write_obj.write(str(total_score))
        write_obj.close() 

        while startup_menu:
            clock.tick(60)
            text_temp = "Final score: " + str(score)
            text_total = "Total score: " + str(total_score)
            cointxt_total = "Total cat coins: " + str(total_cat_coins)

            status = starting_menu(play_again_que, text_temp, text_total, cointxt_total)
            startup_menu = status

            screen.fill("blue")
        
        #The following code should be triggered when the restart button is pressed (i hope D:)
        game_over = False

        tennis_ball.x = 250
        tennis_ball.y = 12

        meme_cat.x = 250
        meme_cat.y = 55

        cat_racket.x = 260
        cat_racket.y = 55

        score = 0
        cat_coins = 0

        tennis_ball.movement_speed = 7

        pygame.mixer.music.play()

    elif angle_left:
        
        angle_factor = tennis_ball.move_angle_left((angle_factor))
        cat_racket.move()
        meme_cat.move()

        played_sound_already = False

    elif angle_forward:
        
        angle_factor = tennis_ball.move_forward((angle_factor))

        cat_racket.move()
        meme_cat.move()

        played_sound_already = False
    elif angle_right:
        

        angle_factor = tennis_ball.move_angle_right((angle_factor))

        cat_racket.move()
        meme_cat.move()

        played_sound_already = False

    elif not game_over:
        
        angle_factor = tennis_ball.move_backward((angle_factor))

        cat_racket.move()
        meme_cat.move()

        pos_assign_num = 0
    
    if pygame.sprite.spritecollide(player_racket, tennis_ball_group, False):
        col = "blue"
        if pygame.sprite.spritecollide(player_racket, tennis_ball_group, False, pygame.sprite.collide_mask) and (not game_over):
            angle_left = False
            angle_forward = False
            angle_right = False

            col = "green"

            if(tennis_ball.y > 576):
                tennis_ball.y = 565
                if not played_sound_already:
                    pygame.mixer.find_channel().play(player_racket.hit_effect)
                    played_sound_already = True
                    score += 1
                else:
                    pass
            else:
                if not played_sound_already:
                    pygame.mixer.find_channel().play(player_racket.hit_effect)
                    played_sound_already = True
                    score += 1

            game_over = False

            if score % 5 == 0:
                tennis_ball.movement_speed = tennis_ball.movement_speed + 3

                send_coin = True

                if len(cat_coin_group.sprites()) <= 0:
                    new_coin = CatCoin()
                    cat_coin_group.add(new_coin)       
        else:
            col = "red"
    
    
    #no collision with racket
    if(tennis_ball.y >= 720):
        played_sound_already = False
        game_over = True
    
    if send_coin:
        for i in cat_coin_group:
            (cat_coin_group.sprites()[0]).move_down()
    
    if pygame.sprite.spritecollide(player_racket, cat_coin_group, False):
        if pygame.sprite.spritecollide(player_racket, cat_coin_group, False, pygame.sprite.collide_mask):
            for j in cat_coin_group:
                    if j.y >= 500:
                        (cat_coin_group.sprites()[0]).collision_collect()
            send_coin = False
            cat_coins = cat_coins + 1

    width = meme_cat.image.get_width()
    height = meme_cat.image.get_height()

    circle_test_group.update(col)
    print(cat_coin_group)
    
    """
    test case statements:
    print("Tennis ball at ", tennis_ball.x, ", ", tennis_ball.y )
    print("Game over is ", game_over)
    print("Forward is ", forward)
    print("Backward is ", backward)
    print(" ")
    print("Angle, factor: ", angle_factor[0], " ", angle_factor[1])
    print("Mouse pos", pos)
    print("Played sound already is ", played_sound_already)
    """
    
    pygame.display.flip()
    pygame.display.update()


pygame.quit()