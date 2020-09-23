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

                # Other controls
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.fire_bullet()
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
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #redraw ship on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self):
        # start game loop
        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_screen()

    #Game methods

    def fire_bullet(self):
        new_bullet = bullet.Bullet(self)
        self.bullets.add(new_bullet)

# Main programm 
if __name__ == '__main__':
    game = game() 
    game.run_game()


