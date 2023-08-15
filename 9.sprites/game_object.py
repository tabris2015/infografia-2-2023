import arcade
import math


class Player(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 0

    def update(self):
        # angle y change_angle expresados grados
        self.angle += self.change_angle
        angle_rad = math.radians(self.angle)

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


class Bullet(arcade.Sprite):
    def __init__(self, image, scale, speed, angle, center_x, center_y):
        super().__init__(
            image, 
            scale, 
            angle=angle, 
            center_x=center_x, 
            center_y=center_y
        )
        self.velocity = (
            speed * math.cos(math.radians(angle)),
            speed * math.sin(math.radians(angle))
        )
