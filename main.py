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
        self.y = 720

        # return a width and height of an image
        self.size = self.test_image.get_size()

        # create an image half bigger than self.image
        self.image = pygame.transform.scale(self.test_image, (int(self.size[0] * 0.5), int(self.size[1] * 0.5)))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.mask_image = pygame.mask.from_surface(self.image)
        self.mask = pygame.mask.from_surface(self.image)

        #self.original_mask_image = self.mask        

    def point_at(self, x, y):
        # calculate distance between racket and mouse
        #x_dist = x - player_racket.x
        # -ve because pygame y coordinates increase down screen
        #y_dist = -(y - player_racket.y)

        #angle = math.degrees(math.atan2(y_dist, x_dist))

        #rotated_image = pygame.transform.rotate(self.original_image, angle - 90)

        
        #self.image = rotated_image

        #self.rect = self.image.get_rect(center=(self.x, self.y))

        self.rect.center = (x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

        #self.image_new_mask = pygame.mask.from_surface(self.image)
        #self.image_of_new_mask = self.image_new_mask.to_surface()
    def update():
        position = pygame.mouse.get_pos()
        
        
        

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
        self.x = 197
        self.y = 12

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)
        
    def rotate(self, angle):
        rotated_image = pygame.transform.rotate(self.original_image, angle)

        self.image = rotated_image

        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image)

        #self.image_new_mask = pygame.mask.from_surface(self.image)
        #self.image_of_new_mask = self.image_new_mask.to_surface()

    def scaleUp(self, factor):
        self.new_size = self.image.get_size()

        bigger_image = pygame.transform.scale_by(self.image, factor)
        self.image = bigger_image

        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image)

        #self.image_new_mask = pygame.mask.from_surface(self.image)
        #self.image_of_new_mask = self.image_new_mask.to_surface()

    def scaleDown(self, factor):
        self.image_for_going_back = self.image

        self.new_size = self.image.get_size()

        smaller_image = pygame.transform.scale_by(self.image_for_going_back, factor)
        self.image = smaller_image

        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mask = pygame.mask.from_surface(self.image)

        #self.image_new_mask = pygame.mask.from_surface(self.image)
        #self.image_of_new_mask = self.image_new_mask.to_surface()
    
        

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
        
    

# Set up screens
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_racket = PlayerRacket()
tennis_ball = TennisBall()

col = "red"
circle_test = RedCircleTest(col)

player_racket_group = pygame.sprite.Group()
tennis_ball_group = pygame.sprite.Group()

circle_test_group = pygame.sprite.Group()


player_racket_group.add(player_racket)
tennis_ball_group.add(tennis_ball)
circle_test_group.add(circle_test)

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

    #draw mask images
    #screen.blit(player_racket.mask, (0,0))
    #screen.blit(tennis_ball.image_of_mask, (5,0))


    #draw images
    player_racket_group.draw(screen)
   
    tennis_ball_group.draw(screen)

    #circle_test_group.draw(screen)

    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if tennis_ball.y <= 12:
        forward = True
        factor = 1
    
    
        
    
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
    
    if pygame.sprite.spritecollide(player_racket, tennis_ball_group, False):
        col = "blue"
        if pygame.sprite.spritecollide(player_racket, tennis_ball_group, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(player_racket, tennis_ball_group, False, pygame.sprite.collide_mask):
            forward = False
            col = "green"
            print("collided at ", tennis_ball.y)
        else:
            col = "red"
    
    if tennis_ball.y == 575:
        forward = 0
    pygame.draw.rect(screen, "black", tennis_ball.rect, 1)

    width = tennis_ball.image.get_width()
    height = tennis_ball.image.get_height()

    circle_test_group.update(col)

    
    pygame.display.flip()


pygame.quit()
