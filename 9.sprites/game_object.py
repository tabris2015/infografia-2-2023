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

        self.center_x += self.speed * math.cos(angle_rad)
        self.center_y += self.speed * math.sin(angle_rad)
