class Settings():

    def __init__(self):
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 30
        self.ship_limit = 3

        self.bullet_speed = 20
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed = 5.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 
        
