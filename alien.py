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

    def draw_alien(self):
        self.screen.blit(self.image,self.rect)