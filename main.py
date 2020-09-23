import sys
import pygame
import settings
import ship
import bullet


class game:

    # Top class to manage the game

    # Init the game
    def __init__(self):

        pygame.init()
        # Get all setings variables from the settings class
        self.settings = settings.Settings()

        #Setting up the window 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.window_caption)
        self.bg = pygame.image.load(self.settings.bg_image)

        # Setting the ship
        self.ship = ship.Ship(self)

        # Setting a sprite group to handle bullets
        self.bullets = pygame.sprite.Group()

    # Method that listen to all events in the game
    def check_events(self):
        for event in pygame.event.get():
            
            # Quitting
            if event.type == pygame.QUIT:
                sys.exit()

            # KeyDown
            elif event.type == pygame.KEYDOWN:

                #Movements
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
  
                # Ship controls
                if event.key == pygame.K_SPACE:
                    self.fire_bullet()

                # Game controls
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_f:
                    self.to_fullscren()
            # KeyUp
            elif event.type == pygame.KEYUP:

                #Movements
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def update_screen(self):
        self.screen.fill(self.settings.bg_color) # Fill the background with color 
        self.screen.blit(self.bg,(0,0)) #Draw the bg on the screen 
        self.ship.blitme() #redraw ship on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self):
        # start game loop
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

    #Game methods

    def fire_bullet(self):
        if(len(self.bullets) < self.settings.max_bullets_allowed):
            new_bullet = bullet.Bullet(self)
            self.bullets.add(new_bullet)
    
    def delete_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def update_bullets(self):
        #Update the position of the bullets and delete old bullets
        self.bullets.update()
        self.delete_bullet()

    # Other game methods
    def to_fullscren(self):
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

# Main programm 
if __name__ == '__main__':
    game = game() 
    game.run_game()


