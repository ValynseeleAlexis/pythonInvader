import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # Class that modelise a single alien

    def __init__(self,game):
        
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien sprite
        self.image = pygame.image.load(self.settings.alien_sprite)
        self.rect = self.image.get_rect()

        # Constant
        self.width = self.rect.width 
        self.height = self.rect.height 

        # Start each new alien near top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Alien coordinates
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        # To know if the alien touched the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def draw_alien(self):
        self.screen.blit(self.image,self.rect)