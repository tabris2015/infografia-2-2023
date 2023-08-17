import math

import arcade
import pymunk


class Bird(arcade.Sprite):
    def __init__(self, image: str, distance: float, angle: float, x: float, y: float, space: pymunk.Space):
        super().__init__(image, 1)
        mass = 5
        radius = 12
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = (x, y)
        distance = 100 if distance >=100 else distance
        power = distance * 50
        impulse = power * pymunk.Vec2d(1, 0)
        body.apply_impulse_at_local_point(impulse.rotated(angle))
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 0.8
        shape.friction = 1

        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)


class PassiveObject(arcade.Sprite):
    def __init__(self, image: str, x: float, y: float, space: pymunk.Space):
        super().__init__(image, 1)
        mass = 2
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        body = pymunk.Body(mass, moment)
        body.position = (x, y)
        shape = pymunk.Poly.create_box(body, (self.width, self.height))
        shape.elasticity = 0.8
        shape.friction = 0.4
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)


class Column(PassiveObject):
    def __init__(self, x, y, space):
        super().__init__("11.angry/assets/img/column.png", x, y, space)


class Pig(arcade.Sprite):
    def __init__(self, x: float, y: float, space: pymunk.Space):
        super().__init__("11.angry/assets/img/pig_failed.png", 0.1)
        mass = 2
        moment = pymunk.moment_for_circle(mass, 0, self.width / 2 - 3)
        body = pymunk.Body(mass, moment)
        body.position = (x, y)
        shape = pymunk.Circle(body, self.width / 2 - 3)
        shape.elasticity = 0.8
        shape.friction = 0.4
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)
