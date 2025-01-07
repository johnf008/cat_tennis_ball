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

        #self note: original x and y values are (197, 12)
        self.x = 250
        self.y = 12

        #angle left stuff
        self.target_x_1 = 25
        self.target_y_1 = 720
        angle_1 = math.atan2(self.target_y_1 - self.y, self.target_x_1 - self.x)

        print("angle in degrees", int(math.degrees(angle_1)))

        self.dx_1 = math.cos(angle_1) * 7
        self.dy_1 = math.sin(angle_1) * 7

        #angle right stuff
        self.target_x_2 = 475
        self.target_y_2 = 720
        angle_2 = math.atan2(self.target_y_2 - self.y, self.target_x_2 - self.x)

        self.dx_2 = math.cos(angle_2) * 7
        self.dy_2 = math.sin(angle_2) * 7

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
        self.y = self.y + 7
        angle = ang_fact[0] + 4

        factor = ang_fact[1] + 0.015
        tennis_ball.update_scale(angle)

        print("towards")

        return (angle,factor)
    
    def move_backward(self, ang_fact):
        #moving backward stuff
        self.target_x_back = 250
        self.target_y_back = 12
        angle_back = math.atan2(self.target_y_back - self.y, self.target_x_back - self.x)

        self.dx_back = math.cos(angle_back) * 7
        self.dy_back = math.sin(angle_back) * 7

        self.x += self.dx_back
        self.y += self.dy_back

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        angle = ang_fact[0] + 4

        factor = ang_fact[1] - 0.016 
        
        tennis_ball.update_scale(angle)
        return((angle, factor))

    
    def move_angle_left(self, ang_fact):
        self.x = self.x + int(self.dx_1)
        self.y = self.y + int(self.dy_1)

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        angle = ang_fact[0] + 4

        factor = ang_fact[1] + 0.015
        tennis_ball.update_scale(angle)
        
        return (angle,factor)

    def move_angle_right(self, ang_fact):
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

def starting_menu(c):
    screen.fill((0,0,0))

    pos = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 200, 50)

    click = c

    if button_1.collidepoint((pos[0], pos[1])):
        if click:
            return False
    
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(screen, (255, 0, 0), button_1)
    pygame.display.update()
    return True

    


# Set up screens
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_racket = PlayerRacket()
tennis_ball = TennisBall()
meme_cat = CatOpponent()
cat_racket = CatRacket()

col = "red"
circle_test = RedCircleTest(col)

player_racket_group = pygame.sprite.Group()
tennis_ball_group = pygame.sprite.Group()
meme_cat_group = pygame.sprite.Group()
cat_racket_group = pygame.sprite.Group()

circle_test_group = pygame.sprite.Group()


player_racket_group.add(player_racket)
tennis_ball_group.add(tennis_ball)
meme_cat_group.add(meme_cat)
cat_racket_group.add(cat_racket)

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


pygame.mixer.music.load("music_and_sounds/wii_music.mp3")
pygame.mixer.music.play(loops=-1)

click = False

while run:

    clock.tick(60)
    while startup_menu:
        status = starting_menu(click)
        
        startup_menu = status

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

    
    screen.fill("white")

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
    

    circle_test_group.draw(screen)

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

        pygame.mixer.music.stop()
        startup_menu = True
        click = False

        while startup_menu:
            status = starting_menu(click)
            startup_menu = status

            print(status)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

        #The following code should be triggered when the restart button is pressed (i hope D:)
        game_over = False

        tennis_ball.x = 250
        tennis_ball.y = 12

        meme_cat.x = 250
        meme_cat.y = 55

        cat_racket.x = 260
        cat_racket.y = 55

    elif angle_left:
        print("towards")
        
        angle_factor = tennis_ball.move_angle_left((angle_factor))
        cat_racket.move()
        meme_cat.move()

        played_sound_already = False

    elif angle_forward:
        print("towards forward")

        angle_factor = tennis_ball.move_forward((angle_factor))

        cat_racket.move()
        meme_cat.move()

        played_sound_already = False
    elif angle_right:
        print("towards right")

        angle_factor = tennis_ball.move_angle_right((angle_factor))

        cat_racket.move()
        meme_cat.move()

        played_sound_already = False

    elif not game_over:
        print("backwards")

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
            print("collided at ", tennis_ball.y)

            if(tennis_ball.y > 576):
                tennis_ball.y = 565
                if not played_sound_already:
                    pygame.mixer.find_channel().play(player_racket.hit_effect)
                    played_sound_already = True
                else:
                    pass
            else:
                if not played_sound_already:
                    pygame.mixer.find_channel().play(player_racket.hit_effect)
                    played_sound_already = True

            game_over = False
        else:
            col = "red"
    
    #no collision with racket
    if(tennis_ball.y >= 720):
        played_sound_already = False
        game_over = True

    width = meme_cat.image.get_width()
    height = meme_cat.image.get_height()

    circle_test_group.update(col)

    print("Tennis ball at ", tennis_ball.x, ", ", tennis_ball.y )
    print("Game over is ", game_over)
    print("Forward is ", forward)
    print("Backward is ", backward)
    print(" ")
    print("Angle, factor: ", angle_factor[0], " ", angle_factor[1])
    print("Mouse pos", pos)
    print("Played sound already is ", played_sound_already)
    
    
    pygame.display.flip()


pygame.quit()
