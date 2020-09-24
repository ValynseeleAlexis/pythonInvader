import sys
import pygame
import settings
import ship
import bullet
import alien


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
        # Setting a sprite group to handle aliens
        self.aliens = pygame.sprite.Group()

        #Setting an alien fleet
        self.create_fleet()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color) # Fill the background with color 
        self.screen.blit(self.bg,(0,0)) #Draw the bg on the screen 
        self.ship.draw_ship() #redraw ship on the screen
        self.bullets.draw(self.screen) #redraw all bullets from the sprite group
        self.aliens.draw(self.screen) #redraw all aliens from the sprite group
        pygame.display.flip() #update the screen

    def run_game(self):
        # start game loop
        while True:
            self.check_events() # listen to keyboard events
            self.ship.update() # update ship coordinates
            self.update_aliens() # Update aliens to make them move
            self.update_bullets() # update bullets coordinates
            self.update_collisions() # Check for collisions
            self.update_screen() # update display

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

    #Game methods

    def fire_bullet(self):
        if(len(self.bullets) < self.settings.max_bullets_allowed):
            new_bullet = bullet.Bullet(self)
            self.bullets.add(new_bullet)
    
    def delete_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) --DEBUG

    def update_bullets(self):
        #Update the position of the bullets and delete old bullets
        self.bullets.update()
        self.delete_bullet()
        self.repop_fleet()

    def create_fleet(self):
        new_alien = alien.Alien(self)
        # self.aliens.add(new_alien)
        available_space_x = self.settings.screen_width - (2 * new_alien.width)
        number_aliens_x = available_space_x // (2 * new_alien.width)

        available_space_y = (self.settings.screen_height + (7 * new_alien.height) - self.ship.height)
        number_rows = available_space_y // (2 * new_alien.height)

        for row_number in range(number_rows):
            for n in range(number_aliens_x):
                self.create_alien(n,row_number)

    def create_alien(self,n,row_number):
        new_alien = alien.Alien(self)
        new_alien.x = new_alien.width + 2 * new_alien.width * n
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.rect.height + 2 * new_alien.rect.height * row_number
        self.aliens.add(new_alien)

    def check_fleet_edges(self):
        for currentAlien in self.aliens.sprites():
            if currentAlien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for currentAlien in self.aliens.sprites():
            currentAlien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def repop_fleet(self):
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

    def update_collisions(self):
        # check for collisions between bullets and aliens sprites, if so delete both 
        collisions = pygame.sprite.pygame.sprite.groupcollide(self.bullets,self.aliens, True,True)

        # Handle collision with the player 
        if pygame.sprite.pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Game Over\n")

    # Other game methods
    
    def to_fullscren(self):
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

# Main programm 
if __name__ == '__main__':
    game = game() 
    game.run_game()


