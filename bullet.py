import pygame
from pygame.sprite import Sprite

# Modelise the bullet that can shoot the player 
class Bullet(Sprite):

    def __init__(self, game):

        #Settings
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        # Making a rectangle for the bullet either with pure rect or a bmp file
        self.image = pygame.image.load(self.settings.bullet_sprite)
        self.rect = self.image.get_rect()
        #self.rect.width = self.settings.bullet_width
        #self.rect.height = self.settings.bullet_height

       
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.height = self.rect.y
        self.width = self.rect.x

        # Bullet coordinate
        self.y = float(self.rect.y)

    # Update bullet coordinate
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    # Redraw the bullet to the screen
    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
