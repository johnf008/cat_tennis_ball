import pygame
import math
import time

pygame.init()

# create player racket


class PlayerRacket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.test_image = pygame.image.load("images/tennis_racket.png").convert_alpha()
        self.x = 250
        self.y = 700
        # return a width and height of an image
        self.size = self.test_image.get_size()

        # create an image half bigger than self.image
        self.image = pygame.transform.scale(self.test_image, (int(self.size[0] * 0.5), int(self.size[1] * 0.5)))
        self.original_image = self.image

    def point_at(self, x, y):
        # calculate distance between racket and mouse
        x_dist = x - player_racket.x
        # -ve because pygame y coordinates increase down screen
        y_dist = -(y - player_racket.y)
        angle = math.degrees(math.atan2(y_dist, x_dist))

        rotated_image = pygame.transform.rotate(self.original_image, angle - 90)
        self.image = rotated_image

class TennisBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/tennis_ball.png").convert_alpha()
        self.original_image = self.image

        #self note: original x and y values are (197, 12)
        self.x = 197
        self.y = 12
        
    def rotate(self, angle):
        rotated_image = pygame.transform.rotate(self.original_image, angle)

        self.image = rotated_image
    def scaleUp(self, factor):
        self.new_size = self.image.get_size()

        bigger_image = pygame.transform.scale_by(self.image, factor)
        self.image = bigger_image
    def scaleDown(self, factor):
        self.image_for_going_back = self.image

        self.new_size = self.image.get_size()

        smaller_image = pygame.transform.scale_by(self.image_for_going_back, factor)
        self.image = smaller_image

# Set up screens
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_racket = PlayerRacket()
all_sprites = pygame.sprite.Group(player_racket)

tennis_ball = TennisBall()

clock = pygame.time.Clock()
run = True
angle = 0
forward = False
backward = True
factor = 20

while run:
    clock.tick(60)
    screen.fill("white")

    # get mouse pos
    pos = pygame.mouse.get_pos()

    player_racket.point_at(pos[0], pos[1])

    # rotate racket
    player_racket_rect = player_racket.image.get_rect(center=(player_racket.x, player_racket.y))

    #rotate tennis ball
    tennis_ball_rect = tennis_ball.image.get_rect(center=(tennis_ball.x, tennis_ball.y))

    screen.blit(player_racket.image, player_racket_rect)
    screen.blit(tennis_ball.image, tennis_ball_rect)

    pygame.draw.circle(screen, 'red', pos, 10)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if tennis_ball.y < 12:
        forward = True
        factor = 1
    
    if tennis_ball.y > 500:
        forward = False
        
    
    if forward:
        tennis_ball.y = tennis_ball.y + 7
        angle = angle + 4

        tennis_ball.rotate(angle)

        factor = factor + 0.015
        tennis_ball.scaleUp(factor)

        print("towards")
        
    else:
        tennis_ball.y = tennis_ball.y - 7
        angle = angle + 4

        tennis_ball.rotate(angle)

        factor = factor - 0.015
        tennis_ball.scaleDown(factor)

        print("backwards")
      
   


    width = tennis_ball.image.get_width()
    height = tennis_ball.image.get_height()

    player_racket.update()
    tennis_ball.update()
    pygame.display.flip()


pygame.quit()
