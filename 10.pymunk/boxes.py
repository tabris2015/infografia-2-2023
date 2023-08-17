import arcade
import pymunk
import timeit
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pymunk"


class PhysicsSprite(arcade.Sprite):
    def __init__(self, pymunk_shape: pymunk.Shape, image):
        super().__init__(image, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape


class CircleSprite(PhysicsSprite):
    def __init__(self, pymunk_shape: pymunk.Shape, image):
        super().__init__(pymunk_shape, image)
        self.width = pymunk_shape.radius * 2
        self.height = pymunk_shape.radius * 2


class BoxSprite(PhysicsSprite):
    def __init__(self, pymunk_shape, filename, width, height):
        super().__init__(pymunk_shape, filename)
        self.width = width
        self.height = height


class App(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # -- Pymunk
        self.space = pymunk.Space()
        self.space.iterations = 35
        self.space.gravity = (0.0, -900.0)

        # Lists of sprites or lines
        self.sprite_list: arcade.SpriteList[PhysicsSprite] = arcade.SpriteList()
        self.static_lines = []

        # Used for dragging shapes around with the mouse
        self.shape_being_dragged = None
        self.last_mouse_position = 0, 0

        self.draw_time = 0
        self.processing_time = 0

        # Create the floor
        floor_height = 80
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, [0, floor_height], [SCREEN_WIDTH, floor_height], 0.0)
        shape.friction = 10
        self.space.add(shape, body)
        self.static_lines.append(shape)

        # Create the stacks of boxes
        for row in range(10):
            for column in range(10):
                size = 32
                mass = 1.0
                x = 500 + column * 32
                y = (floor_height + size / 2) + row * size
                moment = pymunk.moment_for_box(mass, (size, size))
                body = pymunk.Body(mass, moment)
                body.position = pymunk.Vec2d(x, y)
                shape = pymunk.Poly.create_box(body, (size, size))
                shape.elasticity = 0.2
                shape.friction = 0.9
                self.space.add(body, shape)
                # body.sleep()

                sprite = BoxSprite(shape, ":resources:images/tiles/boxCrate_double.png", width=size, height=size)
                self.sprite_list.append(sprite)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # disparar una moneda
            mass = 50
            radius = 10
            inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
            body = pymunk.Body(mass, inertia)
            body.position = (x, y)
            body.velocity = 900, 0
            shape = pymunk.Circle(body, radius, (0, 0))
            shape.friction = 0.4
            self.space.add(body, shape)

            sprite = CircleSprite(shape, ":resources:images/items/coinGold.png")
            self.sprite_list.append(sprite)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.last_mouse_position = x, y
            shape_list = self.space.point_query((x, y), 1, pymunk.ShapeFilter())
            if len(shape_list) > 0:
                self.shape_being_dragged = shape_list[0]

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.shape_being_dragged is not None:
            self.last_mouse_position = (x, y)
            self.shape_being_dragged.shape.body.position = self.last_mouse_position
            self.shape_being_dragged.shape.body.velocity = (dx * 20, dy * 20)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.shape_being_dragged = None

    def on_update(self, delta_time: float):
        self.space.step(1 / 60)
        self.sprite_list.update()
        for sprite in self.sprite_list:
            sprite.center_x = sprite.pymunk_shape.body.position.x
            sprite.center_y = sprite.pymunk_shape.body.position.y
            sprite.angle = math.degrees(sprite.pymunk_shape.body.angle)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()


if __name__ == "__main__":
    app = App(800, 800, "hola")
    arcade.run()