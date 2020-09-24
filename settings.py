class Settings:
    #   Class that manage the game's settiings

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        self.bg_image = "./assets/bg.jpg"
        self.window_caption = "JulienInvader"

        # Ship settings
        self.ship_speed = 5
        self.ship_sprite = "./assets/ship.bmp"

        # Bullet settings
        self.bullet_sprite = "./assets/bullet.bmp"
        self.bullet_speed = 5.0
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets_allowed = 3

        # Alien settings
        self.alien_sprite = "./assets/alien.bmp"
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = -1