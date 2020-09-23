import pygame

# Manage the player 
class Ship:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and its rect.
        self.image = pygame.image.load(self.settings.ship_sprite)
        self.rect = self.image.get_rect()

        # Place the ship initially on midbottom of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movements flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    # Update ship position
    def update(self):

        # Handling movements and screen border
        #if self.moving_up and self.rect.top > self.screen_rect.top:
        #    self.y -= self.settings.ship_speed
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #    self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
    
    # redraw the ship to the screen 
    def blitme(self):
        self.screen.blit(self.image, self.rect)